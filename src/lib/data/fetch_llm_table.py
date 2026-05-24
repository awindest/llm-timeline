#!/usr/bin/env python3
"""
Fetches all wikitables from the Wikipedia "List of large language models" page
using the MediaWiki Action API and outputs a JSON array matching the LLM schema.
"""

import json
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup


API_URL    = "https://en.wikipedia.org/w/api.php"
PAGE_TITLE = "List_of_large_language_models"
WIKI_BASE  = "https://en.wikipedia.org"

COLUMN_MAP = {
    "name":                 "name",
    "release date":         "date",
    "developer":            "developer",
    "number of parameters": "parameters",
    "corpus size":          "corpus",
    "training cost":        "cost",
    "notes":                "notes",
}


# ---------------------------------------------------------------------------
# 1. Fetch rendered HTML via MediaWiki Action API
# ---------------------------------------------------------------------------

def fetch_html(title: str) -> str:
    params = urllib.parse.urlencode({
        "action": "parse", "page": title,
        "prop": "text", "format": "json", "formatversion": "2",
    })
    req = urllib.request.Request(
        f"{API_URL}?{params}",
        headers={"User-Agent": "WikiTableFetcher/1.0"},
    )
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read().decode("utf-8"))
    return data["parse"]["text"]


# ---------------------------------------------------------------------------
# 2. Cell helper
# ---------------------------------------------------------------------------

def cell_text_href(cell) -> dict:
    """Return {"text": str, "href": str, "sort": str} for a <th> or <td> element.

    Wikipedia date cells store the date only inside hidden markup. We try all
    known patterns to extract an 8-digit YYYYMMDD sort value:
      A) <td data-sort-value="20180611">...</td>
      B) <td><span data-sort-value="20180611">...</span></td>
      C) <td><span style="display:none">20180611</span>visible text</td>
    """
    for sup in cell.find_all("sup"):
        sup.decompose()

    sort_value = ""

    # Pattern A: data-sort-value on the <td> itself
    sv = cell.get("data-sort-value", "")
    if sv and sv.strip().isdigit():
        sort_value = sv.strip()

    # Pattern B: data-sort-value on a child span
    if not sort_value:
        for span in cell.find_all("span", attrs={"data-sort-value": True}):
            sv = span.get("data-sort-value", "").strip()
            if sv.isdigit():
                sort_value = sv
                break

    # Pattern C: display:none span — its text IS the sort value
    if not sort_value:
        for span in cell.find_all("span"):
            if "display:none" in span.get("style", "").replace(" ", ""):
                sv = span.get_text(strip=True)
                if sv.isdigit():
                    sort_value = sv
                span.decompose()  # remove so it doesn't pollute get_text()

    text = cell.get_text(separator=" ", strip=True)
    href = ""
    link = cell.find("a", href=lambda h: h and h.startswith("/wiki/") and ":" not in h[6:])
    if link:
        href = WIKI_BASE + link["href"]
    return {"text": text, "href": href, "sort": sort_value}


# ---------------------------------------------------------------------------
# 3. Expand a multi-row header block into a flat list of column labels,
#    correctly handling rowspan and colspan.
# ---------------------------------------------------------------------------

def extract_headers(header_rows: list) -> list[str]:
    grid: dict[tuple[int, int], str] = {}
    for ri, tr in enumerate(header_rows):
        ci = 0
        for cell in tr.find_all(["th", "td"]):
            while (ri, ci) in grid:
                ci += 1
            # Strip footnote superscripts before reading the header label
            for sup in cell.find_all("sup"):
                sup.decompose()
            label = cell.get_text(strip=True)
            rs = int(cell.get("rowspan", 1))
            cs = int(cell.get("colspan", 1))
            for dr in range(rs):
                for dc in range(cs):
                    grid[(ri + dr, ci + dc)] = label
            ci += cs

    if not grid:
        return []

    num_cols = max(c for (_, c) in grid) + 1
    num_rows = max(r for (r, _) in grid) + 1
    # Use the bottom-most label per column (most specific in merged headers)
    return [
        next((grid[(ri, ci)] for ri in range(num_rows - 1, -1, -1) if (ri, ci) in grid), "")
        for ci in range(num_cols)
    ]


# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# 4. Parse all wikitables — with full rowspan/colspan grid expansion
# ---------------------------------------------------------------------------

def parse_tables(html: str) -> list[list[dict]]:
    import re as _re
    soup = BeautifulSoup(html, "html.parser")
    tables = []
    EMPTY = {"text": "", "href": "", "sort": ""}

    for table in soup.find_all("table", class_="wikitable"):
        # Find the year from the nearest preceding heading (e.g. "2025", "Early 2024")
        year_hint = 0
        for sibling in table.find_all_previous(["h2", "h3", "h4"]):
            heading_text = sibling.get_text(strip=True)
            ym = _re.search(r"(20\d{2})", heading_text)
            if ym:
                year_hint = int(ym.group(1))
                break
        all_rows = table.find_all("tr")

        # Split leading all-<th> rows as header rows
        header_rows, data_rows, found_data = [], [], False
        for tr in all_rows:
            ths, tds = tr.find_all("th"), tr.find_all("td")
            if not found_data and ths and not tds:
                header_rows.append(tr)
            else:
                found_data = True
                if tr.find_all(["th", "td"]):
                    data_rows.append(tr)

        if not header_rows:
            continue
        headers = extract_headers(header_rows)
        if not headers:
            continue
        num_cols = len(headers)

        # rowspan_carry[col] = [rows_remaining, cell_value]
        # Tracks cells from previous rows that span into subsequent rows.
        rowspan_carry: dict[int, list] = {}

        rows = []
        for tr in data_rows:
            raw_cells = tr.find_all(["th", "td"])
            # Expand each physical cell by its colspan into a flat list
            physical = []
            for c in raw_cells:
                val = cell_text_href(c)
                for _ in range(int(c.get("colspan", 1))):
                    physical.append({"val": val, "rowspan": int(c.get("rowspan", 1))})

            # Build the full logical row by merging carried rowspan values
            logical = []
            phys_idx = 0
            for col in range(num_cols):
                if col in rowspan_carry and rowspan_carry[col][0] > 0:
                    logical.append(rowspan_carry[col][1])
                    rowspan_carry[col][0] -= 1
                    if rowspan_carry[col][0] == 0:
                        del rowspan_carry[col]
                else:
                    if phys_idx < len(physical):
                        cell = physical[phys_idx]
                        logical.append(cell["val"])
                        if cell["rowspan"] > 1:
                            rowspan_carry[col] = [cell["rowspan"] - 1, cell["val"]]
                        phys_idx += 1
                    else:
                        logical.append(EMPTY)

            row = {headers[i]: logical[i] for i in range(num_cols)}
            row["__year_hint__"] = year_hint
            rows.append(row)

        if rows:
            tables.append(rows)

    return tables

# 5. Map raw rows → LLM schema
# ---------------------------------------------------------------------------

# Month abbreviation -> number
_MONTHS = {m: f"{i+1:02d}" for i, m in enumerate(
    ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
)}

