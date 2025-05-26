---
title: 插件
icon: material/hexagon-outline
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

目标CSS变量:`var(--oz-fta-folder-font-size)`

Default: 0.925 (rem)

<span style="font-size: 0.925rem"
>Sample Alternate file tree Folders font size</span>

#### Folders font color

目标CSS变量:`var(--oz-fta-folder-pane-file-name-color)`

默认( 灯光模式) :
<span class="col-sqr" style="background-color: #080808"
></span
>#080808 (英语).

默认( 暗模式) :
<span class="col-sqr" style="background-color: #d3d5d3"
></span
>#d3d5d3 (英语:

#### Active folder color

CSS Variables(s) targeted: `var(--oz-fta-all-panes-active-text-color)`

默认( 灯光模式) :
<span class="col-sqr" style="background-color: #080808"
></span
>#080808 (英语).

默认( 暗模式) :
<span class="col-sqr" style="background-color: #d3d5d3"
></span
>#d3d5d3 (英语:

#### Files font size

目标CSS变量:`var(--oz-fta-file-font-size)`

Default: 0.9 (rem)

<span style="font-size: 0.9rem"
>Sample Alternate file tree Files font size</san>

#### Files font color

目标CSS变量:`var(--oz-fta-file-pane-file-name-color)`

默认 :
<span class="col-sqr" style="background-color: #6f768599"
></span
>#6f768599 (英语).

#### Disable folder icons

目标CSS变量:`var(--flexcyon-oz-folder-icons-disabled)`

默认 :false(类切换)

#### Disable file tree header

目标CSS变量:`var(--flexcyon-oz-file-tree-header-disabled)`

默认 :false(类切换)

#### Enable Alternate folder count

目标CSS变量:`var(--flexcyon-oz-alternate-folder-count)`

默认 :false(类切换)

#### Enabled dimmed file extensions in file tree

目标CSS变量:`var(--flexcyon-oz-dimmed-file-exts-enabled)`

默认 :true(类切换)

 

### Full Calendar

Accepted formats: x.y, %

#### Opacity of dimmed full calendar items

目标CSS变量:`var(--flexcyon-fc-dimmed-items-opacity)`

Default: 0.89

<span style="opacity: 0.89"
>Sample opacity of dimmed full calendar items</span>

 

### Dataview

接受格式: px

#### Horizontal padding of dataview error messages

目标CSS变量:`var(--flexcyon-dataview-horizontal-padding)`

默认: 8 (px)

 

### Canvas

Defines styles for the core Canvas plugin.

Accepted formats: px, RGB

#### Blur inactive Canvas nodes

目标CSS变量:`var(--flexcyon-canvas-blur-inactive-nodes)`

默认 :false(类切换)

#### Blur intensity for inactive nodes

Used with the previous setting to set the blur intensity of inactive canvas nodes
and all arrows/edges.

目标CSS变量:`var(--flexcyon-canvas-blur-intensity)`

Default: 1 (px)

#### Canvas card menu alignment

Configure the alignment of the canvas card menu.

CSS类目标:`.flexcyon-canvas-menu-bottom-left,`
`
.flexcyon-canvas-menu-bottom-right, .flexcyon-canvas-menu-top-center,
.flexcyon-canvas-menu-top-left, .flexcyon-canvas-menu-top-right,
.flexcyon-canvas-menu-lcenter-center, .flexcyon-canvas-menu-lcenter-top,
.flexcyon-canvas-menu-lcenter-bottom, .flexcyon-canvas-menu-rcenter-center, (中文).
,
.flexcyon-canvas-menu-rcenter-top, .flexcyon-canvas-menu-rcenter-bottom, .flexcyon-canvas-menu-recenter-align
`

默认: 无( 类选择)

选项 :

-左边

- Bottom right

- 顶部center

- 左边

- Top right

- Left aligned center

- Left aligned top

- Left aligned bottom

- Right aligned center

- Right aligned top

- Right aligned bottom

- 右对齐center align

