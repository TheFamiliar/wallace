# Wallace AA (Standard Variant — Dark -2 Background)

A perceptually uniform color palette designed for software UI theme creation, built using OKLCH color space and with WCAG AA accessibility compliance.

> **Status:** documented variant. The **official Wallace palette is the
> Dark -3 variant** (see `Wallace AA Dark3 Palette.md`), which uses a darker
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
**Foreground & Accent Row:** Light +2 • `oklch(0.7172 0.11 <hue>)` — 4 steps above the background  
**Step Constant:** h = 0.1086 (derived — see `Wallace Palette Derivation.md`)  
**Hue Increments:** 30° intervals  
**Contrast Standard:** WCAG AA (4.5:1 minimum)

The step constant makes contrast a function of step distance alone:
**any text 4 steps above its surface meets AA; 5 steps meets AAA.**
Here the foreground and accents sit 4 steps above Dark -2.

---

## Monochromatic Green Palette

9 shades at uniform h = 0.1086 lightness intervals.  
**Hue:** 150° (Cyan-Green) • **Chroma:** 0.11

Contrast ratios are measured against the Dark -2 background `#00360c`.

### Light +4

* OKLCH: `oklch(0.9344 0.11 150)`
* Hex: `#b4ffc3`
* RGB: `rgb(180, 255, 195)`
* Contrast: 11.76:1 (AA ✓, AAA ✓)

### Light +3

* OKLCH: `oklch(0.8258 0.11 150)`
* Hex: `#91daa0`
* RGB: `rgb(145, 218, 160)`
* Contrast: 8.31:1 (AA ✓, AAA ✓)

### Light +2 — Foreground (= Green accent)

* OKLCH: `oklch(0.7172 0.11 150)`
* Hex: `#6fb77f`
* RGB: `rgb(111, 183, 127)`
* Contrast: 5.71:1 (AA ✓)

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

## Chromatic Palette (AA Standard)

12 chromatic colors at Light +2 (`oklch(0.7172 0.11 <hue>)`) displayed on Dark -2 background.  
**30° hue increments • Perceptually uniform spacing**

On this higher-luminance pairing all 12 hues pass AA, including Red and
Orange — they are nonetheless **excluded from all themes** (see Canonical
Theme Palette in the Dark -3 documents).

### Red — excluded from canonical theme palette

* OKLCH: `oklch(0.7172 0.11 0)`
* Hue: 0°
* Hex: `#dc86a1`
* RGB: `rgb(220, 134, 161)`
* Contrast: 5.20:1 • AA Status: ✓ Pass

### Orange — excluded from canonical theme palette

* OKLCH: `oklch(0.7172 0.11 30)`
* Hue: 30°
* Hex: `#e0897a`
* RGB: `rgb(224, 137, 122)`
* Contrast: 5.24:1 • AA Status: ✓ Pass

### Yellow-Orange

* OKLCH: `oklch(0.7172 0.11 60)`
* Hue: 60°
* Hex: `#d69359`
* RGB: `rgb(214, 147, 89)`
* Contrast: 5.33:1 • AA Status: ✓ Pass

### Yellow

* OKLCH: `oklch(0.7172 0.11 90)`
* Hue: 90°
* Hex: `#bea04b`
* RGB: `rgb(190, 160, 75)`
* Contrast: 5.43:1 • AA Status: ✓ Pass

### Yellow-Green

* OKLCH: `oklch(0.7172 0.11 120)`
* Hue: 120°
* Hex: `#9bae5c`
* RGB: `rgb(155, 174, 92)`
* Contrast: 5.61:1 • AA Status: ✓ Pass

### Green (= Light +2)

* OKLCH: `oklch(0.7172 0.11 150)`
* Hue: 150°
* Hex: `#6fb77f`
* RGB: `rgb(111, 183, 127)`
* Contrast: 5.71:1 • AA Status: ✓ Pass
* Identical to the ramp's Light +2 / theme foreground by construction.

### Cyan

* OKLCH: `oklch(0.7172 0.11 180)`
* Hue: 180°
* Hex: `#42baa6`
* RGB: `rgb(66, 186, 166)`
* Contrast: 5.74:1 • AA Status: ✓ Pass

### Blue-Cyan

* OKLCH: `oklch(0.7172 0.11 210)`
* Hue: 210°
* Hex: `#37b6ca`
* RGB: `rgb(55, 182, 202)`
* Contrast: 5.68:1 • AA Status: ✓ Pass

### Blue

* OKLCH: `oklch(0.7172 0.11 240)`
* Hue: 240°
* Hex: `#5dade2`
* RGB: `rgb(93, 173, 226)`
* Contrast: 5.57:1 • AA Status: ✓ Pass

### Blue-Violet

* OKLCH: `oklch(0.7172 0.11 270)`
* Hue: 270°
* Hex: `#89a0e9`
* RGB: `rgb(137, 160, 233)`
* Contrast: 5.39:1 • AA Status: ✓ Pass

### Violet

* OKLCH: `oklch(0.7172 0.11 300)`
* Hue: 300°
* Hex: `#ae94de`
* RGB: `rgb(174, 148, 222)`
* Contrast: 5.28:1 • AA Status: ✓ Pass

### Magenta

* OKLCH: `oklch(0.7172 0.11 330)`
* Hue: 330°
* Hex: `#cb8ac5`
* RGB: `rgb(203, 138, 197)`
* Contrast: 5.21:1 • AA Status: ✓ Pass

---

## Achromatic Color

### Grey

* OKLCH: `oklch(0.7172 0 0)`
* Hex: `#a4a4a4`
* RGB: `rgb(164, 164, 164)`
* Contrast: 5.50:1 • AA Status: ✓ Pass

---

## Technical Details

**Color Space:** OKLCH (Oklab cylindrical representation)  
**Lightness Range:** 0.0656 to 0.9344 (Base ± 4h)  
**Interval System:** h = 0.1086, derived (see `Wallace Palette Derivation.md`)  
**Base Lightness:** L=0.50 (mathematical and perceptual midpoint — the origin green)  
**WCAG Compliance:** All text colors meet AA standard (4.5:1 minimum contrast ratio) against Dark -2  
**Contrast Ratio:** Light +2 on Dark -2 = 5.71:1

Contrast ratios computed per WCAG 2.x relative luminance from the sRGB hex
values (gamut-fitted with coloraide where OKLCH falls outside sRGB).

Perceptually uniform in OKLCH color space, ensuring consistent visual relationships across all colors and shades. Every chromatic accent shares its perceptual lightness with a named green step, so each colour appears equally bright.
