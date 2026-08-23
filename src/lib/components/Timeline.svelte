<script lang="ts">
	import { onMount } from 'svelte'
	import { colors, typography, space, radius, shadow } from '$lib/styles/tokens'
	import { browser } from '$app/environment'

	interface LLM {
		name: string
		nameLink: string
		date: string
		developer: string
		developerLink: string
		parameters: string
		corpus: string
		cost: string
		notes: string
	}
	// ── Data (should be automated and grok the latest data.json file) ───────────────────

	// import llmsData from '$lib/data/llmsMay23.json'; // easiest way
	// import llmsData from '$lib/data/llmsJun9.json'; // easiest way
	// import llmsData from '$lib/data/llmsJun17.json'; // easiest way
	import llmsData from '$lib/data/llmsAug22.json' // easiest way

	// ── Remapping Schema ────────────────────────────────────────────────────────────────

	// const keyMap: Record<string, string> = {
	// 		"Name": "name",
	// 		"Release date": "date",
	//         "Developer": "developer",
	// 		"Number of parameters": "parameters",
	// 		"Corpus size": "corpus",
	// 		"Training cost": "cost",
	// 		"License": "license",
	//         "Notes": "notes"
	// };
	// 	 const llmsData = llmsDataRaw.map(({

	// const renamed = data.map(obj =>
	//   Object.fromEntries(
	//     Object.entries(obj).map(([k, v]) => [keyMap[k] ?? k, v])
	//   )
	// );
	// ── Geometry ────────────────────────────────────────────────────────────────
	// Year width should be variable as the density increases over time and the
	// cards begin overlapping each other
	const YEAR_W = 1600 // used to be 900; px per year — wide enough to prevent card overlap
	const PAD_L = 48 // left padding
	const PAD_R = 64 // right padding
	const START = new Date(2018, 0, 1)
	const END_YEAR = 2027
	const END = new Date(END_YEAR, 0, 1)
	const SPAN_MS = END.getTime() - START.getTime()
	const INNER_W = (END_YEAR - 2018) * YEAR_W + PAD_L + PAD_R

	const AXIS_Y = 370 // y of axis line
	const CARD_W = 106 // card width
	const CARD_H = 42 // card height
	const DOT_D = 8 // dot diameter
	const CONN_PAD = 16 // gap from dot to card
	const LANE_GAP = 62 // vertical distance between lanes

	// 10 lanes: 0-4 above, 5-9 below (closest first)
	// AXIS_Y=370, CONN_PAD=16, CARD_H=42, LANE_GAP=62
	// Lane 4 (top):    370 - 16 - 42 - 62*4 = 64   ✓
	// Lane 9 (bottom): 370 + 16 + 62*4 + 42 = 676
	const LANES = [
		{ y: AXIS_Y - CONN_PAD - CARD_H, above: true }, // 0
		{ y: AXIS_Y - CONN_PAD - CARD_H - LANE_GAP, above: true }, // 1
		{ y: AXIS_Y - CONN_PAD - CARD_H - LANE_GAP * 2, above: true }, // 2
		{ y: AXIS_Y - CONN_PAD - CARD_H - LANE_GAP * 3, above: true }, // 3
		{ y: AXIS_Y - CONN_PAD - CARD_H - LANE_GAP * 4, above: true }, // 4
		{ y: AXIS_Y + CONN_PAD, above: false }, // 5
		{ y: AXIS_Y + CONN_PAD + LANE_GAP, above: false }, // 6
		{ y: AXIS_Y + CONN_PAD + LANE_GAP * 2, above: false }, // 7
		{ y: AXIS_Y + CONN_PAD + LANE_GAP * 3, above: false }, // 8
		{ y: AXIS_Y + CONN_PAD + LANE_GAP * 4, above: false } // 9
	] as const

	const INNER_H = 676 + 42 + 36 // bottom of lane 9 card + bottom padding

	let scrollContainer: HTMLDivElement // div to scroll to current offerings

	// ── Tick generation ──────────────────────────────────────────────────────────
	interface Tick {
		x: number
		isMonthStart: boolean
	}

	const ticks: Tick[] = (() => {
		const out: Tick[] = []
		const d = new Date(START)
		while (d < END) {
			out.push({
				x: dateToX(d),
				isMonthStart: d.getDate() === 1
			})
			d.setDate(d.getDate() + 1)
		}
		return out
	})()

	// Tick sizing — small for days, larger for month starts
	const DAY_TICK_LEN = 5
	const MONTH_TICK_LEN = 12
	const TICK_STROKE_DAY = 1
	const TICK_STROKE_MONTH = 1.5
	// ── Bottom axis position ─────────────────────────────────────────────────────
	const BOTTOM_AXIS_Y = INNER_H - 36 // sits just above the year-label row

	// ── Helpers ─────────────────────────────────────────────────────────────────
	function parseDate(s: string): Date {
		if (!s) return START
		s = s.replace(/\[\w+\]/g, '').trim()
		if (/^\d{4}-\d{2}-\d{2}$/.test(s)) {
			const [y, m, d] = s.split('-').map(Number)
			return new Date(y, m - 1, d)
		}
		const md = s.match(/^(\w+)\s+(\d+),?\s*(\d{4})$/)
		if (md) return new Date(`${md[1]} ${md[2]}, ${md[3]}`)
		const my = s.match(/^(\w+)\s+(\d{4})$/)
		if (my) return new Date(`${my[1]} 1, ${my[2]}`)
		const d = new Date(s)
		return isNaN(d.getTime()) ? START : d
	}

	function dateToX(d: Date): number {
		return PAD_L + ((d.getTime() - START.getTime()) / SPAN_MS) * ((END_YEAR - 2018) * YEAR_W)
	}

	function fmtDate(d: Date): string {
		return d.toLocaleDateString('en-US', { year: 'numeric', month: 'short' })
	}

	function devColor(dev: string): string {
		const d = dev.toLowerCase()
		if (d.includes('openai')) return colors.indigo
		if (d.includes('google') || d.includes('deepmind')) return colors.cyan
		if (d.includes('meta')) return colors.violet
		if (d.includes('anthropic')) return '#D97757'
		if (d.includes('microsoft')) return colors.amber
		if (d.includes('deepseek')) return colors.pink
		if (d.includes('mistral')) return '#fb923c'
		if (d.includes('xai')) return '#e879f9'
		if (d.includes('alibaba')) return '#e60f4c'
		if (d.includes('z.ai')) return '#9D00FF'
		if (d.includes('moonshot ai')) return '#0021F3'
		if (d.includes('nvidia')) return '#76B900' // Nvidia's logo color

		return colors.textSecondary
	}

	// ── Lane assignment ──────────────────────────────────────────────────────────
	interface Positioned extends LLM {
		x: number
		lane: number
		color: string
		parsedDate: Date
	}

	const positioned: Positioned[] = (() => {
		const MIN_SEP = CARD_W + 10 // was 10
		const LANE_ORDER = [0, 5, 1, 6, 2, 7, 3, 8, 4, 9]
		const laneMax = LANES.map(() => -Infinity)

		return llmsData
			.map((llm) => ({
				...llm,
				parsedDate: parseDate(llm.date),
				color: devColor(llm.developer),
				x: 0,
				lane: 0
			}))
			.sort((a, b) => a.parsedDate.getTime() - b.parsedDate.getTime())
			.map((ev) => {
				ev.x = dateToX(ev.parsedDate)
				let best = -1
				for (const li of LANE_ORDER) {
					if (ev.x >= laneMax[li] + MIN_SEP) {
						best = li
						break
					}
				}
				if (best === -1) best = laneMax.indexOf(Math.min(...laneMax))
				laneMax[best] = ev.x
				ev.lane = best
				return ev
			})
	})()

	const YEARS = Array.from({ length: END_YEAR - 2018 + 1 }, (_, i) => 2018 + i)

	// ── Pan state ────────────────────────────────────────────────────────────────
	let viewOffset = $state(0)
	let containerW = $state(1200)
	let maxOffset = $derived(Math.max(0, INNER_W - containerW))

	function pan(dir: 1 | -1) {
		autoScrollCancelled = true // manual interaction wins from now on
		isAutoScrolling = false // pan clicks should use the eased transition
		const step = Math.max(containerW * 0.75, 400)
		viewOffset = Math.max(0, Math.min(maxOffset, viewOffset + dir * step))
	}

	// ── Hover state ──────────────────────────────────────────────────────────────
	let hovered = $state<Positioned | null>(null)
	let mouseX = $state(0)
	let mouseY = $state(0)
	let tipFromEvent = $state(false)
	let clearTimer: ReturnType<typeof setTimeout> | null = null

	function enterEvent(ev: Positioned) {
		if (clearTimer) {
			clearTimeout(clearTimer)
			clearTimer = null
		}
		hovered = ev
		tipFromEvent = true
	}
	function leaveEvent() {
		clearTimer = setTimeout(() => {
			if (!tipFromEvent) hovered = null
		}, 160)
		tipFromEvent = false
	}
	function enterTooltip() {
		if (clearTimer) {
			clearTimeout(clearTimer)
			clearTimer = null
		}
	}
	function leaveTooltip() {
		hovered = null
	}

	// Tooltip position
	let tipX = $derived(mouseX + 16)
	let tipY = $derived(mouseY - 180)

	// ── Auto-scroll state ──────────────────────────────────────────────────────
	let autoScrollCancelled = $state(false)
	let isAutoScrolling = $state(true) // controls whether the CSS transition applies

	function autoScrollTimeline(targetOffset: number, duration: number) {
		const startOffset = viewOffset
		const diff = targetOffset - startOffset
		let start: number | null = null

		function step(timestamp: number) {
			if (autoScrollCancelled) return // bail if the user took control

			if (start === null) start = timestamp
			const timeElapsed = timestamp - start
			const progress = Math.min(timeElapsed / duration, 1)

			viewOffset = startOffset + diff * progress // same state pan() uses

			if (timeElapsed < duration) {
				requestAnimationFrame(step)
			} else {
				isAutoScrolling = false // re-enable the eased transition once done
			}
		}

		requestAnimationFrame(step)
	}

	onMount(() => {
		// Start the slow horizontal scrolling loop: target, duration
		autoScrollTimeline(maxOffset, 40000) // animate viewOffset: 0 -> maxOffset
	})
