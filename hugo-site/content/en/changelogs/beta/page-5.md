---
title: Version 0.5.x
icon: material/numeric-5
---

### Version 0.5.0 Revamp Update
- Added about and help section in Style Settings
- Omnisearch highlighting is now more consistent with the default search highlight
- Fix Double quote ASCII checkbox having a background colour
- Added support for Various Complements Plugin with some configuration options
	- Horizontal and Vertical Suggestion Padding
	- Compact Suggestion Mode
- Increased default horizontal tree item padding to 12px
- Increased default vertical tree item padding to 1.25px
- Applied tree item padding to File Tree Alternative
- Make line wrap for long file names toggleable. Apply line wrap default to File Tree Alternative items as well (including titles and all)
- Replaced "active line number inherits relative line number style" with "replace active line number with string". Defaults to "`->`". Can be configured with Style Settings
- Minor tweaks to Graph View controls. Paddings configurable via Style Settings
- Increased default ribbon width to 48px, added Style Settings option to configure it.
- Aligned collapse icon with text like folder titles etc
- Highlighted text now has some border radius and padding, and increased font weight
- Dimmed enclosing formatting symbols like `*` in *test* to look **better** while editing
- Minor tweaks to Style Settings menu
- Vim smooth cursor default transition duration reduced to `70ms`
- File Tree Alternative folder and file items now inherit from UI font size, file count tags are now bigger, and the folder view should look better.
- Dimmed file extensions now inherit from UI font size
- Icons have increased padding
- You can now configure the view header breadcrumb max width (scales with viewport width)
- Add style Setting option for highlighted text border radius and padding.
- Increase tab header icons padding
- Add font-family callout metadata (based on monospace, text and interface fonts)
- Modified default UI font sizes
- Option to Change default list style for numbered lists in reading mode (too many options provided)
- Split quote text and quote attribution (name or source) into different CSS Variables

### 0.5.1 Debug Update
- Fixed highlighted search result visual bug, thanks to `@Moy` on the Obsidian Members' Group
- Default message on UI element hover is improved for light mode
- Fix ASCII checkbox alignment once again
- Vim mode status now uses your interface font
- Add change opacity of block ID labels, defaults to 0.55
- Default heading font sizes are now changed to inherit from the Golden Ratio
- Added remove Omnisearch icons and Omnisearch result body left margin options
- Added syntax highlighting modes: Catppuccin, Lego, Monochrome
- Style Setting option to disable horizontal rules in reading mode, hr colours more consistent across editing and reading modes
