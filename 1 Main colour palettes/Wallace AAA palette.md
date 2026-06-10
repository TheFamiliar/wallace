# Wallace AAA (Standard Variant — Dark -2 Background)

A perceptually uniform color palette designed for software UI theme creation, built using OKLCH color space and with WCAG AAA accessibility compliance.

> **Status:** documented variant. The **official Wallace palette is the
> Dark -3 variant** (see `Wallace AAA Dark3 Palette.md`), which uses a darker
> background and lower-luminance accents for reduced eye strain. This
> variant keeps the same derived ramp with a higher-luminance pairing:
> background Dark -2, text and accents one ramp step brighter.

## License
This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at http://mozilla.org/MPL/2.0/.

## Theme Specifications

**Origin:** Base • `oklch(0.5 0.11 150)` • `#2b7440`  
**Background:** Dark -2 • `oklch(0.2828 0.11 150)` • `#00360c`  
**Foreground & Accent Row:** Light +3 • `oklch(0.8258 0.11 <hue>)` — 5 steps above the background  
**Step Constant:** h = 0.1086 (derived — see `Wallace Palette Derivation.md`)  
**Hue Increments:** 30° intervals  
**Contrast Standard:** WCAG AAA (7.0:1 minimum)

The step constant makes contrast a function of step distance alone:
**any text 4 steps above its surface meets AA; 5 steps meets AAA.**
Here the foreground and accents sit 5 steps above Dark -2.

---

## Monochromatic Green Palette

9 shades at uniform h = 0.1086 lightness intervals.  
**Hue:** 150° (Cyan-Green) • **Chroma:** 0.11

Contrast ratios are measured against the Dark -2 background `#00360c`.

### Light +4

* OKLCH: `oklch(0.9344 0.11 150)`
* Hex: `#b4ffc3`
* RGB: `rgb(180, 255, 195)`
* Contrast: 11.76:1 (AAA ✓)

### Light +3 — Foreground (= Green accent)

* OKLCH: `oklch(0.8258 0.11 150)`
* Hex: `#91daa0`
* RGB: `rgb(145, 218, 160)`
* Contrast: 8.31:1 (AAA ✓)

### Light +2

* OKLCH: `oklch(0.7172 0.11 150)`
* Hex: `#6fb77f`
* RGB: `rgb(111, 183, 127)`
* Contrast: 5.71:1 — AA only; not for AAA body text on Dark -2

### Light +1

* OKLCH: `oklch(0.6086 0.11 150)`
* Hex: `#4d955f`
* RGB: `rgb(77, 149, 95)`
* Contrast: 3.77:1 — not for body text on Dark -2

### Base — Origin

* OKLCH: `oklch(0.50 0.11 150)`
* Hex: `#2b7440`
* RGB: `rgb(43, 116, 64)`
* Contrast: 2.40:1 — UI accents and large text only

### Dark -1

* OKLCH: `oklch(0.3914 0.11 150)`
* Hex: `#005522`
* RGB: `rgb(0, 85, 34)`
* Non-text role: selections, borders, quote backgrounds

### Dark -2 — Background

* OKLCH: `oklch(0.2828 0.11 150)`
* Hex: `#00360c`
* RGB: `rgb(0, 54, 12)`

### Dark -3

* OKLCH: `oklch(0.1742 0.11 150)`
* Hex: `#001901`
* RGB: `rgb(0, 25, 1)`
* Non-text role: recessed surfaces, code-block backgrounds

### Dark -4

* OKLCH: `oklch(0.0656 0.11 150)`
* Hex: `#000300`
* RGB: `rgb(0, 3, 0)`
* Non-text role: deepest recesses, shadows

---

## Chromatic Palette (AAA Standard)

12 chromatic colors at Light +3 (`oklch(0.8258 0.11 <hue>)`) displayed on Dark -2 background.  
**30° hue increments • Perceptually uniform spacing**

On this higher-luminance pairing all 12 hues pass AAA, including Red and
Orange — they are nonetheless **excluded from all themes** (see Canonical
Theme Palette in the Dark -3 documents).

### Red — excluded from canonical theme palette

* OKLCH: `oklch(0.8258 0.11 0)`
* Hue: 0°
* Hex: `#ffa8c3`
* RGB: `rgb(255, 168, 195)`
* Contrast: 7.59:1 • AAA Status: ✓ Pass

