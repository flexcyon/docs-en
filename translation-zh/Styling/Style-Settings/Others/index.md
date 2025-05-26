---
title: 其他人员
icon: material/dots-horizontal
---

For configuring vim mode text, new tab apperance (ASCII art), sidedock icons,
tooltip radius

接受格式: px

## Navigation

```md
Style Settings
|-- ...
|-- Flexcyon Style Settings
|   |-- ...
|   |-- Others
```

## Configuration Options

### Vim Mode Text

#### Enable Vim Mode Text

目标CSS变量:`var(--flexcyon-vim-mode-text-enable)`

默认 :true(类切换)

#### Vim mode text left positioning

目标CSS变量:`var(--flexcyon-vim-mode-left-positioning)`

Default: 6 (px)

#### Vim mode text bottom positioning

目标CSS变量:`var(--flexcyon-vim-mode-left-positioning)`

Default: -4 (px)

#### Insert Mode Text

目标CSS变量:`var(--flexcyon-vim-insert-text)`

Default: "INSERT"

#### Normal Mode Text

目标CSS变量:`var(--flexcyon-vim-normal-text)`

Default: "NORMAL"

#### Command Mode Text

目标CSS变量:`var(--flexcyon-vim-command-text)`

Default: "COMMAND"

 

### New Tab Appearance

Customize the apperance of new empty tabs

接受格式: px

#### Add before empty state title

CSS类目标:`.flexcyon-ascii-enable, .flexcyon-quote-enable`
> Changing this may take an app reload/restart to take effect

默认: 无( 类选择)
选项 :

- ASCII Art
- Quote

#### Background for add before empty state title

目标CSS变量:`var(--flexcyon-new-tab-bg-wrapper)`

默认 :`linear-gradient(to right, var(--text-accent), var(--color-blue), var(--color-cyan))`

#### Quote

目标CSS变量:`var(--flexcyon-quote-val)`

Default: ""

#### Quote font size

目标CSS变量:`var(--flexcyon-quote-font-size)`

Default: 24 (px)
> Line breaks are escaped as `\a` and `\` is escaped as `\\`

#### ASCII Art

目标CSS变量:`var(--flexcyon-ascii-art)`

默认 :

```md
" \a\
    _______________                                       \a\
    ___  ____/__  /________  ____________  ______________ \a\
    __  /_   __  /_  _ \\_  |/_/  ___/_  / / /  __ \\_  __ \\ \a\
    _  __/   _  / /  __/_
>  < / /__ _  /_/ // /_/ /  / / / \a\
    /_/      /_/  \\___//_/|_| \\___/ _\\__, / \\____//_/ /_/ \a\
                                    /____/                \a\a\a "
