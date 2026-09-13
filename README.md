# Timeline of LLMs
## (based on JQuery Timeline widget)

### [Website](https://llm-timeline-two.vercel.app/)

<img width="979" height="792" alt="Screenshot_of_timeline" src="https://github.com/user-attachments/assets/8877e956-6f33-4345-8ad6-6e6e235fd782" />

# My Process

---

## Update (July 2026)

Edit - created a python script to output JSON data for input. As this information changes rapidly, I thought a mechanism to update the data should be implemented.

To update the data:

`cd ~Document/Projects/llm-timeline/src/lib/data`

`uv run fetch_llm_table.py > llms<Today's Date>.json`

(really need to automate this)

Edit Timeline.svelte component to import the above output file

`pnpm dev`

to check to see if it works (sometimes wikipedia changes their html page formats)

---

First, I went to the wikipedia page for a [list of large language models](https://en.wikipedia.org/wiki/List_of_large_language_models). I copied the table and pasted it into a spreadsheet instead of having Claude scrape it. (Next time, I will paste the table into Claude and transform the data into a JSON data structure.)

Second, I chatted with Claude about how to create a prompt to get what I wanted. 

I then created a sveltekit project:

```
npx sv create llm-timeline
```

(I selected the skeleton project and typescript)


Then selected the llm-timeline directory in Claude Code and I started prompting Claude as follows.

# Prompts for Claude Code

```
I have a SvelteKit project. I want a single Timeline.svelte component first, then wire it into a SvelteKit route (+page.svelte).

Build the Timeline.svelte component modeled after jQuery Timeline found in the jquery.timeline-2.1.3 folder.

Use these data found in List_of_LLMs.xlsx.

The timeline should be horizontal, with events showing Name and release date. On hover, show Developer, Number of parameters (billion), Corpus size,  Training Costs and Notes. Keep all hyperlinks.

Title should be "A Timeline of LLMs".
Use the styles found in the ./src/lib/styles directory. 

Stretch the x-axis so that the elements don't overlap and get rid of the scrollbar adding forward and backward arrows in the middle of the left and right hand margins

Make the timeline a little taller and add a github icon button in the lower right linked to the github repository: https://github.com/awindest/llm-timeline

```

Here is my CLAUDE.md file:

# Claude Code Project Rules — llm-timeline

## Stack
- Sveltekit, TypeScript 5, Svelte


## Critical Rules
- Never delete `public/.nojekyll`
- Build with `pnpm build`
- Never add workflow files that also trigger on `push: main` (causes deployment races)

## Design System
- All design tokens live in `styles/tokens.ts` — never hardcode colors/sizes
- `colors.bgPage` (#0f172a) is the root background on ALL pages — no exceptions
- Use only sizes from `typography.scale`, spacing from `space.*`, radius from `radius.*`

## File Structure
- Page-specific styles: CSS Modules or inline styles with tokens only
- `styles/globals.css`: global reset ONLY (box-sizing + body margin)
- Local components stay in the page file — only shared components go in `components/`


# Design Notes for Version 2

## Second Claude Interaction Session:

This all looks correct now. Let me quickly verify with the current dataset (all 10 lanes are likely in use given density) that the numbers reproduce the original 370/754, then copy the file to outputs.

Here's what changed, all in the <script> block:

1. AXIS_Y is no longer hardcoded to 370 — it's now computed from how many lanes are actually used above the axis, so the top padding above the highest card stays constant (TOP_PAD = 64px) regardless of depth.
1. positioned (lane assignment) no longer reads LANES.length — it just uses NUM_LANES_ABOVE + NUM_LANES_BELOW directly, since lane assignment never actually needed the y-coordinates, just the count.
1. A new block right after positioned scans the assigned lanes to find maxLaneAboveUsed / maxLaneBelowUsed, converts those into depthAbove / depthBelow (clamped between MIN_LANE_DEPTH = 1 and 5), and only then computes AXIS_Y, LANES, BOTTOM_AXIS_Y, and INNER_H from those depths.
1. INNER_H is now a formula, not a constant — it grows or shrinks with depthBelow the same way AXIS_Y grows or shrinks with depthAbove.

The math reproduces your original numbers exactly when all 10 lanes are in use (AXIS_Y=370, INNER_H=754), and shrinks proportionally when fewer lanes are needed — e.g. a dataset that only ever needs 1 lane each side collapses to INNER_H=258.

Two knobs worth knowing about:

- MIN_LANE_DEPTH = 1 is your "fixed minimum" — bump it to 2 or 3 if a single-lane layout feels too cramped.
- TOP_PAD and BOTTOM_PAD control the padding above the topmost card and below the bottommost, independent of lane count.

Here's what changed this time, all in the x-axis math:

1. YEAR_W (fixed 1600px/year) is gone. Each year now gets its own width, computed from how many cards land in it that year.
1. New block, "Dynamic x-axis":
- countPerYear — tallies how many cards fall in each year (2018–2026).
- yearWidths — Math.max(MIN_YEAR_W, countPerYear[y] * PX_PER_CARD). A quiet year floors out at MIN_YEAR_W = 500px; a busy year stretches linearly, 50px wider per card.
- yearStartX — running cumulative offset, so years are laid out left to right at their own widths.
- INNER_W is now the sum of all year widths + padding, instead of a flat multiple.
1. dateToX is rewritten to look up which year a date falls in and place it proportionally within that year's (now variable) width slot, instead of a uniform px-per-day scale.

Two knobs to tune once you see it against your real data:

- MIN_YEAR_W (500) — how compressed a quiet year can get.
- PX_PER_CARD (50) — how aggressively a busy year stretches. Raise it if dense years still show overlap, lower it if things feel too spread out.

If you find year-level granularity too coarse (e.g. one crowded month in an otherwise-quiet year still gets the whole year stretched), the same technique drops in at month granularity — just say the word and I'll adjust DATA_YEARS/countPerYear to bucket by month instead of year.

Adding hover over the bottom x axis month tick to show the Month and Year as in Jul, 2025?

Here's what I added, all scoped to the bottom axis tick marks:

1. Tick now carries a date (a clone of the day being ticked), not just x/isMonthStart.
1. A transparent <rect> hit-area sits on top of each month-start tick in the bottom tick SVG — the actual tick line is only 1.5px wide, too thin to hover reliably, so this gives it a 12×28px target with pointer-events: auto to punch through the SVG's pointer-events: none.
1. hoveredTick state + enterTick/leaveTick track which month is being hovered, following the same mousemove-driven positioning pattern as your existing card tooltip.
1. A small fixed tooltip renders next to the cursor showing fmtMonthYear(hoveredTick), which formats as Jul, 2025 (comma included, unlike the existing fmtDate used for cards).

Only the bottom axis tick marks got this — the day ticks and the two axis-line tick blocks near AXIS_Y are untouched, as requested.
