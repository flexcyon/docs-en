---
title: Files
---

Configure file trees and folder styles.

## Navigation

```md
Style Settings
|-- flexcyon://Editor
|   |-- Files
```

## Configuration Options

### Enable dimmed file extensions in file explorer

Technically applies to all tree items.

CSS Classe(s) targeted: `var(--flexcyon-file-exp-dimmed-file-exts-enabled)`

Default: true (class toggle)

### Dimmed File Extensions font size

CSS Variable(s) targeted: `var(--flexcyon-exp-dimmed-nav-size)`

Default: 13.3623 (px)

### Enable Active File Indicator

CSS Classe(s) targeted: `var(--flexcyon-enable-active-file-indicator)`

Default: false (class toggle)

### Active File Indicator value

CSS Variable(s) targeted: `var(--flexcyon-active-indicator)`

Default: ">> "

### Enable vertical navigation

CSS Variable(s) targeted: `var(--flexcyon-vertical-nav)`

Default: false (class toggle)

### Select folder style

Alternate folder style Adds padding for active file item, makes collapse icons and borders blue for active folders.


CSS Classe(s) targeted: `.flexcyon-rainbow-folders, .flexcyon-alt-folder-style, .flexcyon-md-file-tree-style`

Default: none (class select)

Options:

- Rainbow folders
- Alternate folder style
- Markdown file tree style

### Colour background instead of text for rainbow folders

CSS Classe(s) targeted: `var(--flexcyon-is-bg-rainbow)`

Default: true

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

### Reverse order of Nav Header and other content

Places nav header below other content, for example placing the New Note and
other icons below the file explorer.

CSS Variable(s) targeted: `var(--flexcyon-reverse-workspace-content)`

Default: false (class toggle)
