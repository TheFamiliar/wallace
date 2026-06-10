#!/usr/bin/env python3
"""Wallace theme generator.

Reads wallace.tokens.json (the single source of truth for the palette and
role map) and emits application theme files. Run from anywhere:

    python3 generate.py                 # all targets + audit
    python3 generate.py bat fzf         # selected targets
    python3 generate.py audit           # verify existing themed files only

Targets: bat, delta, fzf, sequelace, audit

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at http://mozilla.org/MPL/2.0/.
"""

import json
import plistlib
import re
import sys
import uuid
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
TOKENS = json.loads((HERE / "wallace.tokens.json").read_text())

RAMP = {k: v["hex"] for k, v in TOKENS["ramp"].items()}
ROWS = TOKENS["rows"]
RAMP_ORDER = ["dark4", "dark3", "dark2", "dark1", "base",
              "light1", "light2", "light3", "light4"]


class Std:
    """Resolved palette for one contrast standard."""

    def __init__(self, key):
        s = TOKENS["standards"][key]
        self.key = key
        self.label = s["label"]
        self.bg = RAMP[s["background"]]
        self.fg = RAMP[s["foreground"]]
        self.fg_step = s["foreground"]
        self.accents = ROWS[s["accentRow"]]
        self.brights = ROWS[s["brightRow"]]
        self.strong = RAMP[s["strong"]]

    def role(self, name):
        """Hex for a role, from this standard's accent row."""
        colour = TOKENS["roles"][name]["colour"]
        return self.accents[colour]

    def role_style(self, name):
        return TOKENS["roles"][name].get("style")

    def surface(self, name):
        return RAMP[TOKENS["surfaces"][name]]

    def fg_plus(self, n):
        i = RAMP_ORDER.index(self.fg_step)
        return RAMP[RAMP_ORDER[min(i + n, len(RAMP_ORDER) - 1)]]


STANDARDS = [Std("aa"), Std("aaa")]


# --------------------------------------------------------------- bat ---

def tm_rule(name, scope, fg=None, style=None):
    settings = {}
    if fg:
        settings["foreground"] = fg
    if style:
        settings["fontStyle"] = style
    return {"name": name, "scope": scope, "settings": settings}


def emit_bat():
    """TextMate .tmTheme files, used by bat (and by delta via syntax-theme)."""
    out = ROOT / "7 CLI Themes"
    out.mkdir(exist_ok=True)
    for s in STANDARDS:
        rules = [
            {"settings": {
                "background": s.bg,
                "foreground": s.fg,
                "caret": s.surface("cursor"),
                "selection": s.surface("selection"),
                "lineHighlight": s.surface("lineHighlight"),
                "invisibles": s.surface("raised"),
            }},
            tm_rule("Comment", "comment, punctuation.definition.comment",
                    s.role("comment"), s.role_style("comment")),
            tm_rule("String", "string", s.role("string")),
            tm_rule("Regular expression", "string.regexp", s.role("regex")),
            tm_rule("Number, constant",
                    "constant.numeric, constant.language, support.constant, "
                    "constant.character, keyword.other.unit, variable.parameter",
                    s.role("number")),
            tm_rule("Escape character", "constant.character.escape",
                    s.role("punctuation")),
            tm_rule("Keyword, storage", "keyword, storage, storage.type",
                    s.role("keyword")),
            tm_rule("Operator, punctuation",
                    "keyword.operator, punctuation", s.role("operator")),
            tm_rule("Tag", "entity.name.tag, meta.tag.sgml", s.role("tag")),
            tm_rule("Function",
                    "entity.name.function, support.function, "
                    "variable.function, meta.function-call", s.role("function")),
            tm_rule("Attribute", "entity.other.attribute-name",
                    s.role("attribute")),
            tm_rule("CSS class and id",
                    "entity.other.attribute-name.class, "
                    "entity.other.attribute-name.id", s.role("cssClassName")),
            tm_rule("CSS property name",
                    "support.type.property-name", s.role("cssPropertyName")),
            tm_rule("Pseudo-class", "entity.other.attribute-name.pseudo-class",
                    s.role("pseudoClass")),
            tm_rule("Type, class",
                    "support.type, support.class, entity.name.class, "
                    "entity.name.type, entity.other.inherited-class",
                    s.role("type")),
            tm_rule("Variable", "variable, variable.language", s.role("variable")),
            tm_rule("Invalid, deleted", "invalid, markup.deleted",
                    s.role("invalid")),
            tm_rule("Inserted", "markup.inserted", s.role("inserted")),
            tm_rule("Heading", "markup.heading, markup.heading entity.name",
                    s.role("heading")),
            tm_rule("Bold", "markup.bold", s.strong, "bold"),
            tm_rule("Italic", "markup.italic", None, "italic"),
            tm_rule("Inline code", "markup.raw.inline", s.role("inlineCode")),
            tm_rule("Link", "markup.underline.link, string.other.link",
                    s.role("link")),
            tm_rule("Quote", "markup.quote", None, "italic"),
        ]
        theme = {
            "name": s.label,
            "comment": "Wallace palette - generated by generate.py; do not edit by hand",
            "semanticClass": f"theme.dark.wallace_{s.key}",
            "uuid": str(uuid.uuid5(uuid.NAMESPACE_URL, f"wallace/{s.key}/tmtheme")),
            "settings": rules,
        }
        path = out / f"{s.label}.tmTheme"
        with open(path, "wb") as f:
            plistlib.dump(theme, f)
        print(f"  wrote {path.relative_to(ROOT)}")


