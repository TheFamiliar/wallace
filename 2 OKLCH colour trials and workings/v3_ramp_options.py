#!/usr/bin/env python3
"""Wallace version 3 ramp explorations.

The version 2 ramp is linear in OKLCH L (step 0.1086) and the background
(dark3) is slightly too dark in use.  This script works up candidate ramps
that pull the background lighter while keeping the three invariants:

  1. the foreground green IS the green of the accent row (same L, C, H)
  2. every accent row sits at one OKLCH lightness (equal perceptual lightness)
  3. AA accents >= 4.5:1 and AAA accents >= 7:1 against the background

Options computed:
  A "equal temperament": constant WCAG contrast ratio between adjacent
     steps (geometric in flare-corrected luminance Y+0.05), 9 steps.
  B "eleven steps": linear in L, 5 steps either side of base; background
     moves to dark4 of the finer ramp.
  C "melodic" asymmetric: dark side compressed to a chosen background,
     light side stretched the minimum needed to restore contrast.

Writes v3_options_data.js for the HTML presenter and prints an audit.

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at http://mozilla.org/MPL/2.0/.
"""

import json
from pathlib import Path

from coloraide import Color

HERE = Path(__file__).resolve().parent
TOKENS = json.loads((HERE.parent / "0 Palette tokens and generator" /
                     "wallace.tokens.json").read_text())

CHROMA = 0.11
HUE_GREEN = 150
HUES = {k: v for k, v in TOKENS["hues"].items()
        if k not in TOKENS["excludedHues"]}      # 10 hues, no red/orange


def swatch(l, c=CHROMA, h=HUE_GREEN):
    """Hex for oklch(l c h), gamut-fitted the same way as version 2."""
    return (Color("oklch", [l, c, h]).convert("srgb")
            .fit("srgb", method="lch-chroma").to_string(hex=True))


def grey(l):
    return swatch(l, 0.0)


def luminance(hex_):
    return Color(hex_).luminance()


def contrast(fg_hex, bg_hex):
    return Color(fg_hex).contrast(bg_hex, method="wcag21")


def l_for_green_luminance(y_target):
    """OKLCH L whose fitted green swatch has relative luminance y_target."""
    lo, hi = 0.0, 1.0
    for _ in range(60):
        mid = (lo + hi) / 2
        if luminance(swatch(mid)) < y_target:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def row(l):
    """One equal-lightness accent row: 10 hues + grey."""
    r = {name: swatch(l, CHROMA, hue) for name, hue in HUES.items()}
    r["grey"] = grey(l)
    return r


def row_min_contrast(l, bg_hex):
    return min(contrast(hex_, bg_hex) for hex_ in row(l).values())


def verify_pipeline():
    """Reproduce every version 2 hex from the formula; abort on mismatch."""
    bad = []
    for name, spec in TOKENS["ramp"].items():
        got = swatch(spec["l"])
        if got != spec["hex"]:
            bad.append((name, spec["hex"], got))
    for row_name, hexes in TOKENS["rows"].items():
        l = TOKENS["ramp"][row_name]["l"]
        for hue, want in hexes.items():
            got = grey(l) if hue == "grey" else swatch(l, CHROMA, TOKENS["hues"][hue])
            if got != want:
                bad.append((f"{row_name}/{hue}", want, got))
    if bad:
        for b in bad:
            print("  MISMATCH", b)
        raise SystemExit("pipeline does not reproduce version 2 hexes")
    print("  pipeline reproduces all version 2 hexes exactly")


# ---------------------------------------------------------------- ramps ---

BASE_L = TOKENS["meta"]["origin"]["l"]          # 0.5
V2_STEP = TOKENS["meta"]["step"]                # 0.1086
Y_BASE = None                                   # set in main
DARK4_FLOOR_L = TOKENS["ramp"]["dark4"]["l"]    # keep near-black floor


def steps_linear(step, n):
    """k = -n..+n  ->  {name: L}"""
    names = ([f"dark{i}" for i in range(n, 0, -1)] + ["base"] +
             [f"light{i}" for i in range(1, n + 1)])
    return {name: BASE_L + (i - n) * step for i, name in enumerate(names)}


def passes(ls, bg_name, aa_row, aaa_row):
    bg = swatch(ls[bg_name])
    return (row_min_contrast(ls[aaa_row], bg) >= 7.0 and
            row_min_contrast(ls[aa_row], bg) >= 4.5)


def search_min(make_ls, bg_name, aa_row, aaa_row, lo, hi):
    """Smallest parameter (4 dp, rounded up) whose ramp passes both bars."""
    for _ in range(40):
        mid = (lo + hi) / 2
        if passes(make_ls(mid), bg_name, aa_row, aaa_row):
            hi = mid
        else:
            lo = mid
    p = round(hi + 0.00005, 4)
    assert passes(make_ls(p), bg_name, aa_row, aaa_row)
    return p


