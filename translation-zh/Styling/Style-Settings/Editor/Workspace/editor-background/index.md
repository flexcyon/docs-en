---
title: 背景编辑器
icon: material/layers-edit
---

Configure the background in the editor
Accepted formats: px, deg

## Navigation

```md
Style Settings
|-- ...
|-- Flexcyon Style Settings
|   |-- Editor
|   |   |-- ...
|   |   |-- Workspace
|   |   |   |-- ...
|   |   |   |-- Editor Background
|   |   |   |-- ...
|   |   |-- ...
|   |-- ...
|-- ...
```

## Configuration Options

### Select Background Type

CSS类目标:`.flexcyon-editor-grid, .flexcyon-editor-dots, .flexcyon-editor-rhombus`

默认: 无( 类选择)
选项 :

- Grid Background
- Dotted Background
- Rhombus Background

### Rotation value for grid and rhombus background

目标CSS变量:`var(--flexcyon-editor-bg-rotation)`

Default: 0 (deg)

### Width between each dot/line for grid/dotted background

目标CSS变量:`var(--flexcyon-editor-bg-width)`

默认: 15 (px)

### Size of dots for dotted background

目标CSS变量:`var(--flexcyon-editor-dot-size)`

默认: 2 (px)

