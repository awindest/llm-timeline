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
