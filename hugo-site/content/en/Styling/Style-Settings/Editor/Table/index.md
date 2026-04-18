---
title: Table
icon: material/table-cog
---

Defines colour for table borders, and the width of tables in reading mode.

Accepted formats: HEX, %, x.y

## Navigation

```md
Style Settings
|-- ...
|-- Flexcyon Style Settings
|   |-- Editor
|   |   |-- ...
|   |   |-- Table
|   |   |-- ...
|   |-- ...
|-- ...
```

## Configuration Options

### Table border color

CSS Variable(s) targeted: `var(--table-border-color)`

Default:
<span class="col-sqr" style="background-color: #6f768566"></span> #6f768566

### Width of table in reading mode

CSS Variable(s) targeted: `var(--flexcyon-table-reading-mode-width)`

Default: 100%

### Table header font size

CSS Variable(s) targeted: `var(--table-header-size)`

Default: Large (UI Font size)

Options:

- Smaller (UI Font size)
- Small (UI Font size)
- Medium (UI Font size)
- Large (UI Font size)

<span style="font-size: large;">Sample table header</span>

### Table Heading Vertical Padding
CSS Variable(s) targeted: `var(--flexcyon-th-verti-padding)`

Default: 5 (px)

### Table Heading Horizontal Padding
CSS Variable(s) targeted: `var(--flexcyon-th-horiz-padding)`

Default: 10 (px)

### Table Heading Live Preview scaling

Proportion to scale Live Preview table heading padding when compared to Reading mode.

CSS Variable(s) targeted: `var(--flexcyon-th-live-pad-scale)`

Default: 0.2

### Table Cell font size

CSS Variable(s) targeted: `var(--table-text-size)`

Default: Medium (UI Font size)

Options:

- Smaller (UI Font size)
- Small (UI Font size)
- Medium (UI Font size)
- Large (UI Font size)

<span style="font-size: large;">Sample table header</span>

### Table Cell Vertical Padding
CSS Variable(s) targeted: `var(--flexcyon-td-verti-padding)`

Default: 5 (px)

### Table Cell Horizontal Padding
CSS Variable(s) targeted: `var(--flexcyon-td-horiz-padding)`

Default: 10 (px)

### Table Cell Live Preview Scaling

Proportion to scale Live Preview table cell padding when compared to Reading mode.

CSS Variable(s) targeted: `var(--flexcyon-td-live-pad-scale)`

Default: 0.2

> More specifically the scaling of padding compared to the specified values
