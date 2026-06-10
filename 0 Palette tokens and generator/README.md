# Wallace tokens & generator

`wallace.tokens.json` is the **single source of truth** for the Wallace
palette: the green ramp, the chromatic rows, the role map (which hue does
which job), the surfaces, and the ANSI mapping. The values are the
verified, gamut-fitted hexes; how they were derived from the origin green
and the step constant is documented in
`../1 Main colour palettes/Wallace Palette Derivation.md`.

`generate.py` (python3, stdlib only) emits application themes from the
tokens and audits the repository:

```
python3 generate.py                 # all targets + audit
python3 generate.py bat fzf         # selected targets
python3 generate.py audit           # verify themed files only
```

| Target | Output | Install |
|---|---|---|
| `bat` | `7 CLI Themes/Wallace AA.tmTheme`, `…AAA.tmTheme` | `cp` into `$(bat --config-dir)/themes/`, run `bat cache --build`, set `--theme="Wallace AA"` in bat's config |
| `delta` | `7 CLI Themes/wallace.gitconfig` | `[include] path = …` in `~/.gitconfig`, then `[delta] features = wallace-aa` (needs the bat theme installed — delta reuses it via `syntax-theme`) |
| `fzf` | `7 CLI Themes/wallace-fzf.sh` | source it, then append `$WALLACE_FZF_AA` (or `_AAA`) to `FZF_DEFAULT_OPTS` |
| `sequelace` | `8 Sequel Ace Theme/Wallace AA.spTheme`, `…AAA.spTheme` | Sequel Ace → Settings → Editor → theme list gear → Import, or copy into `~/Library/Containers/com.sequel-ace.sequel-ace/Data/Library/Application Support/Sequel Ace/Themes/` |
| `audit` | — | checks that every colour in the themed files (VS Code, Marked 2, BBEdit, CLI, Sequel Ace) is a palette value — catches drift and typos |

The VS Code, Marked 2, BBEdit and Terminal themes are still hand-maintained
(they carry per-app detail beyond the role map) but are covered by the
audit. If the palette ever changes: update the tokens file, re-run the
generator, and follow the old→new hex map for the hand-maintained files.

## ANSI convention

Wallace bans red and orange. In every terminal-flavoured output the ANSI
**red slot carries magenta** (the palette's error role) and the ANSI
**magenta slot shifts to violet** so the two stay distinct. Programs that
print "red" errors stay legible — just never red.
