---
title: Otros
icon: material/dots-horizontal
---

Para configurar el texto del modo vim, nueva apperance de pestañas (ASCII art), iconos sidedock,
,
radio de punta de la herramienta

Formatos aceptados: px

## Navigation

```md
Style Settings
|-- 。
|-- Flexcyon Style Settings
|   |-- 。
|   |-- Others
```
## Configuration Options

### Vim Mode Text

#### Enable Vim Mode Text

CSSVariable(s) targeted:`var(--flexcyon-vim-mode-text-enable)`
Default:true(de clase)

#### Vim mode text left positioning

CSSVariable(s) targeted:`var(--flexcyon-vim-mode-left-positioning)`
Predeterminado: 6 (px)

#### Vim mode text bottom positioning

CSSVariable(s) targeted:`var(--flexcyon-vim-mode-left-positioning)`
Predeterminado: -4 (px)

#### Insert Mode Text

CSSVariable(s) targeted:`var(--flexcyon-vim-insert-text)`
Default: "INSERT"

#### Normal Mode Text

CSSVariable(s) targeted:`var(--flexcyon-vim-normal-text)`
Default: "NORMAL"

#### Command Mode Text

CSSVariable(s) targeted:`var(--flexcyon-vim-command-text)`
Default: "COMMAND"

___

### New Tab Appearance

Personalizar la tolerancia de nuevas pestañas vacías

Formatos aceptados: px

#### Add before empty state title

CSSClasse(s) targeted:`.flexcyon-ascii-enable, .flexcyon-quote-enable`
> Cambiar esto puede tomar una recarga de la aplicación / reiniciar para tener efecto

Default: none (class select)
Opciones:

- Arte ASCII
- Cita.

#### Background for add before empty state title

CSSVariable(s) targeted:`var(--flexcyon-new-tab-bg-wrapper)`
Default:`linear-gradient(to right, var(--text-accent), var(--color-blue), var(--color-cyan))`
#### Quote

CSSVariable(s) targeted:`var(--flexcyon-quote-val)`
Default: "Esto es una cotización de marca de posición\ain el tema Flexcyon."

#### Quote Attribution Prefix

CSSVariable(s) targeted:`var(--flexcyon-quote-credit-prefix)`
Default: "-"

#### Quote Attribution

CSSVariable(s) targeted:`var(--flexcyon-quote-credit)`
Default: "bladeacer"

#### Quote font size

