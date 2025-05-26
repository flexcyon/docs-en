---
title: 。icon: material/dots-horizontal
---

For configuring vim mode text, new tab apperance (ASCII art), sidedock icons,
tooltip radius

。: px

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

。CSS。:`var(--flexcyon-vim-mode-text-enable)`

。:true(。)

#### Vim mode text left positioning

。CSS。:`var(--flexcyon-vim-mode-left-positioning)`

Default: 6 (px)

#### Vim mode text bottom positioning

。CSS。:`var(--flexcyon-vim-mode-left-positioning)`

Default: -4 (px)

#### Insert Mode Text

。CSS。:`var(--flexcyon-vim-insert-text)`

Default: "INSERT"

#### Normal Mode Text

。CSS。:`var(--flexcyon-vim-normal-text)`

Default: "NORMAL"

#### Command Mode Text

。CSS。:`var(--flexcyon-vim-command-text)`

Default: "COMMAND"

 

### New Tab Appearance

Customize the apperance of new empty tabs

。: px

#### Add before empty state title

CSS。:`.flexcyon-ascii-enable, .flexcyon-quote-enable`
> Changing this may take an app reload/restart to take effect

。: 无( 。)
。:

- ASCII Art
- Quote

#### Background for add before empty state title

。CSS。:`var(--flexcyon-new-tab-bg-wrapper)`

。:`linear-gradient(to right, var(--text-accent), var(--color-blue), var(--color-cyan))`

#### Quote

。CSS。:`var(--flexcyon-quote-val)`

Default: ""

#### Quote font size

。CSS。:`var(--flexcyon-quote-font-size)`

Default: 24 (px)
> Line breaks are escaped as `\a` and `\` is escaped as `\\`

#### ASCII Art

。CSS。:`var(--flexcyon-ascii-art)`

。:

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

。CSS。:`var(--flexcyon-ascii-max-font-size)`

。: 14 (px)

#### ASCII art line height

。CSS。:`var(--flexcyon-ascii-line-height)`
> Changes line height for quote as welll

Default: 1

#### Disable Empty State title

。CSS。:`var(--flexcyon-empty-state-title-disable)`

。:true(。)

#### Disable Empty State Actions

。CSS。:`var(--flexcyon-empty-state-actions-disable)`

。:false(。)

 

### Side Dock Icons

Configure the side dock icons

#### Enable side dock icon effects
> Rainbow effect on hover
。CSS。:`var(--flexcyon-sidedock-icon-effects)`

。:true(。)

#### Hide the side dock ribbon

。CSS。:`var(--flexcyon-sidedock-ribbon-hidden)`

。:false(。)

 

### Tooltip radius

Configure the tooltip radius

#### Small radius

。CSS。:`var(--radius-s)`

。: 2 (px)

#### Medium radius

。CSS。:`var(--radius-m)`

。: 4( px)

#### Large radius

。CSS。:`var(--radius-l)`

。: 6 (px)

#### Extra large radius

。CSS。:`var(--radius-xl)`

。: 8 (px)

 

### Sidebar Background

Configure background images in the left and right sidebars.

Accepted Formats: px, %

#### Select background in sidebar

CSS。:`.flexcyon-sidebar-bg-dots, .flexcyon-sidebar-bg-grid, flexcyon-sidebar-bg-rhombus`
> Overrides background image declaration below, configures in both left and
> right sidebar

。: 无( 。)
。:

- Grid
- Dotted
- Rhombus

#### Left sidebar background image url

。CSS。:`var(--flexcyon-bg-image-sidebar-left-url)`

Default: url("")
> For urls to work, add your URL between the double quotes e.g. a value of:
`url("https://fake_domain/not_a_real_image.png")`

#### Right sidebar background image url

。CSS。:`var(--flexcyon-bg-image-sidebar-right-url)`

。: url (")
> For urls to work, add your URL between the double quotes e.g. a value of:
`url("https://fake_domain/not_a_real_image.png")`

#### Sidebar Background image blend mode

。CSS。:`var(--flexcyon-bg-image-blend-mode)`

。:darken

#### Sidebar Background image repeat

。CSS。:`var(--flexcyon-bg-image-repeat)`

。:no-repeat

#### Sidebar Background image blur

。CSS。:`var(--flexcyon-bg-image-blur)`

Default: 1px
> Will be changed to 0px next update

#### Sidebar Background image brightness

。CSS。:`var(--flexcyon-bg-image-brightness)`

。:unset
> Accepts percentage values like 55%

#### Sidebar Background image size

。CSS。:`var(--flexcyon-bg-image-size)`

。:contain

#### Sidebar Background image position

。CSS。:`var(--flexcyon-bg-image-position)`

。:center

 

### Modal Background

Configure background images in the background of settings menu, prompts etc

。: px,%

#### Modal Background image url

。CSS。:`var(--flexcyon-modal-bg-url)`

。: url (")
> For urls to work, add your URL between the double quotes e.g. a value of:
`url("https://fake_domain/not_a_real_image.png")`

#### Modal Background image blend mode

。CSS。:`var(--flexcyon-modal-image-blend-mode)`

。:lighten

#### Modal Background image repeat

。CSS。:`var(--flexcyon-modal-image-repeat)`

。:no-repeat

#### Modal Background image blur

。CSS。:`var(--flexcyon-modal-image-blur)`

。:1px

#### Modal Background image brightness

。CSS。:`var(--flexcyon-bg-modal-brightness)`

。:unset
> Accepts percentage values like 55%

#### Modal background image size

。CSS。:`var(--flexcyon-modal-image-size)`

。:cover

#### Modal background image position

。CSS。:`var(--flexcyon-modal-image-position)`

。:center

 

### Easter egg mode

Deprecated. See [here for reasons](../../../README/page-5.md)。

 

### Accessibility

Toggle accessibility options
> Note that changing these will change how the entire theme renders.
>
> Tweaking these values too much may make the theme look ugly

### Global brightness ratio

。CSS。:`var(--flexcyon-brightness-ratio)`

。:1

### Global contrast ratio

。CSS。:`var(--flexcyon-contrast-ratio)`

。:1
> E.g. if you want slightly more contrast like on an OLED screen, try values
> between 1 to 1.5

### Global saturation ratio

。CSS。:`var(--flexcyon-saturation-ratio)`

。:1
> Use to modify the saturation of colors

 

### Return to Zero mode
> Extreme minimalism inspired by the Shimmering Focus theme. Most UI elements
> are not displayed until hovered on. Will not recommend on mobile.

。CSS。:`var(--flexcyon-rtz-mode)`

。:false(。)

