---
title: Line Numbers
icon: material/line-scan
---

配置行号和相对行号。

接受的格式: HEX, %, x.y

## 导航

```md
Style Settings
|-- ...
|-- Flexcyon Style Settings
| |-- Editor
| | |-- ...
| | |-- Line Numbers
| | |-- ...
| |-- ...
|-- ...
```

## 配置选项
### 突出显示活动行

目标 CSS 变量: `var(--flexcyon-highlight-active-line)`

默认: false (类切换)

### 启用相对行号

目标 CSS 变量: `var(--flexcyon-enable-rel-nums)`

默认: false (类切换)

### 相对线号和默认线号在不同的线上

目标 CSS 变量: `var(--flexcyon-no-num-with-relative)`

默认: false

### 仅显示相对行号

目标 CSS 变量: `var(--flexcyon-relative-num-only)`

默认: false

### 配置相对行号样式

目标 CSS 变量: `var(--flexcyon-roman-rel-nums)`,
`var(--flexcyon-roman-greek-nums), var(--flexcyon-roman-chinese-nums)`

默认: none (类切换)

Options:

- Roman (罗马语)
- Greek (希腊语)
- Chinese (中文)

### 用字符串替换活动行号

使用您自己的字符串自定义活动行号, 默认为 "->"

目标 CSS 变量: `var(--flexcyon-repl-active-line-num-str)`

默认: false (类切换)

### 替换活动行号字符串

目标 CSS 变量: `var(--flexcyon-repl-active-line-str)

默认: "->"

### 替换活动行号字符串字距离

目标 CSS 变量: `var(--flexcyon-repl-active-str-space)`

默认: 0 (px)
