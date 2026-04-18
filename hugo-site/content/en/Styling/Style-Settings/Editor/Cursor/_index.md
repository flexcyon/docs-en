---
title: Cursor
icon: material/cursor-text
---

Configure the cursor

## Navigation

```md
Style Settings
|-- ...
|-- Flexcyon Style Settings
| |-- Editor
| | |-- ...
| | |-- Cursor
| |-- ...
|-- ...
```

## Configuration Options

### Default cursor type

CSS Variable(s) targeted: `var(--flexcyon-cursor-type)`

Sets the cursor type when it is not specified by the app.
> Not the VS Code fork

Default: auto (variable select)

Options: For full list of options, view [MDN on cursor styling](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/cursor).

### Enable smooth cursor

CSS Classe(s) targeted: `var(--flexcyon-enable-smooth-cursor)`

Default: true

> Technically the caret, as was pointed out.

### Smooth cursor transition duration

CSS Classe(s) targeted: `var(--flexcyon-cursor-duration)`

Default: 42.5 (ms)

### Smooth cursor timing function

CSS Classe(s) targeted: `var(--flexcyon-cursor-timing-fn)`

Default: ease-in

### Smooth cursor minimum width

CSS Classe(s) targeted: `var(--flexcyon-cursor-min-width)`

Default: unset
