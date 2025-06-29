---
title: 行号
icon: material/line-scan
---

配置行号和相对行号

接受格式:HEX百分比,x.y

□ 导航

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

□ 配置选项

QQ 启用相对行号

CSS目标变量:`var(--flexcyon-enable-rel-nums)`
默认 :false(类切换)

* 不同线路的相对和正常行号

CSS目标变量:`var(--flexcyon-no-num-with-relative)`
默认 :false

### 只显示相对行号

CSS目标变量:`var(--flexcyon-relative-num-only)`
默认 :false

### 配置相对行号样式

CSS目标变量:`var(--flexcyon-roman-rel-nums)`, (中文).
,
`var(--flexcyon-roman-greek-nums), var(--flexcyon-roman-chinese-nums)`
默认: 无( 类切换)
选项 :

-罗曼语
-希腊语
- 中国语

### 将活动行号替换为字符串
用自己的字符串自定义活动行号,默认为“-
>”

CSS目标变量:`var(--flexcyon-repl-active-line-num-str)`
默认 :false(类切换)

### 已替换活动行号字符串值
CSS目标变量:`var(-弹性-活性-线-str)

默认: "-
>"
