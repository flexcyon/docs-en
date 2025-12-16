---
title: Callouts
icon: material/information-slab-box-outline
tags:
  - callouts
---

配置标注样式。

接受的格式: px, rem, em, s

## 导航

```md
Style Settings
|-- ...
|-- Flexcyon Style Settings
| |-- Editor
| | |-- ...
| | |-- Callouts
| | |-- ...
| |-- ...
|-- ...
```

## 配置选项

### 标注图标右侧填充

目标 CSS 变量: `var(--flexcyon-callout-icon-right-padding)`

默认: 4 (px)

### 第一个代码块边距顶部

目标 CSS 变量: `var(--flexcyon-callout-first-codeblock-margin-top)`

默认: 1 (rem)

### 标注元数据背景不透明度

目标 CSS 变量: `var(--flexcyon-callout-bg-opacity)`

默认: 20%

<span style="opacity: 20%">Sample Background Opacity</span>

### 标注垂直边距

目标 CSS 变量: `var(--flexcyon-callout-vertical-margin)`

默认: 1 (em)

### 标注垂直填充

目标 CSS 变量: `var(--flexcyon-callout-vertical-padding)`

默认: 12 (px)

### 标注水平填充

目标 CSS 变量: `var(--flexcyon-callout-horiz-padding)`

默认: 24 (px)

### 标注文本边框半径

目标 CSS 变量: `var(--callout-radius)`

默认: 2 (px)

### 标注添加了边框半径

目标 CSS 变量: `var(--flexcyon-callout-radix)`

默认: 16 (px)

### 选择 Callout 样式

目标 CSS 类: `.flexcyon-tui-callouts, .flexcyon-plain-callouts, .flexcyon-vert-callouts`

默认: none (类选项)

选项:

- TUI (文本用户界面) Callouts
- Plain (简化) Callouts
- Vertical (垂直) Callouts

### 不显示 TUI Callout 的图标

目标 CSS 类: `.flexcyon-tui-no-icons`

默认: false (类切换)

---

### 抽认卡标注

配置[抽认卡标注](../../../Callout-Metadata/flashcard.md)。

#### 抽认卡标注宽度

目标 CSS 变量: `var(--flexcyon-callouts-flashcard-width)`

默认: 250 (px)

#### 抽认卡标注高度

目标 CSS 变量: `var(--flexcyon-callouts-flashcard-height)`

默认: 250 (px)

#### 抽认卡标注动画持续时间

目标 CSS 变量: `var(--flexcyon-callout-flashcard-animation-duration)`

默认: 0.5s

---

### 弹出式标注

配置[弹出式标注](../../../Callout-Metadata/popup.md)。

#### 弹出式标注动画持续时间

目标 CSS 变量: `var(--flexcyon-callout-pop-animation-duration)`

默认: 0.2s