```
> The ASCII art string needs to be escaped for CSS to render it, line breaks are
> escaped as `\a` and `\` is escaped as `\\`

#### ASCII art font size limit

目标CSS变量:`var(--flexcyon-ascii-max-font-size)`

默认: 14 (px)

#### ASCII art line height

目标CSS变量:`var(--flexcyon-ascii-line-height)`
> Changes line height for quote as welll

Default: 1

#### Disable Empty State title

目标CSS变量:`var(--flexcyon-empty-state-title-disable)`

默认 :true(类切换)

#### Disable Empty State Actions

目标CSS变量:`var(--flexcyon-empty-state-actions-disable)`

默认 :false(类切换)

 

### Side Dock Icons

Configure the side dock icons

#### Enable side dock icon effects
> Rainbow effect on hover
目标CSS变量:`var(--flexcyon-sidedock-icon-effects)`

默认 :true(类切换)

#### Hide the side dock ribbon

目标CSS变量:`var(--flexcyon-sidedock-ribbon-hidden)`

默认 :false(类切换)

 

### Tooltip radius

Configure the tooltip radius

#### Small radius

目标CSS变量:`var(--radius-s)`

默认: 2 (px)

#### Medium radius

目标CSS变量:`var(--radius-m)`

默认: 4( px)

#### Large radius

目标CSS变量:`var(--radius-l)`

默认: 6 (px)

#### Extra large radius

目标CSS变量:`var(--radius-xl)`

默认: 8 (px)

 

### Sidebar Background

Configure background images in the left and right sidebars.

Accepted Formats: px, %

#### Select background in sidebar

CSS类目标:`.flexcyon-sidebar-bg-dots, .flexcyon-sidebar-bg-grid, flexcyon-sidebar-bg-rhombus`
> Overrides background image declaration below, configures in both left and
> right sidebar

默认: 无( 类选择)
选项 :

- Grid
- Dotted
- Rhombus

#### Left sidebar background image url

目标CSS变量:`var(--flexcyon-bg-image-sidebar-left-url)`

Default: url("")
> For urls to work, add your URL between the double quotes e.g. a value of:
`url("https://fake_domain/not_a_real_image.png")`

#### Right sidebar background image url

目标CSS变量:`var(--flexcyon-bg-image-sidebar-right-url)`

默认: url (")
> For urls to work, add your URL between the double quotes e.g. a value of:
`url("https://fake_domain/not_a_real_image.png")`

#### Sidebar Background image blend mode

目标CSS变量:`var(--flexcyon-bg-image-blend-mode)`

默认 :darken

#### Sidebar Background image repeat

目标CSS变量:`var(--flexcyon-bg-image-repeat)`

默认 :no-repeat

#### Sidebar Background image blur

目标CSS变量:`var(--flexcyon-bg-image-blur)`

Default: 1px
> Will be changed to 0px next update

#### Sidebar Background image brightness

目标CSS变量:`var(--flexcyon-bg-image-brightness)`

默认 :unset
> Accepts percentage values like 55%

#### Sidebar Background image size

目标CSS变量:`var(--flexcyon-bg-image-size)`

默认 :contain

#### Sidebar Background image position

目标CSS变量:`var(--flexcyon-bg-image-position)`

默认 :center

 

### Modal Background

Configure background images in the background of settings menu, prompts etc

接受格式: px,%

#### Modal Background image url

目标CSS变量:`var(--flexcyon-modal-bg-url)`

默认: url (")
> For urls to work, add your URL between the double quotes e.g. a value of:
`url("https://fake_domain/not_a_real_image.png")`

#### Modal Background image blend mode

目标CSS变量:`var(--flexcyon-modal-image-blend-mode)`

默认 :lighten

#### Modal Background image repeat

目标CSS变量:`var(--flexcyon-modal-image-repeat)`

默认 :no-repeat

#### Modal Background image blur

目标CSS变量:`var(--flexcyon-modal-image-blur)`

默认:1px

#### Modal Background image brightness

目标CSS变量:`var(--flexcyon-bg-modal-brightness)`

默认 :unset
> Accepts percentage values like 55%

#### Modal background image size

目标CSS变量:`var(--flexcyon-modal-image-size)`

默认 :cover

#### Modal background image position

目标CSS变量:`var(--flexcyon-modal-image-position)`

默认 :center

 

### Easter egg mode

Deprecated. See [here for reasons](../../../README/page-5.md)。

 

### Accessibility

Toggle accessibility options
> Note that changing these will change how the entire theme renders.
>
> Tweaking these values too much may make the theme look ugly

### Global brightness ratio

目标CSS变量:`var(--flexcyon-brightness-ratio)`

默认:1

### Global contrast ratio

目标CSS变量:`var(--flexcyon-contrast-ratio)`

默认:1
> E.g. if you want slightly more contrast like on an OLED screen, try values
> between 1 to 1.5

### Global saturation ratio

目标CSS变量:`var(--flexcyon-saturation-ratio)`

默认:1
> Use to modify the saturation of colors

 

### Return to Zero mode
> Extreme minimalism inspired by the Shimmering Focus theme. Most UI elements
> are not displayed until hovered on. Will not recommend on mobile.

目标CSS变量:`var(--flexcyon-rtz-mode)`

默认 :false(类切换)

