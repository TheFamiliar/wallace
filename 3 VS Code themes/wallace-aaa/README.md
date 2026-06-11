# Wallace Themes

Forest-green colour themes for VS Code, based on psychology research into
the best colours for creativity, and built for low-glare, accessible
reading. Two variants ship in this extension:

- **Wallace AA** — every accent colour reaches at least **4.5:1** (WCAG AA)
  against the editor background.
- **Wallace AAA** — every accent colour reaches at least **7:1** (WCAG AAA).

## The palette

All colours derive from a single origin green, `oklch(0.5 0.11 150)`,
and one solved constant: the ramp step. The monochromatic green ramp runs
four steps either side of the origin at equal perceptual-lightness
intervals; the accent palette is the hue wheel rotated about a ramp step,
so every accent row sits at one OKLCH lightness. The step is the smallest
value where every hue the required number of steps above the background
clears its contrast bar — so compliance is a property of the geometry,
not of per-colour tuning.

There is no red and no orange anywhere in the themes: error and alert
roles use magenta instead. The current line is marked with a border
rather than a fill, so text on it keeps full contrast.

The palette source of truth, derivation notes, and themes for seven other
applications (Terminal, BBEdit, Marked 2, bat, delta, fzf, Sequel Ace)
live in the Wallace repository.

## Install from VSIX

```
code --install-extension wallace-themes-2.1.1.vsix
```

Then **Cmd+K Cmd+T** and pick *Wallace AA* or *Wallace AAA*.

## Licence

MPL-2.0.