def format_date(cell: dict, year_hint: int = 0) -> str:
    """Convert a Wikipedia abbreviated date cell to YYYY-MM-DD.

    Handles all observed formats:
      "Jun 11"      (month day, no year — use year_hint)
      "Oct 2018"    (month year)
      "Feb 2024"    (month year)
      "Jan 20"      (month 2-digit-day, no year — use year_hint)
      "Jun 11, 2018" (full date)
      "20180611"    (sort value)
      "2018-06-11"  (already ISO)
    """
    import re
    from datetime import datetime

    sort = cell.get("sort", "").strip()
    text = cell.get("text", "").strip()

    # Already ISO format in sort value
    if re.match(r"^\d{4}-\d{2}-\d{2}$", sort):
        return sort

    # 8-digit YYYYMMDD sort value
    m = re.match(r"^(\d{8})", sort)
    if m:
        s = m.group(1)
        return f"{s[:4]}-{s[4:6]}-{s[6:]}"

    # Work from the visible text
    # Full date: "June 11, 2018" or "Jun 11, 2018"
    m = re.match(r"^(\w+)\s+(\d{1,2}),\s+(\d{4})$", text)
    if m:
        try:
            dt = datetime.strptime(text, "%B %d, %Y")
            return dt.strftime("%Y-%m-%d")
        except ValueError:
            try:
                dt = datetime.strptime(text, "%b %d, %Y")
                return dt.strftime("%Y-%m-%d")
            except ValueError:
                pass

    # "Mon YYYY" e.g. "Oct 2018", "Feb 2024"
    m = re.match(r"^(\w{3})\s+(\d{4})$", text)
    if m:
        mon, yr = m.group(1), m.group(2)
        mm = _MONTHS.get(mon)
        if mm:
            return f"{yr}-{mm}-01"

    # "Mon DD" e.g. "Jun 11", "Jan 20" — day ≤31, no year: use year_hint
    m = re.match(r"^(\w{3})\s+(\d{1,2})$", text)
    if m:
        mon, day = m.group(1), m.group(2)
        mm = _MONTHS.get(mon)
        yr = str(year_hint) if year_hint else "????"
        if mm:
            return f"{yr}-{mm}-{int(day):02d}"

    return text


def format_parameters(text: str) -> str:
    """Normalise parameter counts to a billions decimal string.
       e.g. '117M' -> '0.117',  '7B' -> '7',  '1.5B' -> '1.5',  '540B' -> '540'
    """
    import re
    if not text or text.strip().lower() in ("unknown", ""):
        return text
    # Match a number followed by an optional B/M/T suffix
    m = re.match(r"^~?([\d,.]+)\s*([BMTbmt])?", text.strip())
    if not m:
        return text
    number = float(m.group(1).replace(",", ""))
    suffix = (m.group(2) or "B").upper()
    if suffix == "M":
        number = number / 1000
    elif suffix == "T":
        number = number * 1000
    # Format: drop trailing zeros, keep as plain decimal string
    formatted = f"{number:g}"
    return formatted


def map_row(raw: dict) -> dict:
    year_hint = raw.pop("__year_hint__", 0)
    resolved: dict[str, dict] = {}
    for col, cell in raw.items():
        field = COLUMN_MAP.get(col.strip().lower())
        if field and field not in resolved:
            resolved[field] = cell

    def text(f): return resolved.get(f, {}).get("text", "")
    def href(f): return resolved.get(f, {}).get("href", "") or "Unknown"

    return {
        "name":          text("name"),
        "nameLink":      href("name"),
        "date":          format_date(resolved.get("date", {}), year_hint),
        "developer":     text("developer"),
        "developerLink": href("developer"),
        "parameters":    format_parameters(text("parameters")),
        "corpus":        text("corpus"),
        "cost":          text("cost"),
        "notes":         text("notes"),
    }


# ---------------------------------------------------------------------------
# 6. Main
# ---------------------------------------------------------------------------

def main():
    import sys
    debug = "--debug" in sys.argv

    html   = fetch_html(PAGE_TITLE)
    tables = parse_tables(html)

    if debug:
        for i, table in enumerate(tables):
            print(f"\n=== TABLE {i} HEADERS: {list(table[0].keys()) if table else []} ===", file=sys.stderr)
            for row in table[:3]:
                date_cell = row.get("Release date", row.get("release date", {}))
                print(f"  name={row.get('Name',{}).get('text','?')!r}  "
                      f"date_sort={date_cell.get('sort','')!r}  "
                      f"date_text={date_cell.get('text','')!r}  "
                      f"-> {format_date(date_cell)!r}", file=sys.stderr)
        return

    records = [map_row(row) for table in tables for row in table]
    print(json.dumps(records, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
