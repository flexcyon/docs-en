---
title: Line Numbers
icon: material/line-scan
---

Configure line numbers and relative line numbers

Accepted formats: HEX, %, x.y

## Navigation

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

## Configuration Options

### Enable Relative Line Numbers

CSS Variable(s) targeted: `var(--flexcyon-enable-rel-nums)`

Default: false (class toggle)

### Relative and normal line numbers on different lines

CSS Variable(s) targeted: `var(--flexcyon-no-num-with-relative)`

Default: false

### Only display relative line numbers

CSS Variable(s) targeted: `var(--flexcyon-relative-num-only)`

Default: false

### Configure Relative Line Number Style

CSS Variable(s) targeted: `var(--flexcyon-roman-rel-nums)`,
`var(--flexcyon-roman-greek-nums), var(--flexcyon-roman-chinese-nums)`

Default: none (class toggle)
Options:

- Roman
- Greek
- Chinese

### Replace active line number with string

Customise the active line number with your own string, defaults to "->"

CSS Variable(s) targeted: `var(--flexcyon-repl-active-line-num-str)`

Default: false (class toggle)

### Replaced active line number string value

CSS Variable(s) targeted: `var(--flexcyon-repl-active-line-str)

Default: "->"
