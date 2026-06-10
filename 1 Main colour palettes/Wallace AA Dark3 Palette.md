# Wallace AA (Dark -3 Variant) — Official Palette

A perceptually uniform color palette designed for software UI theme creation, built using OKLCH color space and with WCAG AA accessibility compliance.

## License
This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at http://mozilla.org/MPL/2.0/.

## Theme Specifications

**Origin:** Base • `oklch(0.5 0.11 150)` • `#2b7440`  
**Background:** Dark -3 • `oklch(0.1742 0.11 150)` • `#001901`  
**Foreground & Accent Row:** Light +1 • `oklch(0.6086 0.11 <hue>)`  
**Step Constant:** h = 0.1086 (derived — see below)  
**Hue Increments:** 30° intervals  
**Contrast Standard:** WCAG AA (4.5:1 minimum)

## How the palette is derived

Everything is generated from the origin green and one derived constant:

1. **Origin:** `oklch(0.5 0.11 150)` — the muted forest green at the
   perceptual midpoint. This is the palette's Base, and it never moves.
2. **Step constant h = 0.1086:** the smallest perceptually uniform
   lightness interval such that *five steps above the background, every
   hue of the chromatic wheel reaches AAA contrast (7:1)*. The worst hue
   (Magenta, 330°) lands on exactly 7.00:1. The same constant gives AA
   for free: *four steps* up, every hue passes 4.5:1 (worst: 4.57:1).
3. **Green ramp:** Base ± k·h for k = 1…4, giving 9 steps from
   Dark -4 to Light +4.
4. **Chromatic accents:** the hue wheel rotated at the lightness of a
   named green step — Light +1 for AA, Light +2 for AAA — so every accent
   shares its perceptual brightness with a green in the ramp. WCAG
   luminance varies by hue at fixed OKLCH lightness, which is why the
   step constant is solved against the worst hue rather than green.

Because the chromatic rows sit *on* ramp steps, the green↔chromatic
relationship is exact and reversible: accent = `oklch(L(step) 0.11 hue)`.

---

## Canonical Theme Palette

The canonical palette used to build Wallace themes is:

* The 9-shade monochromatic green ramp (backgrounds, foreground text, UI chrome)
* 10 chromatic accents: **Yellow-Orange through Magenta** (hues 60°–330°)
* Grey (achromatic, punctuation/operators)

**Red (0°) and Orange (30°) are excluded from all themes.** Psychology
research indicates red hues increase speed of brain function but reduce
cognitive ability and capacity for creativity. They remain documented below
for completeness. An audit of the version 1 VS Code theme showed 9 accent
colours + grey in active use, so the canonical set covers every syntax role
with headroom.

**The Green accent (150°) is the same colour as the ramp's Light +1** —
by construction, since the accent row lives at Light +1's lightness. Both
are documented so the relationship can be reverse-engineered, and so that
either naming scheme (`--green-l1` in ramp contexts, `--green` in chromatic
contexts) resolves to the same value. Adjacent accents are uniformly spaced
(ΔE-OK ≈ 0.057 between neighbours at 30° intervals).

---

## Monochromatic Green Palette

9 shades at uniform h = 0.1086 lightness intervals.  
**Hue:** 150° (Cyan-Green) • **Chroma:** 0.11

Contrast ratios are measured against the Dark -3 background `#001901`.

### Light +4

* OKLCH: `oklch(0.9344 0.11 150)`
* Hex: `#b4ffc3`
* RGB: `rgb(180, 255, 195)`
* Contrast: 15.82:1 (AA ✓, AAA ✓)

### Light +3

* OKLCH: `oklch(0.8258 0.11 150)`
* Hex: `#91daa0`
* RGB: `rgb(145, 218, 160)`
* Contrast: 11.18:1 (AA ✓, AAA ✓)

### Light +2

* OKLCH: `oklch(0.7172 0.11 150)`
* Hex: `#6fb77f`
* RGB: `rgb(111, 183, 127)`
* Contrast: 7.68:1 (AA ✓, AAA ✓)

### Light +1 — Foreground (= Green accent)

* OKLCH: `oklch(0.6086 0.11 150)`
* Hex: `#4d955f`
* RGB: `rgb(77, 149, 95)`
* Contrast: 5.07:1 (AA ✓)

### Base — Origin

* OKLCH: `oklch(0.50 0.11 150)`
* Hex: `#2b7440`
* RGB: `rgb(43, 116, 64)`
* Contrast: 3.23:1 — not for body text; UI accents and large text only

### Dark -1

* OKLCH: `oklch(0.3914 0.11 150)`
* Hex: `#005522`
* RGB: `rgb(0, 85, 34)`
* Non-text role: selections, borders, quote backgrounds

### Dark -2

* OKLCH: `oklch(0.2828 0.11 150)`
* Hex: `#00360c`
* RGB: `rgb(0, 54, 12)`
* Non-text role: raised surfaces, line highlight

### Dark -3 — Background

* OKLCH: `oklch(0.1742 0.11 150)`
* Hex: `#001901`
* RGB: `rgb(0, 25, 1)`

