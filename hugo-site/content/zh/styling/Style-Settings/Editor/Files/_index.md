---
title: Files
icon: material/file-cog
---

配置文件树和文件夹样式。

## 导航

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

## 配置选项

### 启用变暗的文件扩展名

目标 CSS 变量: `var(--flexcyon-file-exp-dimmed-file-exts-enabled)`

默认: true (类切换)


### 变暗的文件扩展名字体大小

目标 CSS 变量: `var(--flexcyon-exp-dimmed-nav-size)`

默认: 13.3623 (px)

### 启用现用文件指示器

目标 CSS 类: `var(--flexcyon-enable-active-file-indicator)`

默认: false (类切换)

### 现用文件指示器符值

目标 CSS 变量: `var(--flexcyon-active-indicator)`

默认: ">> "

### 启用垂直导航样式

目标 CSS 变量: `var(--flexcyon-vertical-nav)`

默认: false (类切换)

### 文件夹样式

目标 CSS 类: `.flexcyon-rainbow-folders, .flexcyon-alt-folder-style, .flexcyon-md-file-tree-style`

默认: none (类选项)

选项:

- Rainbow folders (彩虹)
- Alternate folder style (备用)
- Markdown file tree style (Markdown 文件树)

### 彩虹文件夹彩色背景代替彩色文本

目标 CSS 类: `var(--flexcyon-is-bg-rainbow)`

默认: false

### 启用极简文件树

目标 CSS 变量: `var(--flexcyon-minimalist-tree)`

默认: false (类切换)

### 垂直树项目填充

目标 CSS 类: `var(--flexcyon-tree-item-verti-padding)`

默认: 2 (px)

### 水平树项目填充

目标 CSS 类: `var(--flexcyon-tree-item-horiz-padding)`

默认: 10 (px)

### 换行长文件名

将长文件名换行, 而不是省略末尾部分。

目标 CSS 变量: `var(--flexcyon-wrap-long-filenames)`

默认: true (类切换)