# ------------------------------------------------------------- delta ---

def emit_delta():
    out = ROOT / "7 CLI Themes"
    out.mkdir(exist_ok=True)
    blocks = []
    for s in STANDARDS:
        deleted = s.role("deleted")
        inserted = s.role("inserted")
        blocks.append(f"""[delta "wallace-{s.key}"]
    dark = true
    # requires the matching bat theme: see wallace-fzf-and-cli-readme below
    syntax-theme = {s.label}
    minus-style = "{deleted}" "{s.surface('recessed')}"
    minus-emph-style = bold "{s.bg}" "{deleted}"
    plus-style = syntax "{s.surface('recessed')}"
    plus-emph-style = bold "{s.bg}" "{inserted}"
    line-numbers = true
    line-numbers-minus-style = "{deleted}"
    line-numbers-plus-style = "{inserted}"
    line-numbers-zero-style = "{RAMP['base']}"
    line-numbers-left-style = "{RAMP['base']}"
    line-numbers-right-style = "{RAMP['base']}"
    file-style = bold "{s.role('heading')}"
    file-decoration-style = ul "{RAMP['base']}"
    hunk-header-style = "{s.accents['grey']}"
    hunk-header-decoration-style = "{RAMP['base']}" box
    commit-style = bold "{s.role('number')}"
    whitespace-error-style = reverse "{deleted}"
    blame-palette = "{RAMP['dark3']}" "{RAMP['dark4']}" "{RAMP['dark2']}"
""")
    header = """# Wallace themes for delta (https://github.com/dandavison/delta)
# Generated by generate.py - do not edit by hand.
#
# Wallace bans red: deletions are magenta, additions green.
#
# Install:
#   1. Save/symlink this file, then in ~/.gitconfig add:
#        [include]
#            path = /path/to/wallace.gitconfig
#        [delta]
#            features = wallace-aa        # or wallace-aaa
#   2. syntax-theme needs the Wallace bat theme installed:
#        mkdir -p "$(bat --config-dir)/themes"
#        cp "7 CLI Themes/Wallace AA.tmTheme" "$(bat --config-dir)/themes/"
#        bat cache --build

"""
    path = out / "wallace.gitconfig"
    path.write_text(header + "\n".join(blocks))
    print(f"  wrote {path.relative_to(ROOT)}")


# --------------------------------------------------------------- fzf ---

def emit_fzf():
    out = ROOT / "7 CLI Themes"
    out.mkdir(exist_ok=True)
    lines = ["""# Wallace colours for fzf (https://github.com/junegunn/fzf)
# Generated by generate.py - do not edit by hand.
# Source this file from your shell profile, then pick one:
#   export FZF_DEFAULT_OPTS="$FZF_DEFAULT_OPTS $WALLACE_FZF_AA"
#   export FZF_DEFAULT_OPTS="$FZF_DEFAULT_OPTS $WALLACE_FZF_AAA"
"""]
    for s in STANDARDS:
        colours = ",".join([
            f"bg:{s.bg}",
            f"fg:{s.fg}",
            f"bg+:{s.surface('selection')}",
            f"fg+:{s.strong}",
            f"hl:{s.role('matchHighlight')}",
            f"hl+:{s.brights[TOKENS['roles']['matchHighlight']['colour']]}",
            f"query:{s.fg_plus(1)}",
            f"info:{s.accents['grey']}",
            f"prompt:{s.role('heading')}",
            f"pointer:{s.surface('cursor')}",
            f"marker:{s.role('variable')}",
            f"spinner:{s.accents['grey']}",
            f"header:{s.accents['grey']}",
            f"border:{RAMP['base']}",
            f"label:{s.accents['grey']}",
            f"gutter:{s.surface('recessed')}",
            f"separator:{RAMP['base']}",
            f"scrollbar:{RAMP['base']}",
        ])
        lines.append(f'WALLACE_FZF_{s.key.upper()}="--color={colours}"')
    path = out / "wallace-fzf.sh"
    path.write_text("\n".join(lines) + "\n")
    print(f"  wrote {path.relative_to(ROOT)}")


