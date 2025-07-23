---
title: Version 0.6.x
icon: material/numeric-6-box-outline
---

### 0.6.0 Golden Update
- Reduce opacity for enclosing formatting symbols like code blocks and maths blocks to be more consistent with existing styling
- UI font sizes inherits from the Golden Ratio as well
- Improved ASCII check boxes
- Added Clip Path Checkboxes which can be toggled separately
- Improved default Mermaid Diagram Styling, thanks to `@harr` on the Obsidian Members' `Group`
- Active line numbers are now improved to use the accent colour with a higher opacity
- Modified default font size of Vim Mode Status and Status Bar Text to inherit from the Golden Ratio
- Improved community item effects styling option
- Changed default padding values for tree items. Affects file explorer, outline, alternate file tree etc. Updated its Style Settings configuration.
- Improved Animations
	- Changed default animation duration to `0.3s`
	- Changed default slide amount for sliding related animations to inherit from the Golden Ratio
	- Added scale up animation option
	- Animations now apply to more UI elements and feel more snappy
- Vim Smooth Cursor now has its default transition duration decreased to `42.5ms` and its default timing function changed to `ease-in`.
- Fixed sidebar toggle icon alignment thanks to `@F4doli` for noticing
- You can now further customise horizontal rules by adding your own custom strings
	- Configuration options like horizontal rule colour, left percentage, horizontal padding, font size.
	- Move Disable horizontal rules in reading mode to the new Style Settings section
