# Wallace AAA (Dark -3 Variant) — Official Palette

A perceptually uniform color palette designed for software UI theme creation, built using OKLCH color space and with WCAG AAA accessibility compliance.

## License
This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at http://mozilla.org/MPL/2.0/.

## Theme Specifications

**Origin:** Base • `oklch(0.5 0.11 150)` • `#2b7440`  
**Background:** Dark -3 • `oklch(0.1742 0.11 150)` • `#001901`  
**Foreground & Accent Row:** Light +2 • `oklch(0.7172 0.11 <hue>)`  
**Step Constant:** h = 0.1086 (derived — see below)  
**Hue Increments:** 30° intervals  
**Contrast Standard:** WCAG AAA (7.0:1 minimum)

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
for completeness — note that Red does not reach AAA at Light +2 (6.99:1),
which is moot for themes since it is excluded anyway. An audit of the
version 1 VS Code theme showed 9 accent colours + grey in active use, so
the canonical set covers every syntax role with headroom.

**The Green accent (150°) is the same colour as the ramp's Light +2** —
by construction, since the accent row lives at Light +2's lightness. Both
are documented so the relationship can be reverse-engineered, and so that
either naming scheme (`--green-l2` in ramp contexts, `--green` in chromatic
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
* Contrast: 15.82:1 (AAA ✓)

### Light +3

* OKLCH: `oklch(0.8258 0.11 150)`
* Hex: `#91daa0`
* RGB: `rgb(145, 218, 160)`
* Contrast: 11.18:1 (AAA ✓)

### Light +2 — Foreground (= Green accent)

* OKLCH: `oklch(0.7172 0.11 150)`
* Hex: `#6fb77f`
* RGB: `rgb(111, 183, 127)`
* Contrast: 7.68:1 (AAA ✓)

### Light +1

* OKLCH: `oklch(0.6086 0.11 150)`
* Hex: `#4d955f`
* RGB: `rgb(77, 149, 95)`
* Contrast: 5.07:1 — AA only; not for AAA body text

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

## Chromatic Palette (AAA Standard)

12 chromatic colors at Light +2 (`oklch(0.7172 0.11 <hue>)`) displayed on Dark -3 background.  
**30° hue increments • Perceptually uniform spacing**

### Red — excluded from canonical theme palette

* OKLCH: `oklch(0.7172 0.11 0)`
* Hue: 0°
* Hex: `#dc86a1`
* RGB: `rgb(220, 134, 161)`
* Contrast: 6.99:1 • AAA Status: ✗ Fail (excluded from themes regardless)

### Orange — excluded from canonical theme palette

* OKLCH: `oklch(0.7172 0.11 30)`
* Hue: 30°
* Hex: `#e0897a`
* RGB: `rgb(224, 137, 122)`
* Contrast: 7.05:1 • AAA Status: ✓ Pass

### Yellow-Orange

* OKLCH: `oklch(0.7172 0.11 60)`
* Hue: 60°
* Hex: `#d69359`
* RGB: `rgb(214, 147, 89)`
* Contrast: 7.18:1 • AAA Status: ✓ Pass

### Yellow

* OKLCH: `oklch(0.7172 0.11 90)`
* Hue: 90°
* Hex: `#bea04b`
* RGB: `rgb(190, 160, 75)`
* Contrast: 7.30:1 • AAA Status: ✓ Pass

### Yellow-Green

* OKLCH: `oklch(0.7172 0.11 120)`
* Hue: 120°
* Hex: `#9bae5c`
* RGB: `rgb(155, 174, 92)`
* Contrast: 7.55:1 • AAA Status: ✓ Pass

### Green (= Light +2)

* OKLCH: `oklch(0.7172 0.11 150)`
* Hue: 150°
* Hex: `#6fb77f`
* RGB: `rgb(111, 183, 127)`
* Contrast: 7.68:1 • AAA Status: ✓ Pass
* Identical to the ramp's Light +2 / theme foreground by construction.

### Cyan

* OKLCH: `oklch(0.7172 0.11 180)`
* Hue: 180°
* Hex: `#42baa6`
* RGB: `rgb(66, 186, 166)`
* Contrast: 7.73:1 • AAA Status: ✓ Pass

### Blue-Cyan

* OKLCH: `oklch(0.7172 0.11 210)`
* Hue: 210°
* Hex: `#37b6ca`
* RGB: `rgb(55, 182, 202)`
* Contrast: 7.64:1 • AAA Status: ✓ Pass

### Blue

* OKLCH: `oklch(0.7172 0.11 240)`
* Hue: 240°
* Hex: `#5dade2`
* RGB: `rgb(93, 173, 226)`
* Contrast: 7.50:1 • AAA Status: ✓ Pass

### Blue-Violet

* OKLCH: `oklch(0.7172 0.11 270)`
* Hue: 270°
* Hex: `#89a0e9`
* RGB: `rgb(137, 160, 233)`
* Contrast: 7.26:1 • AAA Status: ✓ Pass

### Violet

* OKLCH: `oklch(0.7172 0.11 300)`
* Hue: 300°
* Hex: `#ae94de`
* RGB: `rgb(174, 148, 222)`
* Contrast: 7.10:1 • AAA Status: ✓ Pass

### Magenta

* OKLCH: `oklch(0.7172 0.11 330)`
* Hue: 330°
* Hex: `#cb8ac5`
* RGB: `rgb(203, 138, 197)`
* Contrast: 7.00:1 • AAA Status: ✓ Pass (the binding constraint — exactly 7.00)

---

## Achromatic Color

### Grey

* OKLCH: `oklch(0.7172 0 0)`
* Hex: `#a4a4a4`
* RGB: `rgb(164, 164, 164)`
* Contrast: 7.39:1 • AAA Status: ✓ Pass

---

## Technical Details

**Color Space:** OKLCH (Oklab cylindrical representation)  
**Lightness Range:** 0.0656 to 0.9344 (Base ± 4h)  
**Interval System:** h = 0.1086, derived from the AAA constraint (see "How the palette is derived")  
**Base Lightness:** L=0.50 (mathematical and perceptual midpoint — the origin green)  
**WCAG Compliance:** All canonical text colors meet AAA standard (7.0:1 minimum contrast ratio) against Dark -3  
**Contrast Ratio:** Light +2 on Dark -3 = 7.68:1

Contrast ratios computed per WCAG 2.x relative luminance from the sRGB hex
values (gamut-fitted with coloraide where OKLCH falls outside sRGB — the
dark ramp steps clip; all Light steps and accents are in gamut).

Perceptually uniform in OKLCH color space, ensuring consistent visual relationships across all colors and shades. Every chromatic accent shares its perceptual lightness with a named green step, so each colour appears equally bright. This variant uses a darker background (Dark -3) with moderate brightness foreground colors, achieving AAA accessibility compliance with low overall luminance. Provides excellent accessibility while being comfortable for extended use.
