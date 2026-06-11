#!/usr/bin/env python3
"""Migrate the Wallace palette from version 2 to version 3 (option A,
"compressed nine": uniform step 0.087, background dark3 #002909).

The ramp keeps 9 steps but every step pulls toward base (~0.83x).  To keep
the contrast bars, both standards' rows shift up one rung:

  AA : foreground/accents light1 -> light2, brights light2 -> light3
  AAA: foreground/accents light2 -> light3, brights light3 -> light4

Does three things:
  1. rewrites 0 Palette tokens and generator/wallace.tokens.json
  2. builds the v2 -> v3 colour map (v3_hex_map.json, also used by the
     Terminal theme migrator)
  3. applies the map to the hand-maintained theme files (VS Code, Marked,
     BBEdit), handling hex and both rgba() scales

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at http://mozilla.org/MPL/2.0/.
"""

import json
import re
from pathlib import Path

import v3_ramp_options as base

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
TOKENS_PATH = ROOT / "0 Palette tokens and generator" / "wallace.tokens.json"
V2 = json.loads(TOKENS_PATH.read_text())

STEP = 0.087
RAMP_NAMES = ["light4", "light3", "light2", "light1", "base",
              "dark1", "dark2", "dark3", "dark4"]
K = {"light4": 4, "light3": 3, "light2": 2, "light1": 1, "base": 0,
     "dark1": -1, "dark2": -2, "dark3": -3, "dark4": -4}


def ramp_l(name):
    return round(0.5 + K[name] * STEP, 4)


def full_row(l):
    """All 12 hues + grey, in the same order version 2 recorded them."""
    row = {h: base.swatch(l, base.CHROMA, hue)
           for h, hue in V2["hues"].items()}
    row["grey"] = base.grey(l)
    return row


def build_tokens():
    ramp = {n: {"l": ramp_l(n), "hex": base.swatch(ramp_l(n))}
            for n in RAMP_NAMES}
    rows = {n: full_row(ramp_l(n)) for n in ("light2", "light3", "light4")}
    t = dict(V2)
    t["meta"] = dict(V2["meta"])
    t["meta"]["version"] = "3.0.0"
    t["meta"]["step"] = STEP
    t["meta"]["formula"] = {
        "ramp": "L(k) = origin.l + k * step, k = -4..+4, at C=0.11 H=150",
        "accentRow": "oklch(L(step) 0.11 hue) for hue = 0,30,...,330; grey at C=0",
        "step": "smallest uniform interval where every hue 6 steps above the "
                "background reaches 7:1 (AAA); 5 steps then gives 4.5:1 (AA) "
                "for every hue",
        "gamut": "colours outside sRGB are fitted with coloraide "
                 "fit('srgb', method='lch-chroma') -- later coloraide "
                 "releases changed the default fit, so name it explicitly; "
                 "hexes below are the fitted, verified values",
    }
    t["ramp"] = ramp
    t["rows"] = rows
    t["standards"] = {
        "aa": {"label": "Wallace AA", "minContrast": 4.5,
               "background": "dark3", "foreground": "light2",
               "accentRow": "light2", "brightRow": "light3",
               "strong": "light4"},
        "aaa": {"label": "Wallace AAA", "minContrast": 7.0,
                "background": "dark3", "foreground": "light3",
                "accentRow": "light3", "brightRow": "light4",
                "strong": "light4"},
    }
    return t, ramp


def build_map(ramp):
    """v2 hex -> v3 hex. Dark steps and base keep their names; every light
    row shifts up one (light4 stays light4 -- the top of the ramp)."""
    m = {}
    for n in ("dark4", "dark3", "dark2", "dark1", "base"):
        m[V2["ramp"][n]["hex"]] = ramp[n]["hex"]
    shift = {"light1": "light2", "light2": "light3", "light3": "light4"}
    for old_row, new_row in shift.items():
        new = full_row(ramp_l(new_row))
        for hue, old_hex in V2["rows"][old_row].items():
            m[old_hex] = new[hue]
    m[V2["ramp"]["light4"]["hex"]] = ramp["light4"]["hex"]
    assert len(m) == 5 + 3 * 13 + 1
    return m


# ------------------------------------------------------- file rewriting ---

MIGRATE_FILES = [
    "3 VS Code themes/wallace-aaa/themes/Wallace AA-color-theme.json",
    "3 VS Code themes/wallace-aaa/themes/Wallace AAA-color-theme.json",
    "4 Marked 2 Theme/Wallace AA.css",
    "4 Marked 2 Theme/Wallace AAA.css",
    "6 BB Edit Theme/Wallace AA.bbColorScheme",
    "6 BB Edit Theme/Wallace AAA.bbColorScheme",
]


def apply_map(text, cmap):
    counts = {"hex": 0, "rgba": 0}

    def hex_sub(m):
        new = cmap.get(m.group(0).lower())
        if new:
            counts["hex"] += 1
            return new
        return m.group(0)

    def rgba_sub(m):
        parts = [p.strip() for p in m.group(1).split(",")]
        vals = [float(p) for p in parts[:3]]
        floats = max(vals) <= 1.0
        scale = 255 if not floats else 1
        old_hex = "#" + "".join(f"{round(v * (1 if not floats else 255)):02x}"
                                for v in vals)
        new = cmap.get(old_hex)
        if not new:
            return m.group(0)
        counts["rgba"] += 1
        rgb = [int(new[i:i + 2], 16) for i in (1, 3, 5)]
        if floats:
            body = ",".join(f"{v / 255:.6f}" for v in rgb)
        else:
            body = ",".join(str(v) for v in rgb)
        return f"rgba({body},{parts[3]})" if len(parts) == 4 else f"rgba({body})"

    text = re.sub(r"#[0-9a-fA-F]{6}(?![0-9a-fA-F])", hex_sub, text)
    text = re.sub(r"rgba\(([^)]+)\)", rgba_sub, text)
    return text, counts


def main():
    tokens, ramp = build_tokens()
    TOKENS_PATH.write_text(json.dumps(tokens, indent=2) + "\n")
    print(f"wrote {TOKENS_PATH.relative_to(ROOT)} (version 3.0.0, step {STEP})")

    cmap = build_map(ramp)
    map_path = HERE / "v3_hex_map.json"
    map_path.write_text(json.dumps(cmap, indent=1) + "\n")
    print(f"wrote {map_path.relative_to(ROOT)} ({len(cmap)} entries)")

    for rel in MIGRATE_FILES:
        p = ROOT / rel
        new_text, counts = apply_map(p.read_text(), cmap)
        p.write_text(new_text)
        print(f"  {rel}: {counts['hex']} hex + {counts['rgba']} rgba replaced")


if __name__ == "__main__":
    main()
