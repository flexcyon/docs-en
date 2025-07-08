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

## Opciones de configuración

### Enable Relative Line Numbers

CSSVariable(s) targeted:`var(--flexcyon-enable-rel-nums)`
Default:false(de clase)

## Números relativos y normales de línea en diferentes líneas

CSSVariable(s) targeted:`var(--flexcyon-no-num-with-relative)`
Default:false

### Sólo muestra números de línea relativos

CSSVariable(s) targeted:`var(--flexcyon-relative-num-only)`
Default:false

### Número de línea relativa configura

CSSVariable(s) targeted:`var(--flexcyon-roman-rel-nums)`,
,
`var(--flexcyon-roman-greek-nums), var(--flexcyon-roman-chinese-nums)`
Default: ninguno (clase toggle)
Opciones:

- Roman
- Griego
- Chino

### Reemplazar el número de línea activa con cadena
Personalizar el número de línea activa con su propia cadena, predeterminado a "- título"

CSSVariable(s) targeted:`var(--flexcyon-repl-active-line-num-str)`
Default:false(de clase)

### Valor de cadena de números activos reemplazado
CSSVariable(s) targeted: `var(--flexcyon-epl-active-line-str)

Predeterminado: "- Conf"