</script>

<svelte:window
	onmousemove={(e) => {
		mouseX = e.clientX
		mouseY = e.clientY
	}}
/>

<section
	style="
  background: {colors.bgPage};
  padding: {space[10]}px {space[6]}px {space[8]}px;
  min-height: 100vh;
  font-family: {typography.fontSans};
"
>
	<!-- Title -->
	<h1
		style="
    color: {colors.textPrimary};
    font-size: {typography.scale.h2}px;
    font-weight: {typography.weight.bold};
    margin: 0 0 {space[3]}px;
    text-align: center;
    letter-spacing: {typography.letterSpacing.wide}px;
  "
	>
		A Timeline of LLMs
	</h1>

	<!-- Subtitle / count -->
	<p
		style="
    color: {colors.textMuted};
    font-size: {typography.scale.body}px;
    text-align: center;
    margin: 0 0 {space[6]}px;
  "
	>
		{positioned.length} models · 2018–2026 · Hover over an event for details ·
		<a
			href="https://en.wikipedia.org/wiki/List_of_large_language_models"
			target="_blank"
			rel="noopener noreferrer">Click here for source data</a
		> · Last Update: Aug 22, 2026
	</p>

	<!-- Color legend -->
	<div
		style="
    display: flex;
    flex-wrap: wrap;
    gap: {space[3]}px {space[5]}px;
    justify-content: center;
    margin-bottom: {space[6]}px;
  "
	>
		{#each [['OpenAI', colors.indigo], ['Google / DeepMind', colors.cyan], ['Meta', colors.violet], ['Anthropic', '#D97757'], ['Microsoft', colors.amber], ['DeepSeek', colors.pink], ['Mistral', '#fb923c'], ['xAI', '#e879f9'], ['Alibaba', '#e60f4c'], ['Z.ai', '#9D00FF'], ['Moonshot AI', '#0021F3'], ['Nvidia', '#76B900'], ['Other', colors.textSecondary]] as [label, clr] ((label, clr))}
			<span
				style="display:flex; align-items:center; gap:{space[1]}px; font-size:{typography.scale
					.caption}px; color:{colors.textSecondary};"
			>
				<span style="width:10px; height:10px; border-radius:50%; background:{clr}; flex-shrink:0;"
				></span>
				{label}
			</span>
		{/each}
	</div>

	<!-- Arrow + viewport row -->
	<div style="display: flex; align-items: center; gap: {space[3]}px;">
		<!-- Left arrow -->
		<button
			onclick={() => pan(-1)}
			disabled={viewOffset <= 0}
			aria-label="Scroll left"
			style="
        flex-shrink: 0;
        width: 44px;
        height: 56px;
        border-radius: {radius.sm}px;
        border: 1px solid {viewOffset <= 0 ? colors.borderFaint : colors.borderDefault};
        background: {colors.bgSurface};
        color: {viewOffset <= 0 ? colors.textDim : colors.textSecondary};
        font-size: 22px;
        cursor: {viewOffset <= 0 ? 'default' : 'pointer'};
        display: flex;
        align-items: center;
        justify-content: center;
        transition: border-color 0.15s, color 0.15s;
        user-select: none;
      ">‹</button
		>

		<!-- Viewport (no scrollbar) -->
		<div
			bind:clientWidth={containerW}
			bind:this={scrollContainer}
			style="
        flex: 1;
        overflow: hidden;
        border: 1px solid {colors.borderDefault};
        border-radius: {radius.md}px;
        background: {colors.bgSurface};
      "
		>
			<!-- Inner canvas -->
			<div
				style="
      position: relative;
      width: {INNER_W}px;
      height: {INNER_H}px;
      background: {colors.bgSurface};
      transform: translateX(-{viewOffset}px);
      transition: {isAutoScrolling ? 'none' : 'transform 0.38s cubic-bezier(0.4, 0, 0.2, 1)'};
      will-change: transform;
    "
			>
				<!-- Year gridlines + labels -->
				{#each YEARS as yr (yr)}
					{@const xg = dateToX(new Date(yr, 0, 1))}
					<div
						style="
          position: absolute;
          left: {xg}px;
          top: 0;
          bottom: 0;
          width: 1px;
          background: {colors.borderFaint};
          pointer-events: none;
        "
					></div>
					<span
						style="
          position: absolute;
          left: {xg + 4}px;
          bottom: 10px;
          color: {colors.textPrimary};
          font-size: {typography.scale.caption}px;
          font-weight: {typography.weight.medium};
          user-select: none;
          pointer-events: none;
          letter-spacing: {typography.letterSpacing.wide}px;
        ">{yr}</span
					>
				{/each}

				<!-- Axis line -->
				<div
					style="
        position: absolute;
        left: 0;
        right: 0;
        top: {AXIS_Y}px;
        height: 2px;
        background: linear-gradient(to right,
          transparent 0%,
          {colors.borderDefault} 3%,
          {colors.borderDefault} 97%,
          transparent 100%);
        pointer-events: none;
      "
				></div>
				<!-- Day/month tick marks -->
				<svg
					width={INNER_W}
					height={INNER_H}
					style="position: absolute; left: 0; top: 0; pointer-events: none;"
				>
					{#each ticks as t, i (i)}
						{@const len = t.isMonthStart ? MONTH_TICK_LEN : DAY_TICK_LEN}
						<line
							x1={t.x}
							y1={AXIS_Y - len / 2}
							x2={t.x}
							y2={AXIS_Y + len / 2}
							stroke={t.isMonthStart ? colors.indigo : colors.indigo}
							stroke-width={t.isMonthStart ? TICK_STROKE_MONTH : TICK_STROKE_DAY}
						/>
					{/each}
				</svg>
				<!-- Bottom axis line -->
				<div
					style="
        position: absolute;
        left: 0;
        right: 0;
        top: {BOTTOM_AXIS_Y}px;
        height: 2px;
        background: linear-gradient(to right,
          transparent 0%,
          {colors.borderDefault} 3%,
          {colors.borderDefault} 97%,
          transparent 100%);
        pointer-events: none;
      "
				></div>
				<!-- Day/month tick marks — top -->
				<svg
					width={INNER_W}
					height={INNER_H}
					style="position: absolute; left: 0; top: 0; pointer-events: none; z-index: 1;"
				>
					{#each ticks as t, i (i)}
						{@const len = t.isMonthStart ? MONTH_TICK_LEN : DAY_TICK_LEN}
						<line
							x1={t.x}
							y1={AXIS_Y - len / 2}
							x2={t.x}
							y2={AXIS_Y + len / 2}
							stroke={t.isMonthStart ? colors.indigo : colors.indigo}
							stroke-width={t.isMonthStart ? TICK_STROKE_MONTH : TICK_STROKE_DAY}
						/>
					{/each}
				</svg>

				<!-- Day/month tick marks — bottom -->
				<svg
					width={INNER_W}
					height={INNER_H}
					style="position: absolute; left: 0; top: 0; pointer-events: none; z-index: 1;"
				>
					{#each ticks as t, i (i)}
						{@const len = t.isMonthStart ? MONTH_TICK_LEN : DAY_TICK_LEN}
						<line
							x1={t.x}
							y1={BOTTOM_AXIS_Y - len / 2}
							x2={t.x}
							y2={BOTTOM_AXIS_Y + len / 2}
							stroke={t.isMonthStart ? colors.indigo : colors.indigo}
							stroke-width={t.isMonthStart ? TICK_STROKE_MONTH : TICK_STROKE_DAY}
						/>
					{/each}
				</svg>

				<!-- Events -->
				{#each positioned as ev (ev)}
					{@const lane = LANES[ev.lane]}
					{@const cardTop = lane.y}
					{@const isAbove = lane.above}
					{@const connTop = isAbove ? cardTop + CARD_H : AXIS_Y + DOT_D / 2}
					{@const connH = isAbove
						? AXIS_Y - DOT_D / 2 - (cardTop + CARD_H)
						: cardTop - (AXIS_Y + DOT_D / 2)}
					{@const active = hovered === ev}
					{@const cx = ev.x - CARD_W / 2}

					<!-- Connector line -->
					<div
						style="
          position: absolute;
          left: {ev.x - 0.5}px;
          top: {connTop}px;
          width: 1px;
          height: {connH}px;
          background: {ev.color};
          opacity: {active ? 0.7 : 0.25};
          transition: opacity 0.15s;
          pointer-events: none;
        "
					></div>

					<!-- Axis dot -->
					<div
						role="button"
						tabindex="0"
						aria-label={ev.name}
						style="
            position: absolute;
            left: {ev.x - DOT_D / 2}px;
            top: {AXIS_Y - DOT_D / 2}px;
            width: {DOT_D}px;
            height: {DOT_D}px;
            border-radius: {radius.full}px;
            background: {ev.color};
            box-shadow: {active ? shadow.glow(ev.color) : 'none'};
            transition: box-shadow 0.15s;
            cursor: pointer;
            z-index: 2;
          "
						onmouseenter={() => enterEvent(ev)}
						onmouseleave={leaveEvent}
						onkeydown={(e) => {
							if (e.key === 'Enter' && ev.nameLink) window.open(ev.nameLink, '_blank')
						}}
					></div>

					<!-- Card -->
					<div
						role="button"
						tabindex="-1"
						style="
            position: absolute;
            left: {cx}px;
            top: {cardTop}px;
            width: {CARD_W}px;
            height: {CARD_H}px;
            border-radius: {radius.xs}px;
            background: {active ? colors.bgSurface : `rgba(15,23,42,0.85)`};
            border: 1px solid {active ? ev.color : colors.borderSubtle};
            cursor: pointer;
            overflow: hidden;
            padding: 0 {space[2]}px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            box-shadow: {active ? shadow.glowSm(ev.color) : 'none'};
            transition: border-color 0.15s, box-shadow 0.15s;
            z-index: 3;
          "
						onmouseenter={() => enterEvent(ev)}
						onmouseleave={leaveEvent}
						onkeydown={(e) => {
							if (e.key === 'Enter' && ev.nameLink) window.open(ev.nameLink, '_blank')
						}}
					>
						<span
							style="
            color: {ev.color};
            font-size: {typography.scale.label}px;
            font-weight: {typography.weight.bold};
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
            line-height: 1.25;
          ">{ev.name}</span
						>
						<span
							style="
            color: {colors.textDim};
            font-size: {typography.scale.label}px;
            line-height: 1.25;
            margin-top: 2px;
          ">{fmtDate(ev.parsedDate)}</span
						>
					</div>
				{/each}
			</div>
			<!-- end inner canvas -->
		</div>
		<!-- end viewport -->

		<!-- Right arrow -->
		<button
			onclick={() => pan(1)}
			disabled={viewOffset >= maxOffset}
			aria-label="Scroll right"
			style="
        flex-shrink: 0;
        width: 44px;
        height: 56px;
        border-radius: {radius.sm}px;
        border: 1px solid {viewOffset >= maxOffset ? colors.borderFaint : colors.borderDefault};
        background: {colors.bgSurface};
        color: {viewOffset >= maxOffset ? colors.textDim : colors.textSecondary};
        font-size: 22px;
        cursor: {viewOffset >= maxOffset ? 'default' : 'pointer'};
        display: flex;
        align-items: center;
        justify-content: center;
        transition: border-color 0.15s, color 0.15s;
        user-select: none;
      ">›</button
		>
	</div>
	<!-- end arrow+viewport row -->
</section>

<!-- Tooltip (fixed, portal-like) -->
{#if hovered}
	{@const tt = hovered}
	<div
		role="tooltip"
		style="
      position: fixed;
      left: {tipX}px;
      top: {tipY}px;
      width: 300px;
      max-height: 80vh;
      overflow-y: auto;
      background: {colors.bgSurface};
      border: 1px solid {tt.color};
      border-radius: {radius.sm}px;
      padding: {space[4]}px;
      z-index: 9999;
      box-shadow: 0 8px 40px rgba(0,0,0,0.6), {shadow.glowSm(tt.color)};
      font-family: {typography.fontSans};
    "
		onmouseenter={enterTooltip}
		onmouseleave={leaveTooltip}
	>
		<!-- Model name -->
		<div
			style="margin-bottom: {space[3]}px; border-bottom: 1px solid {colors.borderSubtle}; padding-bottom: {space[3]}px;"
		>
			<span
				style="color: {tt.color}; font-size: {typography.scale.ui}px; font-weight: {typography
					.weight.bold}; line-height: {typography.lineHeight.tight};">{tt.name}</span
			>
			<div
				style="color: {colors.textMuted}; font-size: {typography.scale
					.caption}px; margin-top: {space[1]}px;"
			>
				{tt.date}
			</div>
		</div>

		<!-- Detail rows -->
		<div style="display: flex; flex-direction: column; gap: {space[2]}px;">
			<!-- Developer -->
			<div>
				<div
					style="color: {colors.textDim}; font-size: {typography.scale
						.label}px; text-transform: uppercase; letter-spacing: {typography.letterSpacing
						.wider}px; margin-bottom: 2px;"
				>
					Developer
				</div>
				<div style="color: {colors.textSecondary}; font-size: {typography.scale.caption}px;">
					{tt.developer || '—'}
				</div>
			</div>

			<!-- Parameters -->
			<div>
				<div
					style="color: {colors.textDim}; font-size: {typography.scale
						.label}px; text-transform: uppercase; letter-spacing: {typography.letterSpacing
						.wider}px; margin-bottom: 2px;"
				>
					Parameters (billion)
				</div>
				<div style="color: {colors.textSecondary}; font-size: {typography.scale.caption}px;">
					{tt.parameters || '—'}
				</div>
			</div>

			<!-- Corpus -->
			<div>
				<div
					style="color: {colors.textDim}; font-size: {typography.scale
						.label}px; text-transform: uppercase; letter-spacing: {typography.letterSpacing
						.wider}px; margin-bottom: 2px;"
				>
					Corpus Size
				</div>
				<div style="color: {colors.textSecondary}; font-size: {typography.scale.caption}px;">
					{tt.corpus || '—'}
				</div>
			</div>

			<!-- Training cost -->
			<div>
				<div
					style="color: {colors.textDim}; font-size: {typography.scale
						.label}px; text-transform: uppercase; letter-spacing: {typography.letterSpacing
						.wider}px; margin-bottom: 2px;"
				>
					Training Cost (petaFLOP-day)
				</div>
				<div style="color: {colors.textSecondary}; font-size: {typography.scale.caption}px;">
					{tt.cost || '—'}
				</div>
			</div>

			<!-- Notes -->
			{#if tt.notes}
				<div>
					<div
						style="color: {colors.textDim}; font-size: {typography.scale
							.label}px; text-transform: uppercase; letter-spacing: {typography.letterSpacing
							.wider}px; margin-bottom: 2px;"
					>
						Notes
					</div>
					<div
						style="color: {colors.textSecondary}; font-size: {typography.scale
							.caption}px; line-height: {typography.lineHeight.relaxed};"
					>
						{tt.notes}
					</div>
				</div>
			{/if}
		</div>
	</div>
{/if}
