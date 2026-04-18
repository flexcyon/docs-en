---
title: Version 0.4.x
icon: material/numeric-4
---

### Version 0.4.0 Light Mode Update

- Changed sidebar background brightness setting default to `unset`.
  Was previously causing issues like blurring Calender plugin content.

- WIP light theme (mixes flexoki light + origami colour palette)

- Others misc changes

  - Added toggle for extended colour palette, on by default

  - Added table header size option

  - Updated documentation to show a small preview of colors/opacity applied by
    the theme

  - Added web showcase of the theme's features

  - Remove Easter Egg mode

- Style color picker for light and dark mode options

- ASCII Art and quotes now inherit from the interface font

- Improved prompt styling and tree item padding

- Return to Zero (ultra minimalist mode) inspired by Shimmering Focus

### Version 0.4.1 Quickfix Update

- Fix TUI rendering in light mode

- Fix left sidebar toggle when ribbon is not enabled

- Fix text highlight bg specifically with suggestion-highlight

- Fix embeds not displaying

### Version 0.4.2 Relative Line Numbers

- Removed leftover Easter Egg Mode stuff
- File line width setting using `cssclasses`
- New documentation site with translations over at https://flexcyon-docs.readthedocs.io/en/latest/
  - Old documentation is deprecated
- Fixed light mode background colours and active line gutter
- Relative line numbers adapted from Shimmering Focus
  - Add options to configure Roman numerals, lower Greek letters
  - Add options to only display relative line numbers, relative line numbers and normal line numbers on different lines
  - Add option to toggle active line number to adapt relative line number style
- Fixed Headings Indicator `cssclasses` not working
- Fixed background colour issue with TUI
- Add global writing mode option

### Version 0.4.3 Rainbow Repair

- Fixed rainbow bullet lists, rainbow folders, side dock icon effects
- Add Style Settings option for configuring tree item padding
- Added colour background instead of text for rainbow folders options (makes rainbow folders in this theme more consistent with those in other themes)
- Add smooth cursor effect, configurable via style settings
  - duration, timing function, minimum width
- Fixed Vim Mode Status to use `var(--font-ui-medium)` by default

### Version 0.4.4 Consistencies Update

- Fix footnote alignment
- Fix bullet list alignment
- Changed default highlight colour
- ASCII checkboxes now uses the same colour gradient as rainbow folders in this theme
- Added more ASCII checkbox options (see the web demo)
- Text wrap to newline when file explorer file/folder title overflows
- Add Style Settings option for configuring suggestion item padding
- Added support for Omnisearch plugin
