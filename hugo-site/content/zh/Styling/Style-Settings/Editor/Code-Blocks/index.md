---
title: Code Blocks
icon: material/format-color-highlight
---

在主题中配置代码块

接受的格式: px

## 导航

```md
Style Settings
|-- ...
|-- Flexcyon Style Settings
| |-- Editor
| | |-- ...
| | |-- Code Blocks
| | |-- ...
| |-- ...
|-- ...
```

## 配置选项

### Flexcyon 语法高亮显示模式

目标 CSS 类: `.flexcyon-syntax-catppuccin,
.flexcyon-syntax-lego, .flexcyon-syntax-monochrome`

默认: none (类选项)
选项:

- Catppuccin
- Lego (乐高)
- Monochrome (单色)

### 关于代码块文件扩展名

自定义代码块文件扩展名, 仅在 Live Preview 模式下显示。

### 使代码块文件扩展名小写

目标 CSS 类: `.flexcyon-codeblock-fmt-ext`

默认: false (类切换)

### 在代码块扩展之前添加前缀

目标 CSS 类: `.flexcyon-codeblock-prefix-ext`

默认: false (类切换)

### 在代码块扩展之前自定义前缀

目标 CSS 变量: `var(--flexcyon-codeblock-ext-prefix)`

默认: "."

### 代码块文件扩展名字重

目标 CSS 变量: `var(--flexcyon-code-file-ext-font-w)`

默认: 500
