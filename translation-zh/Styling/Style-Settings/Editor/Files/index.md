---
title: 文件
icon: material/file-cog
---

配置文件树和文件夹样式。

□ 导航

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

□ 配置选项

### 在文件探索器中启用 dimmed 文件扩展名

CSS目标变量:`var(--flexcyon-file-exp-dimmed-file-exts-enabled)`
默认 :true(类切换)

### 选择文件夹样式

CSS目标类别:`.flexcyon-rainbow-folders, .flexcyon-alt-folder-style, .flexcyon-md-file-tree-style`
默认: 无( 类选择)

选项 :

- 彩虹文件夹
- 替代文件夹样式
- Markdown 文件树样式

### 彩虹文件夹的颜色背景而非文本

CSS目标类别:`var(--flexcyon-is-bg-rainbow)`
默认 :false

启用最小化树

CSS目标变量:`var(--flexcyon-minimalist-tree)`
默认 :false(类切换)

垂直树条

CSS目标类别:`var(--flexcyon-tree-item-verti-padding)`
默认 :1.5 (px) (中文(简体) ).

水平树项

CSS目标类别:`var(--flexcyon-tree-item-horiz-padding)`
默认: 12 (px)

QQ 环绕长文件名称
将长文件名保存到新行, 而不是省略结尾部分 。
.

CSS目标变量:`var(--flexcyon-wrap-long-filenames)`
默认 :true(类切换)
