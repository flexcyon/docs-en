---
title: Editor Background
---

Configure the background in the editor

Accepted formats: px, deg

## Navigation

```md
Style Settings
|-- flexcyon://Editor
|   |-- Editor Background
```

## Configuration Options

### Select Background Type

CSS Classe(s) targeted: `.flexcyon-editor-grid, .flexcyon-editor-dots, .flexcyon-editor-rhombus`

Default: none (class select)

Options:

- Grid Background
- Dotted Background
- Rhombus Background
- Circle Background (Polka dot pattern)
- Chess Background (Checkerboard pattern)

### Rotation value for grid and rhombus background

CSS Variable(s) targeted: `var(--flexcyon-editor-bg-rotation)`

Default: 0 (deg)

### Width between each dot/line for grid/dotted background

CSS Variable(s) targeted: `var(--flexcyon-editor-bg-width)`

Default: 15 (px)

### Size of dots for dotted background

CSS Variable(s) targeted: `var(--flexcyon-editor-dot-size)`

Default: 2.5 (px)

### Alternate Width for editor background

> For the chess and circle backgrounds

CSS Variable(s) targeted: `var(--flexcyon-editor-bg-width-2)`

Default: 40 (px)

### Alternate dot size for editor background

> For the chess and circle backgrounds

CSS Variable(s) targeted: `var(--flexcyon-editor-dot-size-2)`

Default: 6 (px)