CSSVariable(s) targeted:`var(--flexcyon-quote-font-size)`
Predeterminado: 24 (px)
> Los descansos de la línea se escapan`\a`y`\`se escapó`\\`
#### ASCII Art

CSSVariable(s) targeted:`var(--flexcyon-ascii-art)`
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
> La cadena de arte ASCII necesita ser escapada paraCSSpara renderizarla, las roturas de línea
> escaparon`\a`y`\`se escapó`\\`
#### ASCII art font size limit

CSSVariable(s) targeted:`var(--flexcyon-ascii-max-font-size)`
Predeterminado: 14 (px)

#### ASCII art line height

CSSVariable(s) targeted:`var(--flexcyon-ascii-line-height)`
> Cambios línea de altura para la cotización as welll

Default: 1

#### Disable Empty State title

CSSVariable(s) targeted:`var(--flexcyon-empty-state-title-disable)`
Default:true(de clase)

#### Disable Empty State Actions

CSSVariable(s) targeted:`var(--flexcyon-empty-state-actions-disable)`
Default:false(de clase)

___

### Side Dock

Configure los iconos de muelle lateral

#### Enable side dock icon effects
> Efecto del arco iris en el tubo

CSSVariable(s) targeted:`var(--flexcyon-sidedock-icon-effects)`
Default:true(de clase)

### Side Dock Ribbon Width

CSSVariable(s) targeted:`var(--flexcyon-sidedock-ribbon-width)`
Default: 48 (px)

___

### Tooltip radius

Configure el radio de punta de la herramienta

#### Small radius

CSSVariable(s) targeted:`var(--radius-s)`
Predeterminado: 2 (px)

#### Medium radius

CSSVariable(s) targeted:`var(--radius-m)`
Predeterminado: 4 (px)

#### Large radius

CSSVariable(s) targeted:`var(--radius-l)`
Predeterminado: 6 (px)

#### Extra large radius

CSSVariable(s) targeted:`var(--radius-xl)`
Predeterminado: 8 (px)

___

### Sidebar Background

Configurar imágenes de fondo en las barras laterales izquierda y derecha.
.

Formatos aceptados: px, %

#### Select background in sidebar

CSSClasse(s) targeted:`.flexcyon-sidebar-bg-dots, .flexcyon-sidebar-bg-grid, flexcyon-sidebar-bg-rhombus`
> Supera la declaración de imagen de fondo a continuación, configura en izquierda y
> barra lateral derecha

Default: none (class select)
Opciones:

- Grid
- Dotted
- Rhombus

#### Left sidebar background image url

CSSVariable(s) targeted:`var(--flexcyon-bg-image-sidebar-left-url)`
Predeterminado: url("")
> Para que los urls funcionen, agregue su URL entre las citas dobles, por ejemplo, un valor de:
`url("https://fake_domain/not_a_real_image.png")`
#### Right sidebar background image url

CSSVariable(s) targeted:`var(--flexcyon-bg-image-sidebar-right-url)`
Predeterminado: url("")
> Para que los urls funcionen, agregue su URL entre las citas dobles, por ejemplo, un valor de:
`url("https://fake_domain/not_a_real_image.png")`
#### Sidebar Background image blend mode

CSSVariable(s) targeted:`var(--flexcyon-bg-image-blend-mode)`
Default:darken

#### Sidebar Background image repeat

CSSVariable(s) targeted:`var(--flexcyon-bg-image-repeat)`
Default:no-repeat

#### Sidebar Background image blur

CSSVariable(s) targeted:`var(--flexcyon-bg-image-blur)`
Predeterminado: 1px
> Se cambiará a 0px siguiente actualización

#### Sidebar Background image brightness

CSSVariable(s) targeted:`var(--flexcyon-bg-image-brightness)`
Default:unset
> Acepta valores porcentuales como 55%

#### Sidebar Background image size

CSSVariable(s) targeted:`var(--flexcyon-bg-image-size)`
Default:contain

#### Sidebar Background image position

CSSVariable(s) targeted:`var(--flexcyon-bg-image-position)`
Default:center

___

### Modal Background

Configurar imágenes de fondo en el fondo del menú de configuración, indicaciones, etc

Formatos aceptados: px, %

#### Modal Background image url

CSSVariable(s) targeted:`var(--flexcyon-modal-bg-url)`
Predeterminado: url("")
> Para que los urls funcionen, agregue su URL entre las citas dobles, por ejemplo, un valor de:
`url("https://fake_domain/not_a_real_image.png")`
#### Modal Background image blend mode

CSSVariable(s) targeted:`var(--flexcyon-modal-image-blend-mode)`
Default:lighten

#### Modal Background image repeat

CSSVariable(s) targeted:`var(--flexcyon-modal-image-repeat)`
Default:no-repeat

#### Modal Background image blur

CSSVariable(s) targeted:`var(--flexcyon-modal-image-blur)`
Predeterminado: 1px

#### Modal Background image brightness

CSSVariable(s) targeted:`var(--flexcyon-bg-modal-brightness)`
Default:unset
> Acepta valores porcentuales como 55%

#### Modal background image size

CSSVariable(s) targeted:`var(--flexcyon-modal-image-size)`
Default:cover

#### Modal background image position

CSSVariable(s) targeted:`var(--flexcyon-modal-image-position)`
Default:center

___

### Easter egg mode

Deprecatado. See[here for reasons](../../../README/page-5.md).
.

___

### Accessibility

Toggle accessibility options
> Tenga en cuenta que cambiar estos va a cambiar cómo el tema entero renderiza.
>
> Tweaking estos valores demasiado puede hacer que el tema parezca feo

### Global brightness ratio

CSSVariable(s) targeted:`var(--flexcyon-brightness-ratio)`
Default: 1

### Global contrast ratio

CSSVariable(s) targeted:`var(--flexcyon-contrast-ratio)`
Default: 1
> Por ejemplo, si quieres un poco más de contraste como en una pantalla OLED, prueba valores
> entre 1 y 11.

### Global saturation ratio

CSSVariable(s) targeted:`var(--flexcyon-saturation-ratio)`
Default: 1
> Uso para modificar la saturación de colores

___
## Modes

### Return to Zero mode
> El minimalismo extremo inspirado en el tema Shimmering Focus. La mayoría de los elementos de la UI
> no se muestran hasta que se encendieron. No recomendará en el móvil.

CSSVariable(s) targeted:`var(--flexcyon-rtz-mode)`
Default:false(de clase)

### Enable Writing Mode globally
> Como su contraparte cssclass, excepto aplicada globalmente

CSSVariable(s) targeted:`var(--flexcyon-editor-writing)`
Default:false(de clase)

### Writing mode indentation

CSSVariable(s) targeted:`var(--flexcyon-editor-writing-indentation)`
Predeterminado: 16 (px)

