---
title: Version 2.x.x
---

## Version 2.0.x

### Version 2.0.1: Patch 1

#### Features
- Added new Style Settings option to dim inactive stacked tab content. Defaults to true.
- Inactive tabs titles are dimmed as part of the theme's design language, as well as being consistent with how regular inactive tab titles are dimmed.

#### Changes
- Improved styling for 1.13 Settings UI.
- Settings search container has adjusted padding.
- `var(--text-on-accent)` now inherits from `var(--color-base-00)` and thus `var(--flexcyon-base-01)`. This makes buttons with accent colour background have better contrast (green/purple with black has better contrast than white text on those backgrounds).
- Improved Spaced Repetition plugin styling.

#### Fixes
- Fixed `var(--slider-track-background)` to use `var(--color-base-25)` instead of transparent.
- Removed redundant code, prevented Highlightr plugin realistic style from having its border radius overriden by the theme's default highlight border radius.
- Improved stylised horizontal rule rendering in Canvas blocks.

### Version 2.0.0 Metamorphosis

#### Features
- Improved Accessibility, you can now adjust contrast, brightness, saturation and colour warmth for theme colours.
- The theme's colours now mostly use `oklch` colour space for more accurate colour rendering
	- Overrode some default hardcoded declarations to use `oklch` colour equivalents
- Style Settings
	- Added prevent accidental unpin, disables unpin via clicking on pin icon. To unpin with this setting enabled, use the right click menu or Ctrl + W.
	- Added Editor Top Margin
	- Added Callout Horizontal Margin
	- Added Disable Vim Block Cursor Blink
	- Added Hide Keychain item in Style Settings
	- Add Style setting option for scrollbar width, moved existing do not show scrollbar in Settings to `flexcyon://Editor > Scrollbar`
- Added support for Banners Reloaded Plugin
- The theme now has it's own Flexcyon Multi-Column implementation (FMCi)
	- Keyword here means both callout type and callout metadata
	- Supports the use of `>[!col]` or `>[!multi-column]` keywords, can be used with `wrap` callout keyword to line wrap column items if they do not fit comfortably in the same column e.g. `>[!col|wrap]` 
	- `wide-0` to `wide-100` keyword supported
	- [See documentation for more details](../../styling/callout-metadata/fmci)
- Added callout keyword alias `capitalize` for applying text capitalisation to text content (previously only the short form "caps" was supported)
- Added support for Lemons Search plugin
	- Added padding to search result previews
	- Uses readable line length
- We now have Korean documentation thanks to `@Onev`'s efforts

#### Changes
- Revamped Style Settings, use the [migration tool](../2.0-migration) to bring over old style settings to flexcyon 2.0.
	- All Opacity related Style settings under `flexcyon://Editor` are consolidated and moved over to its own dedicated section under `flexcyon://Editor > Animations`.
	- Write Style Settings migrator script, change of IDs e.g. `flexcyon` to `flexcyon-a11y` for accessibility related style settings
	- Renamed numerous style setting options to better reflect their purpose
	- "Do not show scrollbar in settings" is now enabled by default and not set to enabled by Flex Max Mode
	- Removed unused base grey tab, base grey token, base grey scroll, base grey scroll hover variables.
	- "Relative and normal line numbers on different lines" defaults to true now
	- Pl10k workspace layout no longer set by Flex Max, "Select Workspace Layout" now defaults to Pl10k workspace layout
	- Make dimmed file extensions and wrap long filenames default to true and no longer set by Flex Max

- Improved ASCII icons, a set of icons complementary to the existing UI. Shoutout to Floodlight on OMG for inspiring this.
- Enforcement of scale system for font size, line height etc. Theme should look more consistent and cohesive.
- Make ASCII and Clip Path checkboxes better conform to alternate checkboxes reference set where possible (or deemed necessary).
	- ASCII checkboxes are now enabled by default, clip path checkboxes are disabled by default
	- Some icon definitions have been remapped for better compatibility, please refer to the updated icon set if your checkboxes are not rendering properly.
	- Please note that ASCII/Clip Path checkboxes are case sensitive
	- Some new icons are added
	- Double quote and single quote ASCII checkboxes no longer use Unicode, whether rendered quotation marks have slight "cursive" will depend your font family
- Improved light and dark theme colours for improved contrast and readability
- You can now specify base callout types that come with Obsidian in callout metadata instead of callout type. E.g. `>[!tip|a]` and `>[!a|tip]` looks the same.
	- Question callouts are now green instead of orange (inherits theme's colours)
	- Important callouts are now purple instead of cyan (inherits theme's colours). They also use `lucide-star` instead of `lucide-fire` for their default icon.
	- Error callouts now use `lucide-circle-alert` instead of `luicde-zap` for their default icon for their default icon.
	- Callout icon alignment is slightly tweaked for better alignment with title text
- Other small QOL tweaks in the theme

#### Fixes
- Mermaid, Canvas styling fixes
- Banner snippet live preview fix
- pl10k Status bar fix
- Novel Word Count plugin compatibility with dimmed file extensions, thanks to `@psolkaiyn` on the OMG Discord server
- Fixed ASCII art rendering and direction. Do update your ASCII art of choice if required.
- "Background for add before empty state title" `linear-gradient` logic now uses the correct direction.
- Attempts to improve performance and clean up parts of the codebase
- Fixed Revert to Pre 1.11 UI