# --------------------------------------------------------- sequel ace ---

def emit_sequelace():
    """Sequel Ace .spTheme: tmTheme-style plist, hex strings, six named slots."""
    out = ROOT / "8 Sequel Ace Theme"
    out.mkdir(exist_ok=True)
    for s in STANDARDS:
        theme = {
            "name": s.label,
            "settings": [
                {"settings": {
                    "background": s.bg,
                    "foreground": s.fg,
                    "caret": s.surface("cursor"),
                    "selection": s.surface("selection"),
                    "lineHighlight": s.surface("lineHighlight"),
                }},
                {"name": "Comment",
                 "settings": {"foreground": s.role("comment"),
                              "fontStyle": "italic"}},
                {"name": "String", "settings": {"foreground": s.role("string")}},
                {"name": "Keyword", "settings": {"foreground": s.role("keyword")}},
                # backtick-quoted table/column identifiers
                {"name": "User-defined constant",
                 "settings": {"foreground": s.role("identifier")}},
                {"name": "Number", "settings": {"foreground": s.role("number")}},
                {"name": "Variable", "settings": {"foreground": s.role("variable")}},
            ],
        }
        path = out / f"{s.label}.spTheme"
        with open(path, "wb") as f:
            plistlib.dump(theme, f)
        print(f"  wrote {path.relative_to(ROOT)}")


# ------------------------------------------------------------- audit ---

AUDIT_FILES = [
    "3 VS Code themes/wallace-aaa/themes/Wallace AA-color-theme.json",
    "3 VS Code themes/wallace-aaa/themes/Wallace AAA-color-theme.json",
    "4 Marked 2 Theme/Wallace AA.css",
    "4 Marked 2 Theme/Wallace AAA.css",
    "6 BB Edit Theme/Wallace AA.bbColorScheme",
    "6 BB Edit Theme/Wallace AAA.bbColorScheme",
    "7 CLI Themes/Wallace AA.tmTheme",
    "7 CLI Themes/Wallace AAA.tmTheme",
    "7 CLI Themes/wallace.gitconfig",
    "7 CLI Themes/wallace-fzf.sh",
    "8 Sequel Ace Theme/Wallace AA.spTheme",
    "8 Sequel Ace Theme/Wallace AAA.spTheme",
]


def palette_hexes():
    hexes = {v["hex"].lstrip("#").lower() for v in TOKENS["ramp"].values()}
    for row in TOKENS["rows"].values():
        hexes |= {h.lstrip("#").lower() for h in row.values()}
    return hexes


def rgba_to_hex(m):
    vals = [float(x) for x in m.groups()[:3]]
    # BBEdit writes 0-1 floats, CSS writes 0-255 ints
    scale = 1 if max(vals) > 1 else 255
    return "".join(f"{round(v * scale):02x}" for v in vals)


def audit():
    allowed = palette_hexes()
    rgba = re.compile(r"rgba\(([\d.]+),([\d.]+),([\d.]+),([\d.]+)\)")
    ok = True
    for rel in AUDIT_FILES:
        p = ROOT / rel
        if not p.exists():
            print(f"  MISSING {rel}")
            ok = False
            continue
        text = p.read_text(errors="ignore").lower()
        found = set(re.findall(r"#([0-9a-f]{6})\b", text))
        found |= {rgba_to_hex(m) for m in rgba.finditer(text)}
        bad = found - allowed
        if bad:
            print(f"  FAIL {rel}: non-palette colours {sorted('#' + b for b in bad)}")
            ok = False
    print("  audit:", "all themed files use palette colours only" if ok else "FAILURES above")
    return ok


# -------------------------------------------------------------- main ---

TARGETS = {"bat": emit_bat, "delta": emit_delta, "fzf": emit_fzf,
           "sequelace": emit_sequelace, "audit": audit}

if __name__ == "__main__":
    chosen = sys.argv[1:] or ["bat", "delta", "fzf", "sequelace", "audit"]
    bad = [c for c in chosen if c not in TARGETS]
    if bad:
        sys.exit(f"unknown target(s) {bad}; choose from {sorted(TARGETS)}")
    result = True
    for c in chosen:
        print(f"{c}:")
        r = TARGETS[c]()
        if r is False:
            result = False
    sys.exit(0 if result else 1)
