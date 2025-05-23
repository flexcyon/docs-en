---
title: Otros
icon: material/dots-horizontal
---

Para configurar el texto del modo vim, nueva apperance de pestañas (ASCII art), iconos laterales, radio de punta de herramientas

Formatos aceptados: px

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
CSS Variable(s) targeted:`var(--flexcyon-vim-mode-text-enable)`

Default:true(de clase)

#### Vim mode text left positioning
CSS Variable(s) targeted:`var(--flexcyon-vim-mode-left-positioning)`

Predeterminado: 6 (px)

#### Vim mode text bottom positioning
CSS Variable(s) targeted:`var(--flexcyon-vim-mode-left-positioning)`

Predeterminado: -4 (px)

#### Insert Mode Text
CSS Variable(s) targeted:`var(--flexcyon-vim-insert-text)`

Default: "INSERT"

#### Normal Mode Text
CSS Variable(s) targeted:`var(--flexcyon-vim-normal-text)`

Default: "NORMAL"

#### Command Mode Text
CSS Variable(s) targeted:`var(--flexcyon-vim-command-text)`

Default: "COMMAND"

___
### New Tab Appearance
Personalizar la tolerancia de nuevas pestañas vacías

Formatos aceptados: px

#### Add before empty state title
CSS Classe(s) targeted:`.flexcyon-ascii-enable, .flexcyon-quote-enable`
> Changing this may take an app reload/restart to take effect

Predeterminado: ninguno (clase selecto)
Opciones:
- Arte ASCII
- Cita.

#### Background for add before empty state title
CSS Variable(s) targeted:`var(--flexcyon-new-tab-bg-wrapper)`

Default:`linear-gradient(to right, var(--text-accent), var(--color-blue), var(--color-cyan))`

#### Quote
CSS Variable(s) targeted:`var(--flexcyon-quote-val)`

Default: ""

#### Quote font size
CSS Variable(s) targeted:`var(--flexcyon-quote-font-size)`