### Orange — excluded from canonical theme palette

* OKLCH: `oklch(0.8258 0.11 30)`
* Hue: 30°
* Hex: `#ffab9b`
* RGB: `rgb(255, 171, 155)`
* Contrast: 7.53:1 • AAA Status: ✓ Pass

### Yellow-Orange

* OKLCH: `oklch(0.8258 0.11 60)`
* Hue: 60°
* Hex: `#fbb57b`
* RGB: `rgb(251, 181, 123)`
* Contrast: 7.83:1 • AAA Status: ✓ Pass

### Yellow

* OKLCH: `oklch(0.8258 0.11 90)`
* Hue: 90°
* Hex: `#e2c36e`
* RGB: `rgb(226, 195, 110)`
* Contrast: 8.00:1 • AAA Status: ✓ Pass

### Yellow-Green

* OKLCH: `oklch(0.8258 0.11 120)`
* Hue: 120°
* Hex: `#bdd17e`
* RGB: `rgb(189, 209, 126)`
* Contrast: 8.21:1 • AAA Status: ✓ Pass

### Green (= Light +3)

* OKLCH: `oklch(0.8258 0.11 150)`
* Hue: 150°
* Hex: `#91daa0`
* RGB: `rgb(145, 218, 160)`
* Contrast: 8.31:1 • AAA Status: ✓ Pass
* Identical to the ramp's Light +3 / theme foreground by construction.

### Cyan

* OKLCH: `oklch(0.8258 0.11 180)`
* Hue: 180°
* Hex: `#6addc9`
* RGB: `rgb(106, 221, 201)`
* Contrast: 8.35:1 • AAA Status: ✓ Pass

### Blue-Cyan

* OKLCH: `oklch(0.8258 0.11 210)`
* Hue: 210°
* Hex: `#62d9ed`
* RGB: `rgb(98, 217, 237)`
* Contrast: 8.26:1 • AAA Status: ✓ Pass

### Blue

* OKLCH: `oklch(0.8258 0.11 240)`
* Hue: 240°
* Hex: `#80d0ff`
* RGB: `rgb(128, 208, 255)`
* Contrast: 8.08:1 • AAA Status: ✓ Pass

### Blue-Violet

* OKLCH: `oklch(0.8258 0.11 270)`
* Hue: 270°
* Hex: `#aac3ff`
* RGB: `rgb(170, 195, 255)`
* Contrast: 7.80:1 • AAA Status: ✓ Pass

### Violet

* OKLCH: `oklch(0.8258 0.11 300)`
* Hue: 300°
* Hex: `#d1b6ff`
* RGB: `rgb(209, 182, 255)`
* Contrast: 7.73:1 • AAA Status: ✓ Pass

### Magenta

* OKLCH: `oklch(0.8258 0.11 330)`
* Hue: 330°
* Hex: `#eface8`
* RGB: `rgb(239, 172, 232)`
* Contrast: 7.66:1 • AAA Status: ✓ Pass

---

## Achromatic Color

### Grey

* OKLCH: `oklch(0.8258 0 0)`
* Hex: `#c6c6c6`
* RGB: `rgb(198, 198, 198)`
* Contrast: 8.02:1 • AAA Status: ✓ Pass

---

## Technical Details

**Color Space:** OKLCH (Oklab cylindrical representation)  
**Lightness Range:** 0.0656 to 0.9344 (Base ± 4h)  
**Interval System:** h = 0.1086, derived (see `Wallace Palette Derivation.md`)  
**Base Lightness:** L=0.50 (mathematical and perceptual midpoint — the origin green)  
**WCAG Compliance:** All text colors meet AAA standard (7.0:1 minimum contrast ratio) against Dark -2  
**Contrast Ratio:** Light +3 on Dark -2 = 8.31:1

Contrast ratios computed per WCAG 2.x relative luminance from the sRGB hex
values (gamut-fitted with coloraide where OKLCH falls outside sRGB).

Perceptually uniform in OKLCH color space, ensuring consistent visual relationships across all colors and shades. Every chromatic accent shares its perceptual lightness with a named green step, so each colour appears equally bright.
