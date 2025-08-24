---
title: Prompts
icon: material/text-box
---

配置命令提示符, 快速切换器等提示。

接受的格式: px, vw, vh

## 导航

```md
Style Settings
|-- ...
|-- Flexcyon Style Settings
| |-- Editor
| | |-- ...
| | |-- Workspace
| | | |-- ...
| | | |-- Prompts
| | | |-- ...
| | |-- ...
| |-- ...
|-- ...
```

## 配置选项

### 提示宽度

目标 CSS 变量: `var(--prompt-width)`

默认: 700 (px)

### 提示最高宽度

目标 CSS 变量: `var(--prompt-max-width)`

默认: 80 (vw)

### 提示最大高度

目标 CSS 变量: `var(--prompt-max-height)`

默认: 70 (vh)

### 提示对齐

目标 CSS 类: `.flexcyon-prompt-align-bottom-left,
.flexcyon-prompt-align-bottom-center, .flexcyon-prompt-align-center-left,
.flexcyon-prompt-align-top-left, .flexcyon-prompt-align-top-center`

默认: none (类选项)

选项:

- Top left (左上角)
- Top center (顶部中心)
- Center left (左部中心)
- Bottom left (左下角)
- Bottom center (底部中心)

### 建议项垂直填充

目标 CSS 变量: `var(--flexcyon-suggestion-verti-padding)`

默认: 8 (px)

### 建议项水平填充

目标 CSS 变量: `var(--flexcyon-suggestion-horiz-padding)`

默认: 12 (px)
