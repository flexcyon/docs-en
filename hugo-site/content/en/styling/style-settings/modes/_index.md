---
title: Modes
---

Configure some unique modes flexcyon has to offer.

## Navigation

```md
Style Settings
|-- flexcyon://Modes
```

## Configuration Options

### Select Mode
CSS Classe(s) targeted: `.flexcyon-flex-max-mode, .flexcyon-rtz-mode`

Default: Flex Max Mode (class select)

Options:

- none
- Flex Max Mode
- Return To Zero Mode

### About Return to Zero mode

Extreme minimalism inspired by the Shimmering Focus theme. Most UI elements
are not displayed until hovered on.
> Will not recommend on mobile.

### About Flex Max mode

An extremely opinionated set up which showcases the unique customisation in this
theme, with features working out of the box. If some options are not too your
taste you can disable this mode and customise the theme more yourself, it will
reset the theme to a clean slate customisations wise.

There are also other default options enabled which you may or may not like.
See below for the list of options it enables on your behalf.

This mode is recommended for users who do not know where to start in terms of
customisation. For those who wish to **customise the theme extensively** or those
who may not like this set of defaults, **disabling this mode is recommended**.

### Flex Max mode enabled settings options

Enables the following settings, even if they are toggled off in style settings

TODO: Sort these in order of appearance in style settings.

* Smiley icons

* ensure community plugin icons take precedence

* Add ASCII art before empty state title

* Disable Empty state title

* Custom horizontal rule string

* Powerlevel10k inspired status bar style

* Hide until hover status bar

* Current status bar editing mode as text instead of icon

* Vim mode status

* Coloured headings

* Extended colour palette

* ASCII checkboxes

* Clip Path checkboxes

* Coloured icons in settings

* Community item effects

* Do not show scrollbar in settings

* Dimmed file extensions for Alternate File Tree Plugin

* Enable side dock icon effects

* Lowercase code block file extensions (Live Preview)

* Add prefix to code block file extension (Live Preview)

You should be able to configure these settings as if they were enabled normally.
The theme has many other settings options for you to explore, some of which are
enabled by default like smooth cursor.

### Typewriter Mode

CSS Classe(s) targeted: `var(--flexcyon-typewriter-mode)`

Reduce opacity of all but the active line in source and live preview mode

Default: false (class toggle)
  
### Typewriter Mode Opacity

Opacity of dimmed non-active lines in typewriter mode

CSS Variable(s) targeted: `var(--flexcyon-typewriter-mode-opacity)`

Default: 0.55

### Reverse Mode

Reverses the rendering of stuff in the UI.

CSS Variable(s) targeted: `var(--flexcyon-reverse-mode)`

Default: false (class toggle)

### Enable Writing Mode globally

> Like its cssclass counterpart, except applied globally

CSS Variable(s) targeted: `var(--flexcyon-editor-writing)`

Default: false (class toggle)

### Writing mode indentation


CSS Variable(s) targeted: `var(--flexcyon-editor-writing-indentation)`

Default: 16 (px)
