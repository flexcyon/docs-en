---
title: Icons
---

## Navigation

```md
Style Settings
|-- flexcyon://Editor
|   |-- Icons
```

## Configuration Options

### Upscale percentage of icons 1

CSS Variable(s) targeted: `var(--upsize)`

Default: 103%

<span style="scale: 103%">Sample upscale percentage 1</span>

### Upscale percentage of icons 2

CSS Variable(s) targeted: `var(--expand)`

Default: 110%

<span style="scale: 110%">Sample upscale percentage 2</span>

### Smiley Toggle Icons in Settings

CSS Classe(s) targeted: `.flexcyon-settings-smiley-icons-enabled`

Default: false (class toggle)

### Load ASCII Icon Set

Replaces some icons with ASCII Icons, works best when used together with smiley icons. This will override the declarations by community plugins like Iconic for the specific icons targeted. This can be prevented with the setting below.

CSS Classe(s) targeted: `.flexcyon-ascii-icon-set`

Default: false (class toggle)

### Ensure community plugin icons take precedence

Ensure community plugins which modify icons have their modifications take precedence over this theme's. Smiley Icons and ASCII Icons will not render when said community plugins are enabled and this setting is enabled. This setting currently only works with the Iconic plugin, as adding support for all icon related plugins negatively affects performance too much.

CSS Classe(s) targeted: `.flexcyon-ensure-plugin-icon`

Default: true (class toggle)

### Coloured Icons in Settings

Display coloured icons for buttons in setting like uninstall, options, hotkeys, etc. Current implementation might not work with earlier Obsidian versions.

CSS Variable(s) targeted: `var(--flexcyon-settings-coloured-icons)`

Default: false (class toggle)
