---
title: 行号
icon: material/line-scan
---

配置行号和相对行号

接受格式:HEX百分比,x.y

## Navigation

```md
Style Settings
|-- 。
|-- Flexcyon Style Settings
|   |-- Editor
|   |   |-- 。
|   |   |-- Line Numbers
|   |   |-- 。
|   |-- 。
|-- 。
```

## Configuration Options

### Enable Relative Line Numbers

CSS目标变量:`var(--flexcyon-enable-rel-nums)`
默认 :false(类切换)

### Relative and normal line numbers on different lines

CSS目标变量:`var(--flexcyon-no-num-with-relative)`
默认 :false

### Only display relative line numbers

CSS目标变量:`var(--flexcyon-relative-num-only)`
默认 :false

### Configure Relative Line Number Style

CSS目标变量:`var(--flexcyon-roman-rel-nums)`, (中文).
,
`var(--flexcyon-roman-greek-nums), var(--flexcyon-roman-chinese-nums)`
默认: 无( 类切换)
选项 :

-罗曼语
-希腊语
- 中国语

### Replace active line number with string
用自己的字符串自定义活动行号,默认为“-
>”

CSS目标变量:`var(--flexcyon-repl-active-line-num-str)`
默认 :false(类切换)

### Replaced active line number string value
CSS目标变量:`var(-弹性-活性-线-str)

默认: "-
>"
