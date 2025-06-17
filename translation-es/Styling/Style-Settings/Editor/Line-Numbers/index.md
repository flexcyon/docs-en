---
title: Números de línea
icon: material/line-scan
---

Configurar números de línea y números de línea relativos

Formatos aceptados: HEX, %, x.y

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

CSS Variable(s) targeted:`var(--flexcyon-enable-rel-nums)`

Default:false(de clase)

### Relative and normal line numbers on different lines

CSS Variable(s) targeted:`var(--flexcyon-no-num-with-relative)`

Default:false

### Only display relative line numbers

CSS Variable(s) targeted:`var(--flexcyon-relative-num-only)`

Default:false

### Configure Relative Line Number Style

CSS Variable(s) targeted:`var(--flexcyon-roman-rel-nums)`,
`var(--flexcyon-roman-greek-nums), var(--flexcyon-roman-chinese-nums)`

Default: ninguno (clase toggle)
Opciones:

- Roman
- Griego
- Chino

### Active Line Numbers inherits Relative Line Number Style

CSS Variable(s) targeted:`var(--flexcyon-active-inherits-rel-num)`

Default:false

> Do note that I have to get creative for Greek and Roman as they do not
> exactly have letters or numbers before I or alpha.
