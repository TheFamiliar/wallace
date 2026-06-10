# Installing the Wallace themes

Every application ships two variants: **Wallace AA** (4.5:1 contrast,
body text Light +1) and **Wallace AAA** (7:1 contrast, body text
Light +2). Both use the same Dark -3 background and the same hue-per-role
mapping, so you can mix variants across apps and everything still reads
as one system. Install whichever suits — AAA is brighter, AA is the
lowest-luminance option.

Paths below are relative to this repository's root.

---

## VS Code

Theme files: `3 VS Code themes/wallace-aaa/` (one extension containing
both themes plus the Markdown preview stylesheet).

**Local install (testing, no marketplace):**

```sh
cp -R "3 VS Code themes/wallace-aaa/." ~/.vscode/extensions/martin-jewiss.wallace-themes-2.0.0/
rm -f ~/.vscode/extensions/martin-jewiss.wallace-themes-2.0.0/.DS_Store
```

Then in VS Code: `Cmd+Shift+P` → **Developer: Reload Window**, then
`Cmd+Shift+P` → **Preferences: Color Theme** → *Wallace AA* or
*Wallace AAA*.

If an old `~/.vscode/extensions/wallace-aaa` folder exists from version 1,
delete it to avoid a duplicate "Wallace AAA" entry in the theme picker.

**Recommended companion extensions** (grammars the themes have rules for):

* *Twig Language 2* — Twig templates
* *DotENV* (mikestead) — `.env` files
* *Apache Conf* — `.htaccess`
* *Perch Language Support* (`lachieh.perch-language-support`) — Perch CMS tags

**Markdown preview:** styled automatically (the extension contributes a
preview stylesheet that follows the active Wallace variant). For the
intended typography install the *Hanken Grotesk*, *IBM Plex Serif* and
*IBM Plex Mono* fonts locally; system fallbacks are used otherwise.

**CakePHP note:** if you use legacy `.ctp` templates, map them to PHP in
settings: `"files.associations": { "*.ctp": "php" }`.

**Publishing to the marketplace (when ready):** create a publisher at
https://marketplace.visualstudio.com/manage matching the `publisher`
field in `package.json`, then from the extension folder run
`npx @vscode/vsce package` to produce a `.vsix` (installable directly via
*Extensions: Install from VSIX*) and `npx @vscode/vsce publish` to
publish.

---

## Marked 2

Theme files: `4 Marked 2 Theme/Wallace AA.css`, `Wallace AAA.css`.

1. Marked 2 → **Settings → Style**
2. Click **+** (Add Custom Style) and choose the CSS file(s)
3. Select *Wallace AA* or *Wallace AAA* from the style dropdown in the
   preview window

Fonts: the stylesheets load Hanken Grotesk / IBM Plex from Google Fonts
automatically; no local installation needed.

---

## macOS Terminal

Theme files: `5 Terminal Theme/Wallace AA.terminal`, `Wallace AAA.terminal`.

Either double-click a `.terminal` file in Finder, or in Terminal:
**Settings → Profiles →** gear menu below the profile list → **Import…**.
Set the imported profile as **Default** if you want it for new windows.

Note: ANSI *red* is mapped to magenta and ANSI *magenta* to violet —
programs that print red errors show them in magenta (Wallace bans red).
This convention is consistent across Terminal, the VS Code integrated
terminal, delta and fzf.

---

## BBEdit

Theme files: `6 BB Edit Theme/Wallace AA.bbColorScheme`,
`Wallace AAA.bbColorScheme`.

```sh
mkdir -p ~/Library/Application\ Support/BBEdit/Color\ Schemes
cp "6 BB Edit Theme/"*.bbColorScheme ~/Library/Application\ Support/BBEdit/Color\ Schemes/
```

Then BBEdit → **Settings → Appearance → Color Scheme** → *Wallace AA* or
*Wallace AAA*.

Limitation: BBEdit's insertion-point colour isn't schemable; the schemes
compensate with a Dark -2 line highlight (`HighlightInsertionPoint`).

---

## bat

Theme files: `7 CLI Themes/Wallace AA.tmTheme`, `Wallace AAA.tmTheme`.
(`brew install bat` if needed.)

```sh
mkdir -p "$(bat --config-dir)/themes"
cp "7 CLI Themes/"*.tmTheme "$(bat --config-dir)/themes/"
bat cache --build
```

Then set the default theme in `$(bat --config-dir)/config`:

```
--theme="Wallace AA"
```

(or `Wallace AAA`). Check with `bat --list-themes | grep Wallace`.

---

## delta (git diffs)

Theme file: `7 CLI Themes/wallace.gitconfig`.
(`brew install git-delta` if needed.)

**Requires the bat theme first** — delta reuses it for syntax
highlighting inside diffs (the `syntax-theme` setting), so do the bat
install above even if you don't use bat directly.

Add to `~/.gitconfig`:

```ini
[include]
    path = /path/to/wallace/7 CLI Themes/wallace.gitconfig

[core]
    pager = delta

[interactive]
    diffFilter = delta --color-only

[delta]
    features = wallace-aa    ; or wallace-aaa
```

Deletions appear in magenta, additions in green, matching the themes'
error/inserted roles everywhere else.

---

## fzf

Theme file: `7 CLI Themes/wallace-fzf.sh`.
(`brew install fzf` if needed.)

Add to your shell profile (`~/.zshrc`):

```sh
source "/path/to/wallace/7 CLI Themes/wallace-fzf.sh"
export FZF_DEFAULT_OPTS="$FZF_DEFAULT_OPTS $WALLACE_FZF_AA"   # or $WALLACE_FZF_AAA
```

---

## Sequel Ace

Theme files: `8 Sequel Ace Theme/Wallace AA.spTheme`, `Wallace AAA.spTheme`.

Sequel Ace → **Settings → Editor** → gear menu beneath the theme list →
**Import…** and choose the `.spTheme` file(s); or copy them directly:

```sh
cp "8 Sequel Ace Theme/"*.spTheme ~/Library/Containers/com.sequel-ace.sequel-ace/Data/Library/Application\ Support/Sequel\ Ace/Themes/
```

Then pick *Wallace AA* or *Wallace AAA* as the editor theme.

---

## Keeping things in sync

The CLI and Sequel Ace themes are generated — never edit them by hand.
After any palette change:

```sh
python3 "0 Palette tokens and generator/generate.py"
```

which regenerates those targets and audits *every* themed file in the
repository against the palette. The VS Code, Marked 2, BBEdit and
Terminal themes are hand-maintained but covered by the same audit.