Predeterminado: 24 (px)
> Line breaks are escaped as `\a` and `\` is escaped as `\\`

#### ASCII Art
CSS Variable(s) targeted:`var(--flexcyon-ascii-art)`

Default:
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
> The ASCII art string needs to be escaped for CSS to render it, line breaks are escaped as `\a` and `\` is escaped as `\\`

#### ASCII art font size limit
CSS Variable(s) targeted:`var(--flexcyon-ascii-max-font-size)`

Predeterminado: 14 (px)

#### ASCII art line height
CSS Variable(s) targeted:`var(--flexcyon-ascii-line-height)`
> Changes line height for quote as welll

Default: 1

#### Disable Empty State title
CSS Variable(s) targeted:`var(--flexcyon-empty-state-title-disable)`

Default:true(de clase)

#### Disable Empty State Actions
CSS Variable(s) targeted:`var(--flexcyon-empty-state-actions-disable)`

Default:false(de clase)

___
### Side Dock Icons
Configure los iconos de muelle lateral

#### Enable side dock icon effects
> Rainbow effect on hover
CSS Variable(s) targeted:`var(--flexcyon-sidedock-icon-effects)`

Default:true(de clase)

#### Hide the side dock ribbon
CSS Variable(s) targeted:`var(--flexcyon-sidedock-ribbon-hidden)`

Default:false(de clase)

___
### Tooltip radius
Configure el radio de punta de la herramienta

#### Small radius
CSS Variable(s) targeted:`var(--radius-s)`

Predeterminado: 2 (px)

#### Medium radius
CSS Variable(s) targeted:`var(--radius-m)`

Predeterminado: 4 (px)

#### Large radius
CSS Variable(s) targeted:`var(--radius-l)`

Predeterminado: 6 (px)

#### Extra large radius
CSS Variable(s) targeted:`var(--radius-xl)`

Predeterminado: 8 (px)

___
### Sidebar Background 
Configurar imágenes de fondo en las barras laterales izquierda y derecha.
.

Formatos aceptados: px, %

#### Select background in sidebar
CSS Classe(s) targeted:`.flexcyon-sidebar-bg-dots, .flexcyon-sidebar-bg-grid, flexcyon-sidebar-bg-rhombus`
> Overrides background image declaration below, configures in both left and right sidebar

Predeterminado: ninguno (clase selecto)
Opciones:
- Grid
- Dotted
- Rhombus

#### Left sidebar background image url
CSS Variable(s) targeted:`var(--flexcyon-bg-image-sidebar-left-url)`

Predeterminado: url("")
> For urls to work, add your URL between the double quotes e.g. a value of:
`url("https://fake_domain/not_a_real_image.png")`

#### Right sidebar background image url
CSS Variable(s) targeted:`var(--flexcyon-bg-image-sidebar-right-url)`

Predeterminado: url("")
> For urls to work, add your URL between the double quotes e.g. a value of:
`url("https://fake_domain/not_a_real_image.png")`

#### Sidebar Background image blend mode
CSS Variable(s) targeted:`var(--flexcyon-bg-image-blend-mode)`

Default: darken

#### Sidebar Background image repeat
CSS Variable(s) targeted:`var(--flexcyon-bg-image-repeat)`

Default:no-repeat

#### Sidebar Background image blur
CSS Variable(s) targeted:`var(--flexcyon-bg-image-blur)`

Predeterminado: 1px
> Will be changed to 0px next update

#### Sidebar Background image brightness
CSS Variable(s) targeted:`var(--flexcyon-bg-image-brightness)`

Default:unset
> Accepts percentage values like 55%

#### Sidebar Background image size
CSS Variable(s) targeted:`var(--flexcyon-bg-image-size)`

Default:contain

#### Sidebar Background image position
CSS Variable(s) targeted:`var(--flexcyon-bg-image-position)`

Por defecto: centro

___
### Modal Background
Configurar imágenes de fondo en el fondo del menú de configuración, indicaciones, etc

Formatos aceptados: px, %

#### Modal Background image url
CSS Variable(s) targeted:`var(--flexcyon-modal-bg-url)`

Predeterminado: url("")
> For urls to work, add your URL between the double quotes e.g. a value of:
`url("https://fake_domain/not_a_real_image.png")`

#### Modal Background image blend mode
CSS Variable(s) targeted:`var(--flexcyon-modal-image-blend-mode)`

Default:lighten

#### Modal Background image repeat
CSS Variable(s) targeted:`var(--flexcyon-modal-image-repeat)`

Default:no-repeat

#### Modal Background image blur
CSS Variable(s) targeted:`var(--flexcyon-modal-image-blur)`

Predeterminado: 1px

#### Modal Background image brightness
CSS Variable(s) targeted:`var(--flexcyon-bg-modal-brightness)`

Default:unset
> Accepts percentage values like 55%

#### Modal background image size
CSS Variable(s) targeted:`var(--flexcyon-modal-image-size)`

Default: cover

#### Modal background image position
CSS Variable(s) targeted:`var(--flexcyon-modal-image-position)`

Por defecto: centro

___
### Easter egg mode
Deprecatado. [[LINK0]]].
.

___
### Accessibility
Toggle accessibility options
> Note that changing these will change how the entire theme renders. 
>
> Tweaking these values too much may make the theme look ugly

### Global brightness ratio
CSS Variable(s) targeted:`var(--flexcyon-brightness-ratio)`

Default: 1

### Global contrast ratio
CSS Variable(s) targeted:`var(--flexcyon-contrast-ratio)`

Default: 1
> E.g. if you want slightly more contrast like on an OLED screen, try values between 1 to 1.5

### Global saturation ratio
CSS Variable(s) targeted:`var(--flexcyon-saturation-ratio)`

Default: 1
> Use to modify the saturation of colors

___
### Return to Zero mode
> Extreme minimalism inspired by the Shimmering Focus theme. Most UI elements are not displayed until hovered on. Will not recommend on mobile.

CSS Variable(s) targeted:`var(--flexcyon-rtz-mode)`

Default:false(de clase)