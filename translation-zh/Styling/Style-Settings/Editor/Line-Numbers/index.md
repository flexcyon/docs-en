---
title: 行号
icon: material/line-scan
---

Configure line numbers and relative line numbers

接受格式:HEX,%,x.y

## Navigation

```md
Style Settings
|-- ...
|-- Flexcyon Style Settings
|   |-- Editor
|   |   |-- ...
|   |   |-- Line Numbers
|   |   |-- ...
|   |-- ...
|-- ...
```

## Configuration Options

### Enable Relative Line Numbers

目标CSS变量:`var(--flexcyon-enable-rel-nums)`

默认 :false(类切换)

### Relative and normal line numbers on different lines

目标CSS变量:`var(--flexcyon-no-num-with-relative)`

默认 :false

### Only display relative line numbers

目标CSS变量:`var(--flexcyon-relative-num-only)`

默认 :false

### Configure Relative Line Number Style

目标CSS变量:`var(--flexcyon-roman-rel-nums)`, (中文).
,
`var(--flexcyon-roman-greek-nums), var(--flexcyon-roman-chinese-nums)`

Default: none (class toggle)
选项 :

- Roman
- Greek
- Chinese

### Active Line Numbers inherits Relative Line Number Style

目标CSS变量:`var(--flexcyon-active-inherits-rel-num)`

默认 :false
> Do note that I have to get creative for Greek and Roman as they do not
> exactly have letters or numbers before I or alpha.
