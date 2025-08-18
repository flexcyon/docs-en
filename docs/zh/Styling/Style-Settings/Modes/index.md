---
title: Modes
icon: material/toggle-switch
---

配置 flexcyon 提供的一些独特模式。您还可以在此处配置辅助功能设置。

## 导航

```md
Style Settings
|-- ...
|-- Flexcyon Style Settings
| |-- Modes
| |-- ...
```

## Configuration Options

### Return to Zero mode

> Extreme minimalism inspired by the Shimmering Focus theme. Most UI elements
> are not displayed until hovered on. Will not recommend on mobile. Does not work with Flex Max mode.

CSS Variable(s) targeted: `var(--flexcyon-rtz-mode)`

Default: false (class toggle)

### Flex Max mode

> An extremely opinionated set up which showcases the unique customisation in this theme, with features working out of the box. If some options are not too your taste you can disable this mode and customise the theme more yourself, it will reset the theme to a clean slate customisations wise. There are also other default options enabled which you may or may not like. See below for the list of options it enables on your behalf.

_This mode is recommended for users who do not know where to start in terms of customisation. **For those who wish to customise the theme extensively or those who may not like this set of defaults, disabling this mode is recommended**._

CSS Variable(s) targeted: `var(--flexcyon-flex-max-mode)`

Default: true (class toggle)

### Flex Max mode enabled settings options

Enables the following settings, even if they are toggled off in style settings

~ smiley icons

~ ensure community plugin icons take precedence

~ left to right animation type

~ animations in Style Settings container

~ ASCII art

~ custom horizontal rule string

~ Powerlevel10k inspired layout and status bar style

~ ASCII checkboxes

~ Hide until hover status bar

~ Current status bar editing mode as text instead of icon

~ Vim mode status

~ Coloured headings

~ Extended colour palette

~ Dimmed file extensions

~ Wrap long filenames

~ ASCII checkboxes

~ Clip Path checkboxes

~ Do not show properties in Reading mode

~ Coloured icons in settings

~ Community item effects

~ Do not show scrollbar in settings

~ Dimmed file extensions for Alternate File Tree Plugin

~ Disable Empty state title

~ Enable side dock icon effects

~ Lowercase code block file extensions (Live Preview)

~ Add prefix to code block file extension (Live Preview)

You should be able to configure these settings as if they were enabled normally. The theme has many other settings options for you to explore, some of which are enabled by default like smooth cursor.

### Enable Writing Mode globally

> Like its cssclass counterpart, except applied globally

CSS Variable(s) targeted: `var(--flexcyon-editor-writing)`

Default: false (class toggle)

### Writing mode indentation

CSS Variable(s) targeted: `var(--flexcyon-editor-writing-indentation)`

Default: 16 (px)

---

### Accessibility

Toggle accessibility options

> Note that changing these will change how the entire theme renders.
>
> Tweaking these values too much may make the theme look ugly

### Global brightness ratio

CSS Variable(s) targeted: `var(--flexcyon-brightness-ratio)`

Default: 1

### Global contrast ratio

CSS Variable(s) targeted: `var(--flexcyon-contrast-ratio)`

Default: 1

> E.g. if you want slightly more contrast like on an OLED screen, try values
> between 1 to 1.5

### Global saturation ratio

CSS Variable(s) targeted: `var(--flexcyon-saturation-ratio)`

Default: 1

> Use to modify the saturation of colors
