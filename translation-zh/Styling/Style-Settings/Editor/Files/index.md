---
title: 文件
icon: material/file-cog
---

配置文件树和文件夹样式。

## Navigation

```md
Style Settings
|-- ...
|-- Flexcyon Style Settings
| |-- Editor
| | |-- ...
| | |-- Files
| | |-- ...
| |-- ...
|-- ...
```

## Configuration Options

### Enable dimmed file extensions in file explorer

目标CSS变量:`var(--flexcyon-file-exp-dimmed-file-exts-enabled)`

默认 :true(类切换)

### Select folder style

CSS类目标:`.flexcyon-rainbow-folders, .flexcyon-alt-folder-style, .flexcyon-md-file-tree-style`

默认: 无( 类选择)

选项 :

- 彩虹文件夹
- 替代文件夹样式
- Markdown 文件树样式

### Colour background instead of text for rainbow folders

CSS类目标:`var(--flexcyon-is-bg-rainbow)`

默认 :false

### Enable minimalist trees

目标CSS变量:`var(--flexcyon-minimalist-tree)`

默认 :false(类切换)

### Vertical Tree Item Padding

CSS类目标:`var(--flexcyon-tree-item-verti-padding)`

默认: 0.75 (px)

### Horizontal Tree Item Padding

CSS类目标:`var(--flexcyon-tree-item-horiz-padding)`

默认: 8 (px)
