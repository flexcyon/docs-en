---
title: Code Blocks
icon: material/format-color-highlight
---

Configure code blocks in the theme

Accepted formats: px

## Navigation

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

## Configuration Options

### Flexcyon Syntax Highlighting Mode

CSS Classe(s) targeted: `.flexcyon-syntax-catppuccin,
.flexcyon-syntax-lego, .flexcyon-syntax-monochrome`

Default: none (class select)
Options:

- Catppuccin
- Lego
- Monochrome

### About Code Block File Extension

Customise the code block file extension, only appears in Live Preview mode.

### Make Code Block File Extension lowercase

CSS Classe(s) targeted: `.flexcyon-codeblock-fmt-ext`

Default: false (class toggle)

### Add Prefix before Code Block File Extension

CSS Classe(s) targeted: `.flexcyon-codeblock-prefix-ext`

Default: false (class toggle)

### Customise Prefix before Code Block Extension

CSS Variable(s) targeted: `var(--flexcyon-codeblock-ext-prefix)`

Default: "."

### Code Block File Extension Font Weight

CSS Variable(s) targeted: `var(--flexcyon-code-file-ext-font-w)`

Default: 500
