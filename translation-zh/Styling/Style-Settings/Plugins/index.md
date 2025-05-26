---
title: 。icon: material/hexagon-outline
---

For configuration of officially supported plugins

Accepted formats: HEX, rem, x.y, %

## Navigation

```md
Style Settings
|-- ...
|-- Flexcyon Style Settings
|   |-- ...
|   |-- Plugins
|   |-- ...
```

## Configuration Options

### Alternate file tree

#### Folders font size

。CSS。:`var(--oz-fta-folder-font-size)`

Default: 0.925 (rem)

<span style="font-size: 0.925rem"
>Sample Alternate file tree Folders font size</span>

#### Folders font color

。CSS。:`var(--oz-fta-folder-pane-file-name-color)`

。( 。) :
<span class="col-sqr" style="background-color: #080808"
></span
>#080808 (。).

。( 。) :
<span class="col-sqr" style="background-color: #d3d5d3"
></span
>#d3d5d3 (。:

#### Active folder color

CSS Variables(s) targeted: `var(--oz-fta-all-panes-active-text-color)`

。( 。) :
<span class="col-sqr" style="background-color: #080808"
></span
>#080808 (。).

。( 。) :
<span class="col-sqr" style="background-color: #d3d5d3"
></span
>#d3d5d3 (。:

#### Files font size

。CSS。:`var(--oz-fta-file-font-size)`

Default: 0.9 (rem)

<span style="font-size: 0.9rem"
>Sample Alternate file tree Files font size</san>

#### Files font color

。CSS。:`var(--oz-fta-file-pane-file-name-color)`

。:
<span class="col-sqr" style="background-color: #6f768599"
></span
>#6f768599 (。).

#### Disable folder icons

。CSS。:`var(--flexcyon-oz-folder-icons-disabled)`

。:false(。)

#### Disable file tree header

。CSS。:`var(--flexcyon-oz-file-tree-header-disabled)`

。:false(。)

#### Enable Alternate folder count

。CSS。:`var(--flexcyon-oz-alternate-folder-count)`

。:false(。)

#### Enabled dimmed file extensions in file tree

。CSS。:`var(--flexcyon-oz-dimmed-file-exts-enabled)`

。:true(。)

 

### Full Calendar

Accepted formats: x.y, %

#### Opacity of dimmed full calendar items

。CSS。:`var(--flexcyon-fc-dimmed-items-opacity)`

Default: 0.89

<span style="opacity: 0.89"
>Sample opacity of dimmed full calendar items</span>

 

### Dataview

。: px

#### Horizontal padding of dataview error messages

。CSS。:`var(--flexcyon-dataview-horizontal-padding)`

。: 8 (px)

 

### Canvas

Defines styles for the core Canvas plugin.

Accepted formats: px, RGB

#### Blur inactive Canvas nodes

。CSS。:`var(--flexcyon-canvas-blur-inactive-nodes)`

。:false(。)

#### Blur intensity for inactive nodes

Used with the previous setting to set the blur intensity of inactive canvas nodes
and all arrows/edges.

。CSS。:`var(--flexcyon-canvas-blur-intensity)`

Default: 1 (px)

#### Canvas card menu alignment

Configure the alignment of the canvas card menu.

CSS Classe(s) targeted: `.flexcyon-canvas-menu-bottom-left,
.flexcyon-canvas-menu-bottom-right, .flexcyon-canvas-menu-top-center,
.flexcyon-canvas-menu-top-left, .flexcyon-canvas-menu-top-right,
.flexcyon-canvas-menu-lcenter-center, .flexcyon-canvas-menu-lcenter-top,
.flexcyon-canvas-menu-lcenter-bottom, .flexcyon-canvas-menu-rcenter-center, (。).
,
.flexcyon-canvas-menu-rcenter-top, .flexcyon-canvas-menu-rcenter-bottom, .flexcyon-canvas-menu-recenter-align`

。: 无( 。)

。:

-。- Bottom right

- 。center

- 。- Top right

- Left aligned center

- Left aligned top

- Left aligned bottom

- Right aligned center

- Right aligned top

- Right aligned bottom

- 。center align

