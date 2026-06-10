# Wallace Palette Derivation

How every Wallace colour is generated from one green and one number.

This document is the canonical record of the palette's construction. With
it, the entire system can be reproduced — or reverse-engineered — from
first principles.

## License
This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at http://mozilla.org/MPL/2.0/.

---

## 1. The origin green

Everything begins with a single muted forest green at the perceptual
midpoint of the lightness scale:

```
Base = oklch(0.5 0.11 150) = #2b7440
```

The choice is informed by psychology research:

1. Green hues tend to boost creativity and aid completion of creative tasks.
2. Red hues tend to increase speed of brain function but reduce cognitive
   ability — which is also why red and orange are excluded from the
   canonical theme palette (§6).

The three numbers are the palette's genome:

* **L = 0.5** — the exact midpoint of OKLCH lightness, so the ramp can
  extend symmetrically in both directions.
* **C = 0.11** — a muted chroma: saturated enough to read as colour,
  desaturated enough for long sessions. Every colour in the system shares
  it (grey, at C = 0, is the one deliberate exception).
* **H = 150°** — the cyan-green hue of the origin.

## 2. Why OKLCH

OKLCH is a perceptually uniform colour space: equal numeric intervals
produce equal *visual* differences. That buys two guarantees the palette
is built on:

* Equal lightness steps in the green ramp **look** like equal steps.
* Colours that share an L value **appear equally bright**, whatever their
  hue — the property Solarized achieved with CIELAB; OKLCH is its modern,
  more accurate successor.

All definitions and operations happen in OKLCH. Conversion to sRGB hex is
the *last* step, and only because most destination applications don't
accept `oklch()` yet. Where an OKLCH colour falls outside the sRGB gamut
(this happens only for the dark ramp steps, where the green hue can't
reach C = 0.11 at very low lightness), it is gamut-fitted with coloraide's
`fit("srgb")`.

## 3. The monochromatic ramp and the step constant *h*

The green ramp is nine steps centred on the origin:

```
L(k) = 0.5 + k·h        for k = −4 … +4
       Dark −4 … Base … Light +4
```

One number remains to be chosen: the step constant **h**.

### The constraint that determines h

WCAG contrast is computed from *physical* luminance (Y), not perceptual
lightness. At a fixed OKLCH lightness, luminance still varies by hue —
green is luminous, magenta and red are not. So if the chromatic palette
(§5) is to sit *on* a ramp step and still meet a contrast standard, the
step constant must be solved against the **worst hue of the wheel**, not
against green:

> **h is the smallest perceptually uniform lightness interval such that,
> five steps above the background, every hue of the chromatic wheel
> reaches AAA contrast (7.0:1).**

Solving numerically (bisection over h, testing all twelve 30° hues plus
grey at C = 0 against the Dark −3 background):

```
h = 0.1086
```

The binding hue is **Magenta (330°)**, which lands on exactly **7.00:1**.
And the same constant delivers AA for free: *four* steps above the
background, every hue passes 4.5:1 (worst: Magenta again, 4.57:1).

### The step-distance rule

Because h was solved against the worst hue, contrast collapses to a
function of step distance alone:

| Steps between text and surface | Standard met | Worst case measured |
|---|---|---|
| 4 | **AA** (≥ 4.5:1) | 4.57:1 on Dark −3 · 5.20:1 on Dark −2 |
| 5 | **AAA** (≥ 7.0:1) | 7.00:1 on Dark −3 · 7.53:1 on Dark −2 |

Verified on both background anchors the project uses. This is the rule of
thumb for theme building: put body text and accents 4 steps above their
surface for AA, 5 for AAA. (The rule is exact at the official Dark −3
anchor and gains margin on lighter backgrounds in this range.)

### The musical analogy

There genuinely is one — two, in fact, and the palette had to choose:

* **Equal temperament in *perception*** (chosen): uniform OKLCH steps are
  the visual analogue of equal semitones — every interval *sounds* (looks)
  the same size. h is the palette's semitone; AA is a fourth (4 steps),
  AAA a fifth (5 steps).
* **Equal temperament in *contrast*** (rejected): a ladder geometric in
  (Y + 0.05) would make every adjacent pair have the *same contrast
  ratio*, and contrast between any two steps would depend only on their
  distance — mathematically lovely. But it was rejected on two grounds:
  the required per-step ratio (≈1.50) compounds to ≈26:1 over the ramp's
  eight intervals, overflowing sRGB's maximum possible ~21:1 against a
  near-black anchor; and geometric luminance steps are *not* perceptually
  even, violating the palette's uniformity aim.

The chosen design recovers the best property of the rejected one — the
step-distance rule above — while keeping perceptual uniformity, because
the rule only needs to hold at the distances actually used (4 and 5).

### The resulting ramp

