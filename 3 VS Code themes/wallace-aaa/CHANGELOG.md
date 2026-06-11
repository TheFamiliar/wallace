# Change Log
All notable changes to the "wallace-aaa" extension will be documented in this file.

Check [Keep a Changelog](http://keepachangelog.com/) for recommendations on how to structure this file.

## [2.1.1] - 2026-06-11
- Current line is now marked with a border (`editor.lineHighlightBorder`,
  Dark -2) instead of a filled background, so text on the current line
  keeps full AA/AAA contrast against the editor background.
- Selection background dropped one step (Dark -1 → Dark -2) to dim the
  selected-text surface.

## [2.1.0] - 2026-06-11
- Version 3 palette: ramp compressed toward base (step 0.087, was 0.1086)
  after the version 2 background proved slightly too dark in use. New
  background `#002909`; every light row shifts up one rung (AA foreground/
  accents light1→light2, AAA light2→light3) so AA 4.5:1 and AAA 7:1 hold
  for every hue.
- Bracket pair colorization now themed: all six nesting levels use the
  punctuation grey (fixes VS Code's default gold brackets in CSS/JS and
  gold `${` in template literals); unexpected brackets use the error
  magenta.

## [2.0.1] - 2026-06-11
- Restored version 1 role assignments using version 2 palette equivalents:
  strings, classes/entity names and JS constructors back to cyan; markdown
  headings and JS method names back to yellow-orange; semantic parameter to
  yellow-orange, property to yellow.
- Class names now use the same cyan in every file type: new rule pins HTML
  `class="..."`/`id="..."` attribute values to the CSS class selector colour.
- Comments stay grey (V1's dim green fails the contrast targets).

## [Unreleased]
- Initial release
