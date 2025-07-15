---
title: 文件
icon: material/file-cog
---

配置文件树和文件夹样式。
.

## Navigation

```md
Style Settings
|-- 。
|-- Flexcyon Style Settings
|   |-- Editor
|   |   |-- 。
|   |   |-- Files
|   |   |-- 。
|   |-- 。
|-- 。
```

## Configuration Options

### Enable dimmed file extensions in file explorer

CSS目标变量:`var(--flexcyon-file-exp-dimmed-file-exts-enabled)`
默认 :true(类切换)

### Select folder style

CSS目标类别:`.flexcyon-rainbow-folders, .flexcyon-alt-folder-style, .flexcyon-md-file-tree-style`
默认: 无( 选择类)

选项 :

- 彩虹文件夹
- 替代文件夹样式
- Markdown 文件树样式

### Colour background instead of text for rainbow folders

CSS目标类别:`var(--flexcyon-is-bg-rainbow)`
默认 :false

### Enable minimalist trees

CSS目标变量:`var(--flexcyon-minimalist-tree)`
默认 :false(类切换)

### Vertical Tree Item Padding

CSS目标类别:`var(--flexcyon-tree-item-verti-padding)`
默认: 1. 25 (px)

### Horizontal Tree Item Padding

CSS目标类别:`var(--flexcyon-tree-item-horiz-padding)`
默认: 12 (px)

### Wrap Long File Names
将长文件名保存到新行, 而不是省略结尾部分 。
.

CSS目标变量:`var(--flexcyon-wrap-long-filenames)`
默认 :true(类切换)
