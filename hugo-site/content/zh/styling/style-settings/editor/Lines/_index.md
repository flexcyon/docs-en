---
title: 行
---

配置行号, 相对行号和活动行.

接受的格式: HEX, %, x.y

## 导航

```md
Style Settings
|-- flexcyon://Editor
|   |-- Lines
```

## 配置选项
### 突出显示活动行

目标 CSS 变量: `var(--flexcyon-highlight-active-line)`

默认: false (类切换)

### 发光活性线

目标 CSS 变量: `var(--flexcyon-glow-active-line)`

默认: false (类切换)

### 发光活性线 x 偏移

目标 CSS 变量: `var(--flexcyon-glow-active-offset-x)`

默认: 1 (px)

### 发光活性线 y 偏移

目标 CSS 变量: `var(--flexcyon-glow-active-offset-y)`

默认: 1 (px)

### 发光活动线模糊强度

目标 CSS 变量: `var(--flexcyon-glow-active-blur-radius)`

默认: 2 (px)

### 发光活动文本颜色

目标 CSS 变量: `var(--flexcyon-glow-active-color)`

默认: Normal text (默认文本颜色) (变量选项)

选项:

* Cyan (青色)
* Blue (蓝色)
* Purple (紫色)
* Pink (粉红色)
* Red (红色)
* Orange (橙色)
* Yellow (黄色)
* Green (绿色)
* Accent (强调色)
* Normal text (默认文本颜色)

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
