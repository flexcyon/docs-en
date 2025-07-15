---
title: Números de línea
icon: material/line-scan
---

Configurar números de línea y números de línea relativos

Formatos aceptados: HEX, %, x.y

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

CSSVariable(s) targeted:`var(--flexcyon-enable-rel-nums)`
Default:false(de clase)

### Relative and normal line numbers on different lines

CSSVariable(s) targeted:`var(--flexcyon-no-num-with-relative)`
Default:false

### Only display relative line numbers

CSSVariable(s) targeted:`var(--flexcyon-relative-num-only)`
Default:false

### Configure Relative Line Number Style

CSSVariable(s) targeted:`var(--flexcyon-roman-rel-nums)`,
,
`var(--flexcyon-roman-greek-nums), var(--flexcyon-roman-chinese-nums)`
Default: ninguno (clase toggle)
Opciones:

- Roman
- Griego
- Chino

### Replace active line number with string
Personalizar el número de línea activa con su propia cadena, predeterminado a "- título"

CSSVariable(s) targeted:`var(--flexcyon-repl-active-line-num-str)`
Default:false(de clase)

### Replaced active line number string value
CSSVariable(s) targeted: `var(--flexcyon-epl-active-line-str)

Predeterminado: "- Conf"
