---
title: 背景编辑器
icon: material/layers-edit
---

在编辑器中配置背景
接受格式: px, deg

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

默认: 无( 选择类)
选项 :
- 网格背景
- 点背景
- 罗姆布斯背景

### Rotation value for grid and rhombus background
目标CSS变量:`var(--flexcyon-editor-bg-rotation)`

默认: 0 (deg)

### Width between each dot/line for grid/dotted background
目标CSS变量:`var(--flexcyon-editor-bg-width)`

默认: 15 (px)

### Size of dots for dotted background
目标CSS变量:`var(--flexcyon-editor-dot-size)`

默认: 2 (px)