### Dark -4

* OKLCH: `oklch(0.0656 0.11 150)`
* Hex: `#000300`
* RGB: `rgb(0, 3, 0)`
* Non-text role: recessed surfaces, code-block backgrounds, shadows

---

## Chromatic Palette (AA Standard)

12 chromatic colors at Light +1 (`oklch(0.6086 0.11 <hue>)`) displayed on Dark -3 background.  
**30° hue increments • Perceptually uniform spacing**

### Red — excluded from canonical theme palette

* OKLCH: `oklch(0.6086 0.11 0)`
* Hue: 0°
* Hex: `#b86580`
* RGB: `rgb(184, 101, 128)`
* Contrast: 4.57:1 • AA Status: ✓ Pass

### Orange — excluded from canonical theme palette

* OKLCH: `oklch(0.6086 0.11 30)`
* Hue: 30°
* Hex: `#bc685b`
* RGB: `rgb(188, 104, 91)`
* Contrast: 4.62:1 • AA Status: ✓ Pass

### Yellow-Orange

* OKLCH: `oklch(0.6086 0.11 60)`
* Hue: 60°
* Hex: `#b27238`
* RGB: `rgb(178, 114, 56)`
* Contrast: 4.70:1 • AA Status: ✓ Pass

### Yellow

* OKLCH: `oklch(0.6086 0.11 90)`
* Hue: 90°
* Hex: `#9c7f26`
* RGB: `rgb(156, 127, 38)`
* Contrast: 4.81:1 • AA Status: ✓ Pass

### Yellow-Green

* OKLCH: `oklch(0.6086 0.11 120)`
* Hue: 120°
* Hex: `#7a8c3a`
* RGB: `rgb(122, 140, 58)`
* Contrast: 4.95:1 • AA Status: ✓ Pass

### Green (= Light +1)

* OKLCH: `oklch(0.6086 0.11 150)`
* Hue: 150°
* Hex: `#4d955f`
* RGB: `rgb(77, 149, 95)`
* Contrast: 5.07:1 • AA Status: ✓ Pass
* Identical to the ramp's Light +1 / theme foreground by construction.

### Cyan

* OKLCH: `oklch(0.6086 0.11 180)`
* Hue: 180°
* Hex: `#039885`
* RGB: `rgb(3, 152, 133)`
* Contrast: 5.12:1 • AA Status: ✓ Pass

### Blue-Cyan

* OKLCH: `oklch(0.6086 0.11 210)`
* Hue: 210°
* Hex: `#0094a7`
* RGB: `rgb(0, 148, 167)`
* Contrast: 5.08:1 • AA Status: ✓ Pass

### Blue

* OKLCH: `oklch(0.6086 0.11 240)`
* Hue: 240°
* Hex: `#3a8bbe`
* RGB: `rgb(58, 139, 190)`
* Contrast: 4.93:1 • AA Status: ✓ Pass

### Blue-Violet

* OKLCH: `oklch(0.6086 0.11 270)`
* Hue: 270°
* Hex: `#697fc5`
* RGB: `rgb(105, 127, 197)`
* Contrast: 4.78:1 • AA Status: ✓ Pass

### Violet

* OKLCH: `oklch(0.6086 0.11 300)`
* Hue: 300°
* Hex: `#8d73bb`
* RGB: `rgb(141, 115, 187)`
* Contrast: 4.65:1 • AA Status: ✓ Pass

### Magenta

* OKLCH: `oklch(0.6086 0.11 330)`
* Hue: 330°
* Hex: `#a869a2`
* RGB: `rgb(168, 105, 162)`
* Contrast: 4.57:1 • AA Status: ✓ Pass

---

## Achromatic Color

### Grey

* OKLCH: `oklch(0.6086 0 0)`
* Hex: `#838383`
* RGB: `rgb(131, 131, 131)`
* Contrast: 4.86:1 • AA Status: ✓ Pass

---

## Technical Details

**Color Space:** OKLCH (Oklab cylindrical representation)  
**Lightness Range:** 0.0656 to 0.9344 (Base ± 4h)  
**Interval System:** h = 0.1086, derived from the AAA constraint (see "How the palette is derived")  
**Base Lightness:** L=0.50 (mathematical and perceptual midpoint — the origin green)  
**WCAG Compliance:** All text colors meet AA standard (4.5:1 minimum contrast ratio) against Dark -3  
**Contrast Ratio:** Light +1 on Dark -3 = 5.07:1

Contrast ratios computed per WCAG 2.x relative luminance from the sRGB hex
values (gamut-fitted with coloraide where OKLCH falls outside sRGB — the
dark ramp steps clip; all Light steps and accents are in gamut).

Perceptually uniform in OKLCH color space, ensuring consistent visual relationships across all colors and shades. Every chromatic accent shares its perceptual lightness with a named green step, so each colour appears equally bright. This variant uses a darker background (Dark -3) with lower brightness foreground colors, providing reduced overall luminance while maintaining AA accessibility compliance. Ideal for users with photophobia or light sensitivity.