| Step | L | Hex | Notes |
|---|---|---|---|
| Light +4 | 0.9344 | `#b4ffc3` | brightest; cursor, highlights |
| Light +3 | 0.8258 | `#91daa0` | bold/strong text; AAA fg on Dark −2 |
| Light +2 | 0.7172 | `#6fb77f` | **AAA foreground** (official, Dark −3) |
| Light +1 | 0.6086 | `#4d955f` | **AA foreground** (official, Dark −3) |
| Base | 0.5000 | `#2b7440` | **origin** — never moves |
| Dark −1 | 0.3914 | `#005522` | selections, borders |
| Dark −2 | 0.2828 | `#00360c` | raised surfaces; variant background |
| Dark −3 | 0.1742 | `#001901` | **official background** |
| Dark −4 | 0.0656 | `#000300` | recessed surfaces, code blocks |

## 4. From ramp to chromatic palette

The chromatic palette is the hue wheel rotated about a ramp step:

```
accent(hue) = oklch(L(step) 0.11 hue)      hue = 0°, 30°, … 330°
```

The lightness is *inherited from the ramp*, never invented. Each standard
uses the step at the right distance from its background:

| Variant | Background | Foreground & accent row | Steps |
|---|---|---|---|
| **AA official** | Dark −3 | Light +1 (L 0.6086) | 4 |
| **AAA official** | Dark −3 | Light +2 (L 0.7172) | 5 |
| AA standard variant | Dark −2 | Light +2 (L 0.7172) | 4 |
| AAA standard variant | Dark −2 | Light +3 (L 0.8258) | 5 |

Because every accent shares its L with a green step, each accent has the
same perceived brightness as its row-mates *and* as that green. The
**Green accent (150°) is therefore literally the same colour as its ramp
step** — the two palettes (monochromatic and chromatic) intersect there.
Both names are kept so the relationship stays visible and variable naming
can be consistent in either context (`--green-l1` ≡ `--green` in the AA
row, `--green-l2` ≡ `--green` in the AAA row).

**Grey** is the same construction at zero chroma: `oklch(L(step) 0 0)`.

Adjacent accents are uniformly spaced perceptually — ΔE-OK ≈ 0.057
between every neighbouring pair, a direct consequence of equal hue
spacing at shared L and C.

## 5. Verification

Compliance is never assumed from the construction — it is measured on the
final sRGB hex values per WCAG 2.x relative luminance:

```
Y = 0.2126·R' + 0.7152·G' + 0.0722·B'     (R',G',B' linearised sRGB)
contrast = (Y_lighter + 0.05) / (Y_darker + 0.05)
```

Measured results for the official (Dark −3) palette: AA row 4.57–5.12:1
(all ≥ 4.5), AAA row 7.00–7.73:1 (all ≥ 7.0), grey 4.86 / 7.39. Full
per-colour figures are in the four palette documents.

One honest footnote: at Light +2, Red (0°) reaches only 6.99:1 — a hair
under AAA. It is excluded from the canonical palette regardless, but the
docs record the failure rather than rounding it away.

## 6. The canonical theme palette

Themes are built from a subset of the full system:

* the 9-step green ramp (backgrounds, body text, UI chrome);
* **10 chromatic accents, Yellow-Orange (60°) through Magenta (330°)**;
* grey.

**Red (0°) and Orange (30°) are excluded** on the psychology grounds in
§1 — roles that conventionally use them (errors, invalid, deleted) use
Magenta instead. An audit of the version 1 VS Code theme found 9 accents
plus grey in active use, and the common conventions (Solarized, Base16)
standardise on 8 accents — so 10 + grey covers every syntax role with
headroom.

## 7. Reproducing the palette

With coloraide (the project venv in `2 OKLCH colour trials and workings/`
has it installed):

```python
from coloraide import Color

H_STEP = 0.1086                      # derived in §3
def ramp(k):                          # k = -4 … +4
    return 0.5 + k * H_STEP

def swatch(L, hue, chroma=0.11):
    c = Color("oklch", [L, chroma, hue])
    if not c.in_gamut("srgb"):
        c = c.fit("srgb")
    return c.convert("srgb").to_string(hex=True)

bg      = swatch(ramp(-3), 150)            # #001901
aa_fg   = swatch(ramp(1), 150)             # #4d955f  (= AA Green accent)
aaa_row = [swatch(ramp(2), h) for h in range(0, 360, 30)]
grey    = swatch(ramp(2), 0, chroma=0)     # #a4a4a4
```

To re-derive h itself: bisect over h, and at each trial compute the
minimum WCAG contrast across all twelve hues plus grey at
`L = ramp(-3) + 5h` against the background `swatch(ramp(-3), 150)`;
h is the smallest value where that minimum reaches 7.0.

## 8. Design lineage (decision log)

1. **v1:** hand-tuned greens; chromatics at fixed OKLCH L (0.105 steps),
   compliance asserted per-row but only true for some hues.
2. **Contrast audit (June 2026):** revealed that fixed-L rows fail WCAG on
   the red/magenta side (hue-dependent luminance). First fix raised the
   accent rows independently of the ramp (L 0.615 / 0.725) — compliant,
   but it orphaned the accents from the green steps.
3. **Derived ramp (current):** the origin green was kept fixed, and the
   step constant h = 0.1086 was solved from the AAA worst-hue constraint,
   restoring the accent↔ramp identity while keeping both standards exact.
   Red and orange were dropped from the canonical set; the Dark −3 pairing
   was made official.
