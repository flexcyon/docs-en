---
title: Callouts
icon: material/information-slab-box-outline
tags:
    - callouts
---

Configure styling of callouts

Accepted Formats: px, rem, em, ms

## Navigation

```md
Style Settings
|-- ...
|-- Flexcyon Style Settings
|   |-- Editor
|   |   |-- ...
|   |   |-- Callouts
|   |   |-- ...
|   |-- ...
|-- ...
```

## Configuration Options

### Callout Icon Right padding

CSS Variable(s) targeted: `var(--flexcyon-callout-icon-right-padding)`

Default: 4 (px)

### First Codeblock Margin Top

CSS Variable(s) targeted: `var(--flexcyon-callout-first-codeblock-margin-top)`

Default: 1 (rem)

### Callout Metadata Background Opacity

CSS Variable(s) targeted: `var(--flexcyon-callout-bg-opacity)`

Default: 20%

<span style="opacity: 20%">Sample Background Opacity</span>

### Callout Vertical Margin

CSS Variable(s) targeted: `var(--flexcyon-callout-vertical-margin)`

Default: 1 (em)

### Callout Vertical Padding

CSS Variable(s) targeted: `var(--flexcyon-callout-vertical-padding)`

Default: 12 (px)

### Callout Horizontal Padding

CSS Variable(s) targeted: `var(--flexcyon-callout-horiz-padding)`

Default: 24 (px)

### Callout Border Radius

CSS Variable(s) targeted: `var(--callout-radius)`

Default: 2 (px)

### Callout Added Border Radius

CSS Variable(s) targeted: `var(--flexcyon-callout-radix)`

Default: 16 (px)

### Select callout style

CSS Classe(s) targeted: `.flexcyon-tui-callouts, .flexcyon-plain-callouts, .flexcyon-vert-callouts`

Default: none (class select)

Options:

- TUI Callouts
- Plain Callouts
- Vertical Callouts

### Disable icons for TUI callout


CSS Classe(s) targeted: `.flexcyon-tui-no-icons`

Default: false (class toggle)

___
### Flashcard callout

Configures the [flashcard callout](../../../Callout-Metadata/flashcard.md).

#### Flashcard callout width

CSS Variable(s) targeted: `var(--flexcyon-callouts-flashcard-width)`

Default: 250 (px)

#### Flashcard callout height

CSS Variable(s) targeted: `var(--flexcyon-callouts-flashcard-height)`

Default: 250 (px)

#### Flashcard callout animation duration

CSS Variable(s) targeted: `var(--flexcyon-callout-flashcard-animation-duration)`

Default: 500 (ms)

___
### Popup callout

Configures the [popup callout](../../../Callout-Metadata/popup.md)

#### Popup callout animation duration

CSS Variable(s) targeted: `var(--flexcyon-callout-pop-animation-duration)`

Default: 200 (ms)