def option_a():
    """Every step pulled toward base by the same factor; the AAA accent row
    moves up one rung (light2 -> light3) so 7:1 still holds.  The smallest
    passing step gives the maximum pull (lightest background)."""
    def make_ls(step):
        return steps_linear(step, 4)
    s = search_min(make_ls, "dark3", "light2", "light3", 0.07, V2_STEP)
    return {"param": ("step", s), "ls": make_ls(s),
            "bg": "dark3", "aa": "light2", "aaa": "light3"}


def option_b():
    def make_ls(step):
        return steps_linear(step, 5)
    s = search_min(make_ls, "dark4", "light2", "light3", 0.06, 0.12)
    return {"param": ("step", s), "ls": make_ls(s),
            "bg": "dark4", "aa": "light2", "aaa": "light3"}


def option_c(bg_l=0.215):
    dark_step = (BASE_L - bg_l) / 3

    def make_ls(light_step):
        ls = {f"dark{i}": BASE_L - i * dark_step for i in range(1, 5)}
        ls["base"] = BASE_L
        ls.update({f"light{i}": BASE_L + i * light_step for i in range(1, 5)})
        return ls
    s = search_min(make_ls, "dark3", "light1", "light2", V2_STEP, 0.16)
    return {"param": ("light step", s, "dark step", round(dark_step, 4)),
            "ls": make_ls(s), "bg": "dark3", "aa": "light1", "aaa": "light2"}


def current():
    return {"param": ("step", V2_STEP), "ls": steps_linear(V2_STEP, 4),
            "bg": "dark3", "aa": "light1", "aaa": "light2"}


# ----------------------------------------------------------- packaging ---

def package(key, title, note, opt):
    ls = opt["ls"]
    ramp = {name: {"l": round(l, 4), "hex": swatch(l)}
            for name, l in sorted(ls.items(), key=lambda kv: kv[1])}
    bg_hex = ramp[opt["bg"]]["hex"]
    standards = {}
    for std, row_name, bar in (("aa", opt["aa"], 4.5), ("aaa", opt["aaa"], 7.0)):
        hexes = row(ls[row_name])
        cons = {hue: round(contrast(h, bg_hex), 2) for hue, h in hexes.items()}
        worst = min(cons, key=cons.get)
        standards[std] = {
            "row": row_name, "bar": bar, "fg": hexes["green"],
            "accents": hexes, "contrast": cons,
            "worst": {"hue": worst, "ratio": cons[worst]},
        }
        print(f"  {key} {std.upper():3} row={row_name} "
              f"min contrast {cons[worst]:.2f} ({worst}) vs bar {bar}")
    # one step above the accent row, for the "bright" row used by bold text
    order = list(ramp.keys())
    brights = {std: row(ls[order[min(order.index(standards[std]["row"]) + 1,
                                     len(order) - 1)]])
               for std in standards}
    return {"key": key, "title": title, "note": note,
            "param": opt["param"], "bg": opt["bg"], "bgHex": bg_hex,
            "bgL": ramp[opt["bg"]]["l"], "ramp": ramp,
            "standards": standards, "brights": brights}


def main():
    global Y_BASE
    print("pipeline:")
    verify_pipeline()
    Y_BASE = luminance(swatch(BASE_L))
    print("options:")
    options = [
        package("current", "Current (v2)",
                "Linear in L, step 0.1086. Background = dark3.", current()),
        package("b", "B — Eleven steps",
                "Linear in L with 5 steps either side of base. The "
                "background moves to dark4 of the finer ramp; AA accents "
                "sit at light2, AAA at light3.",
                option_b()),
        package("c", "C — Melodic (asymmetric)",
                "Dark side compressed (step 0.0950) to lift the background; "
                "light side stretched the minimum (step 0.1259) so AA and "
                "AAA still hold at the familiar light1 / light2 rows.",
                option_c()),
        package("a", "A — Compressed nine",
                "Every step pulled toward base by the same factor (~0.83x); "
                "AA accents move to light2, AAA to light3, so the contrast "
                "bars still hold. Maximum pull toward base.",
                option_a()),
    ]
    roles = TOKENS["roles"]
    data = {"options": options, "roles": roles, "v2step": V2_STEP}
    out = HERE / "v3_options_data.js"
    out.write_text("const DATA = " + json.dumps(data, indent=1) + ";\n")
    print(f"wrote {out.name}")
    for o in options:
        print(f"  {o['key']:8} bg L={o['bgL']:.4f} {o['bgHex']}  param={o['param']}")


if __name__ == "__main__":
    main()
