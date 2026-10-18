---
title: 编辑背景
---

在编辑器中配置背景. 

接受的格式: px, deg

## 导航

```md
Style Settings
|-- flexcyon://Editor
|   |-- Editor Background
```

## 配置选项

### 选择背景类型

目标 CSS 类: `.flexcyon-editor-grid, .flexcyon-editor-dots, .flexcyon-editor-rhombus`

默认: none (类选项)

选项:

- Grid Background (网格背景)
- Dotted Background (虚线背景)
- Rhombus Background (菱形背景)
- Circle Background (波尔卡圆点背景)
- Chess Background (棋盘背景)

### 网格和菱形背景的旋转值

目标 CSS 变量: `var(--flexcyon-editor-bg-rotation)`

默认: 0 (deg)

### 虚线背景的每个点的宽度

目标 CSS 变量: `var(--flexcyon-editor-bg-width)`

默认: 15 (px)

### 虚线背景中点的大小

目标 CSS 变量: `var(--flexcyon-editor-dot-size)`

默认: 2.5 (px)

### 编辑器背景宽度 2

> 对于 "波尔卡圆点" 和 "棋盘" 背景

目标 CSS 变量: `var(--flexcyon-editor-bg-width-2)`

默认: 40 (px)

### 虚线背景中点的大小 2

> 对于 "波尔卡圆点" 和 "棋盘" 背景

目标 CSS 变量: `var(--flexcyon-editor-dot-size-2)`

默认: 6 (px)
