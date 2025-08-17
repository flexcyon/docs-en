---
icon: material/script-text
title: Changelogs
---

#### Note

The changelogs show versions in order of most recent to least recent.
Or, if you prefer the changelogs in chronological order, you can use
the sidebar or hamburger menu to view the relevant sub-pages.

___
## Version 1.0.x
### 1.0.0 Update (TBC)
- Added Style Settings option for changing status bar alignment, hide until hover animation will adapt to the currently selected alignment. 
	- Defaults to right alignment when no alignment is selected.
	- Replaced hide until hover with a option for hold until hover as well. Named "hide until trigger"
- Removed horizontal rule custom string left percentage because I learnt how to centre a `<div>` from Willemstad theme author :D
- Added toggleable display of current operating system and screen dimensions.
	- Credits to https://dev.to/janeori/css-type-casting-to-numeric-tanatan2-scalars-582j and https://css-tip.com/screen-dimension and https://dev.to/leapcell/get-screen-size-in-pure-css-3kna for the screen dimensions.
- Better default alignment for view header items.
	- Moved view header breadcrumb max width to new View header section 
	- Added toggle-able option to display operating system details and screen dimensions, with configurable paddings
- Moved most Icon related Style Settings into its own section
	- Added toggleable ASCII Icon set
	- Smiley Icons are now disabled by default
	- Added WIP Iconic plugin support, you can toggle if the plugin overrides Smiley and ASCII Icons or not
- Fixed animations, animations now also show up in stacked tabs. You can toggle if they show up in Style Settings containers.
- Moved Modes into its own section, added Flex Max mode thanks to `@orionp` on the Obsidian Members' Group Discord
	- Flex Max mode is enabled by default, and is meant for those who do not know where to start in terms of customisation (opinionated defaults)
	- Some Style Settings that were enabled by default will be disabled by default and handled by Flex Max instead
	- Move the long list of settings it enables by default to the documentation
- Fixed broken letter spacing in `tategaki` and `vertical-ltr` callout metadata.
- Added Style Settings option for Editor Top Margin
- Added customisation options for code block file extensions in Live Preview
 - Improved Chinese translation and documentation organisation
	- Other languages will not be supported as I do not know them and relying too much on machines for translations is a bad thing 

___
Beta changelogs can be [found here](./beta/index.md).

I will not be bothering to translate these.
