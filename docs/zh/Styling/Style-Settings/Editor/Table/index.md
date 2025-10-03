---
title: Table
icon: material/table-cog
---

定义表边框的颜色以及读取模式下表的宽度。

接受的格式: HEX, %, x.y

## 导航

```md
Style Settings
|-- ...
|-- Flexcyon Style Settings
| |-- Editor
| | |-- ...
| | |-- Table
| | |-- ...
| |-- ...
|-- ...
```

## 配置选项

### 表格边框颜色

目标 CSS 变量: `var(--table-border-color)`

默认:
<span class="col-sqr" style="background-color: #6f768566"></span> #6f768566

### 表头大小

目标 CSS 变量: `var(--table-header-size)`

默认: large

<span style="font-size: large;">Sample table header</span>

### Reading Mode 下的表格宽度

目标 CSS 变量: `var(--flexcyon-table-reading-mode-width)`

默认: 100%

### 表格单元格垂直填充
目标 CSS 变量: `var(--flexcyon-td-verti-padding)`

默认: 5 (px)

### 表格单元格水平填充
目标 CSS 变量: `var(--flexcyon-td-horiz-padding)`

默认: 10 (px)

### 表格单元格 Live Preview 缩放
目标 CSS 变量: `var(--flexcyon-td-live-pad-scale)`

默认: 0.2

> 更具体地说是与指定值相比, 填充的比例
