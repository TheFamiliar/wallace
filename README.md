Wallace
=======

A family of colour themes intended to improve productivity and creativity,
while reducing eye strain.

## Aims

1. WCAG AA contrast compliant palette
2. WCAG AAA contrast compliant palette
3. Uniform perceptual luminance for all colours in each palette
4. Visual Studio Code themes for each palette
5. BBEdit themes for each palette
6. Marked 2 themes for each palette
7. macOS Terminal themes for each palette

## Overview of colours

For ease, base colour definitions and operations are in OKLCH, a perceptually uniform color space where equal mathematical intervals produce equal visual differences.

Colours are converted to rgb/hex/hsl as a final step, only when the destination application does not support oklch.

All colours are derived from a single muted forest green origin, at the mid-point of the luminance scale: **`oklch(0.5 0.11 150)`** — plus one derived constant, the ramp step **h = 0.1086**.

The step constant is solved so that contrast is a function of step distance alone: text **4 steps** above its surface meets **AA** (4.5:1) for every hue of the chromatic wheel, and **5 steps** meets **AAA** (7:1). The full construction — origin → monochromatic green ramp → chromatic palette, including the mathematical/musical reasoning behind the step — is documented in [`1 Main colour palettes/Wallace Palette Derivation.md`](1%20Main%20colour%20palettes/Wallace%20Palette%20Derivation.md).

The **official palette is the Dark -3 variant** (background `#001901`): lower overall luminance for reduced eye strain, suited to photophobia and light sensitivity. A higher-luminance Dark -2 variant is documented alongside it.

The canonical theme palette excludes red and orange (see below); error/alert roles use magenta instead.

The origin green and palette colour selections have been informed by psychology research studies which together indicate:

1. Green hues tend to boost creativity and aid in completion of creative tasks
2. Red hues tend to increase speed of brain function but reduce cognitive ability.

## Installing the themes

Step-by-step instructions for every application (VS Code, Marked 2, macOS Terminal, BBEdit, bat, delta, fzf, Sequel Ace) are in [INSTALL.md](INSTALL.md).

## Repository layout

0. **Palette tokens and generator** — `wallace.tokens.json`, the machine-readable source of truth (palette + role map), and `generate.py`, which emits the CLI and Sequel Ace themes and audits every themed file against the palette.
1. **Main colour palettes** — the four palette definitions (AA/AAA × Dark -3 official/Dark -2 variant), the derivation document, and a visual comparison page.
2. **OKLCH colour trials and workings** — scripts, experiments and a Python venv (coloraide) used to generate and verify colours.
3. **VS Code themes** — one extension contributing both *Wallace AA* and *Wallace AAA*.
4. **Marked 2 Theme** — `Wallace AA.css` and `Wallace AAA.css`.
5. **Terminal Theme** — `Wallace AA.terminal` and `Wallace AAA.terminal` profiles.
6. **BB Edit Theme** — `Wallace AA.bbColorScheme` and `Wallace AAA.bbColorScheme`.
7. **CLI Themes** — bat (`.tmTheme`), delta (`wallace.gitconfig`) and fzf (`wallace-fzf.sh`), generated from the tokens.
8. **Sequel Ace Theme** — `Wallace AA.spTheme` and `Wallace AAA.spTheme`, generated from the tokens.
