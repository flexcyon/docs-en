---
icon: material/script-text
title: Changelogs
---

#### Note

The changelogs show versions in order of most recent to least recent.
Or, if you prefer the changelogs in chronological order, you can use
the sidebar or hamburger menu to view the relevant sub-pages.

---
## Version 1.3.x
### 1.3.0 Animations Update
#### Features
- You can now use a different set of animations between notes and other parts of the UI like modals.
- Added fade in animation which is set as the default over the old slide left to right for Flex Max mode
- Added Style Settings options for initial opacity in animations and initial scaling for scale up animation
- Added fixes for Banner snippet support in the theme
	- There is now a visual indicator in line gutters to help locate where the banner image is defined in the current note
	- Due to the Obsidian editor's lazy rendering, it is recommended to specify the banner image source near the top of the file
- Added option to set modal background darken intensity
- Added ASCII art scale factor option
	- It is recommended to write a CSS snippet to extensively customise your own ASCII art
- Added alternate link styling (Willemstad inspired)
- Added error handling for Bases when no link is found for file
- Added letter spacing option for replace active line number with custom string setting
- Add style setting to toggle if TUI callouts should have their icons displayed none by default (defaults to false)
- Add font size callouts, inherits UI font sizes like smaller, small, medium or large.
- Added opacity callouts, lets you set the opacity of callout title, content or both at once.
- Added view header options to specify view header title padding in Angled and Powerlevel10k layouts
- Added Opacity callouts in increments of 0.05 
- Core slides plugin now has slide numbers in presentation view (up to 99 slides)
- ASCII art now appears in core slides plugin pause presentation mode (press b to trigger)
- Added Stylised Pinned Icons
- Added Style Settings plugin check
- Added toggle display properties title

#### Changes
- Updated styling of backlinks and outgoing links view
- Slightly tweaked Alternate File Tree create and delete dialog titles
- Improved existing styling of mermaid diagrams
- Improved sidebar background code
- Improved ASCII art code, empty state actions are now disabled by default.
- Deprecate web demo since does not translate the theme's aesthetics well

#### Fixes
- Fixed animations, they now apply to your notes and sidebar content as well
- Fixed horizontal rule custom string to work in reading mode as well
- Fixed TUI callout appearance. Note that un-collapsing large code snippets like mermaid diagrams in callouts will cause rendering delays. This applies to all callouts, even default ones.
- Fixed display operating system and screen dimensions to work without tab title bar enabled
	- Split tabs and debug related style settings into their own section
- Fixed extended colour palette to properly support all combinations of base colour variables
- Made Bases text alignment consistent
- Core slides plugin is now smoother and more consistent with the theme
- Fixed default ASCII art alignment to make more sense, configurable in Style Settings
- Fixed inline math inside highlight
- Fixed default TUI callout icon not inheriting icon colour
- Fixed default no metadata in reading mode
- Removed left align status bar setting as it was too hardcoded

## Version 1.2.x
### 1.2.1 Settings Update
- Fixed duplicate Style Settings entries, thanks to `@saberzero` on the OMG Discord

### 1.2.0 Retrospect Update
- Fixed File Properties in vertical navigation
- Fixed Right Sidebar Toggle Button disappearing in vertical navigation
- Updated Full Calendar Plugin styling
- Added Style Settings options for tables
- Tweaked some background colours in the theme
- Updated Style Settings and active item background
- Added Style Settings option to set heading text alignment
- Added Styling for Core Slides plugin
- Added Styling for Tasks plugin
- Added option to place workspace ribbon (sidedock icons)
- Added options to place vault switcher at the top, reverse vault switcher and actions
- Added toggleable active line highlight when not in reading mode

## Version 1.1.x

### 1.1.3 Headings Fix
- Fixed broken heading indicator settings
- Fixed heading indicator overlap with collapse icon

### 1.1.2 Vertical Fixes
- Fixed vertical layout not working for specific UI region
- Added more useful error messages to Bases 
	- e.g. when the Base query result is empty (no notes found matching specified criteria), or a specific note property cannot be found for some note
- Added styling for core Web Viewer plugin
- You can now specify a colour for callouts like `vert-orange`, `tui border-purple`, `plain-yellow`. Each corresponds to a specific callout style.
	- Like the callout styles, the metadata providers are mutually exclusive.
	- Whether you write the option in callout metadata or as a custom callout is up to you
- Fixed first iframe padding top in callouts
- Slightly improved performance of sidebar background options

### 1.1.1 Vertical Styling
- Added callout metadata option for setting lucide icon in callouts. When using lucide icon setting, either the entire callout metadata or custom callout section must match the lucide icon value else the icon will not render.
	- E.g. `>[!lucide-git-fork|title-orange]` instead of `>[!note|lucide-git-fork title-orange]` or `>[!title-orange|lucide-git-fork]` (you cannot specify multiple custom callout types, but can modify with callout metadata)
	- Renamed `vertical-ltr` callout metadata to `vert-ltr`
- Added selectable default callout style. Options include TUI, Plain and Vertical. These also have callout metadata and custom callout equivalents.
	- The custom callout and callout metadata options are mutally exclusive but can override the default callout style selected
- Updated community store appearance and community item effects
- Added toggleable vertical navigation style

### 1.1.0 Callouts Update

- Changed (slightly reduced) default line heights in the theme
	- You can configure them to your liking
- Added more callout style setting options
- You can now use any valid lucide icon as a custom callout. It replaces the default icon with the lucide icon you input.
	- This does not have a callout metadata equivalent
- You can now specify all callout metadata as a custom callout. E.g. `>[!|empty]` and `>[!empty]` both do the same thing
- Updated ASCII Icon Set
- You can number your tabs and remove their titles (enabled by default in RTZ mode). You can also toggle it separately.
- Added Experimental TUI callouts and an option to enable them for all callouts
- Added toggleable active file indicator
- Styled core search plugin
- More view header styling for pl10k layout

## Version 1.0.x

### 1.0.2 Fixed Highlighting
- Text highlighting is now fixed
  - Thanks to `weiss-d` on GitHub and `arthur` on the OMG Discord
- Added more Bases styling options

### 1.0.1 Typography Update

- Added experimental Bases style settings
- Modified some Style Settings to use variable-select for better performance. Legacy options are kept for backwards compatibility
- Added an experimental Loading Indicator when Obsidian starts up
- You can now configure the normal text colour, line height, letter and word spacing of text throughout the theme.

### 1.0.0 Update

- Added Style Settings option for changing status bar alignment, hide until hover animation will adapt to the currently selected alignment.
  - Defaults to right alignment when no alignment is selected.
  - Replaced hide until hover with a option for hold until hover as well. Named "hide until trigger"
- Removed horizontal rule custom string left percentage because I learnt how to centre a `<div>` from Willemstad theme author :D
- Added toggleable display of current operating system and screen dimensions.
  - Credits to [this dev](https://dev.to/janeori/css-type-casting-to-numeric-tanatan2-scalars-582j) and [this dev](https://css-tip.com/screen-dimension) and [this dev](https://dev.to/leapcell/get-screen-size-in-pure-css-3kna) for the screen dimensions.
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

---

Beta changelogs can be [found here](./beta/index.md).

I will not be bothering to translate these.
