export const colors = {
  bgPage:        "#0f172a",
  bgSurface:     "#1e293b",
  bgSubtle:      "rgba(255,255,255,0.03)",
  borderDefault: "#1e3a5f",
  borderSubtle:  "rgba(255,255,255,0.07)",
  borderFaint:   "rgba(255,255,255,0.04)",
  indigo:        "#818cf8",
  indigoDim:     "#4f46e5",
  cyan:          "#22d3ee",
  violet:        "#a78bfa",
  amber:         "#fbbf24",
  teal:          "#2dd4bf",
  pink:          "#f472b6",
  textPrimary:   "#f1f5f9",
  textSecondary: "#94a3b8",
  textMuted:     "#64748b",
  textDim:       "#475569",
};

export const typography = {
  fontSans: "Inter, system-ui, sans-serif",
  fontMono: "monospace",
  scale: { label:10, caption:12, body:14, ui:16, lead:20, h3:24, h2:32, h1:40 },
  weight: { regular:400, medium:600, bold:700, black:800, heavy:900 },
  lineHeight: { tight:1.15, base:1.4, relaxed:1.6, loose:1.7 },
  letterSpacing: { normal:0, wide:0.5, wider:1, widest:2, uppercase:3 },
};

export const space = { 1:4, 2:8, 3:12, 4:16, 5:20, 6:24, 8:32, 10:40, 12:48, 14:56, 16:64 };

export const radius = { xs:4, sm:8, md:12, full:9999 };

export const shadow = {
  none: "none",
  glow:   (color: string) => `0 0 12px ${color}33`,
  glowSm: (color: string) => `0 0 8px ${color}22`,
};

export const layout = {
  navHeight:            56,
  maxWidth:             800,
  maxWidthWide:         1200,
  contentPaddingTop:    60,
  contentPaddingX:      24,
  contentPaddingXWide:  18,
  contentPaddingBottom: 60,
};
