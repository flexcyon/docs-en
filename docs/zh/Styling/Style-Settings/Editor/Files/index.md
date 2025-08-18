---
title: Files
icon: material/file-cog
---

Configure file trees and folder styles.

## Navigation

```md
Style Settings
|-- ...
|-- Flexcyon Style Settings
| |-- Editor
| | |-- ...
| | |-- Files
| | |-- ...
| |-- ...
|-- ...
```

## Configuration Options

### Enable dimmed file extensions in file explorer

CSS Variable(s) targeted: `var(--flexcyon-file-exp-dimmed-file-exts-enabled)`

Default: true (class toggle)

### Select folder style

CSS Classe(s) targeted: `.flexcyon-rainbow-folders, .flexcyon-alt-folder-style, .flexcyon-md-file-tree-style`

Default: none (class select)

Options:

- Rainbow folders
- Alternate folder style
- Markdown file tree style

### Colour background instead of text for rainbow folders

CSS Classe(s) targeted: `var(--flexcyon-is-bg-rainbow)`

Default: false

### Enable minimalist trees

CSS Variable(s) targeted: `var(--flexcyon-minimalist-tree)`

Default: false (class toggle)

### Vertical Tree Item Padding

CSS Classe(s) targeted: `var(--flexcyon-tree-item-verti-padding)`

Default: 2 (px)

### Horizontal Tree Item Padding

CSS Classe(s) targeted: `var(--flexcyon-tree-item-horiz-padding)`

Default: 10 (px)

### Wrap Long File Names

Wrap long filenames to a new line instead of omitting the ending part.

CSS Variable(s) targeted: `var(--flexcyon-wrap-long-filenames)`

Default: true (class toggle)
