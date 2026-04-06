# Timeline of LLMs based upon JQuery Timeline widget

# Prompt

```
I have a SvelteKit project. I want a single Timeline.svelte component first, then wire it into a SvelteKit route (+page.svelte).

Build the Timeline.svelte component modeled after jQuery Timeline found in the jquery.timeline-2.1.3 folder.

Use these data found in List_of_LLMs.xlsx.

The timeline should be horizontal, with events showing Name and release date. On hover, show Developer, Number of parameters (billion), Corpus size,  Training Costs and Notes. Keep all hyperlinks.

Title should be "A Timeline of LLMs".
Use the styles found in the ./src/lib/styles directory. 

Stretch the x-axis so that the elements don't overlap and get rid of the scrollbar adding forward and backward arrows in the middle of the left and right hand margins

```

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
