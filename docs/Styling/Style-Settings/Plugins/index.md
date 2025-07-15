---
title: Plugins
icon: material/hexagon-outline
---

Para la configuración de plugins compatibles oficialmente

Formatos aceptados: HEX, rem, x.y, %

## Navigation

```md
Style Settings
|-- 。
|-- Flexcyon Style Settings
|   |-- 。
|   |-- Plugins
|   |-- 。
```

## Configuration Options

### Alternate file tree

#### Folders font size

CSSVariable(s) targeted:`var(--oz-fta-folder-font-size)`
Default: 0.925 (rem)

<span style="font-size: 0.925rem"
>Muestra Árbol de archivo alternativo Folders tamaño de la fuente</span>

#### Folders font color

CSSVariable(s) targeted:`var(--oz-fta-folder-pane-file-name-color)`
Default (modo de luz):
<span class="col-sqr" style="background-color: #080808"
></span
>#080808

Default (modo oscuro):
<span class="col-sqr" style="background-color: #d3d5d3"
></span
>#d3d5d3

#### Active folder color

CSSVariables(s) dirigidas:`var(--oz-fta-all-panes-active-text-color)`
Default (modo de luz):
<span class="col-sqr" style="background-color: #080808"
></span
>#080808

Default (modo oscuro):
<span class="col-sqr" style="background-color: #d3d5d3"
></span
>#d3d5d3

#### Files font size

CSSVariable(s) targeted:`var(--oz-fta-file-font-size)`
Predeterminado: 0.9 (rem)

<span style="font-size: 0.9rem"
>Muestra Árbol de archivos alternativos tamaño de fuente</san>

#### Files font color

CSSVariable(s) targeted:`var(--oz-fta-file-pane-file-name-color)`
Default:
<span class="col-sqr" style="background-color: #6f768599"
></span
>#6f768599

#### Disable folder icons

CSSVariable(s) targeted:`var(--flexcyon-oz-folder-icons-disabled)`
Default:false(de clase)

#### Disable file tree header

CSSVariable(s) targeted:`var(--flexcyon-oz-file-tree-header-disabled)`
Default:false(de clase)

#### Enable Alternate folder count

CSSVariable(s) targeted:`var(--flexcyon-oz-alternate-folder-count)`
Default:false(de clase)

#### Enabled dimmed file extensions in file tree

CSSVariable(s) targeted:`var(--flexcyon-oz-dimmed-file-exts-enabled)`
Default:true(de clase)

___

### Full Calendar

Formatos aceptados: x.y, %

#### Opacity of dimmed full calendar items

CSSVariables(s) dirigidas:`var(--flexcyon-fc-dimmed-items-opacity)`
Default: 0.89

<span style="opacity: 0.89"
>Opacidad de la muestra de elementos de calendario completo</span>

___

### Dataview

Formatos aceptados: px

#### Horizontal padding of dataview error messages

CSSVariables(s) dirigidas:`var(--flexcyon-dataview-horizontal-padding)`
Predeterminado: 8 (px)

___

### Canvas

Define estilos para el plugin Canvas núcleo.
.

Formatos aceptados: px, RGB

#### Blur inactive Canvas nodes

CSSVariable(s) targeted:`var(--flexcyon-canvas-blur-inactive-nodes)`
Default:false(de clase)

#### Blur intensity for inactive nodes

Utilizado con el ajuste anterior para establecer la intensidad de borda de los nodos de tela inactivos
y todas las flechas/edges.
.

CSSVariable(s) targeted:`var(--flexcyon-canvas-blur-intensity)`
Predeterminado: 1 (px)

#### Canvas card menu alignment

Configurar la alineación del menú de la tarjeta de lienzo.
.

CSSClasse(s) targeted:`.flexcyon-canvas-menu-bottom-left,`
`
.flexcyon-anvas-menu-bottom-right, .flexcyon-canvas-menu-top-center,
,
.flexcyon-anvas-menu-top-left, .flexcyon-canvas-menu-top-right,
,
.flexcyon-anvas-menu-lcenter-center, .flexcyon-anvas-menu-lcenter-top,
,
.flexcyon-anvas-menu-lcenter-bottom, .flexcyon-canvas-menu-rcenter-center,
,
.flexcyon-anvas-menu-rcenter-top, .flexcyon-canvas-menu-rcenter-bottom, .flexcyon-canvas-menu-recenter-align
`
Default: none (class select)

Opciones:

- El fondo izquierdo

- Bien.

- Topcenter

- Arriba a la izquierda

- Arriba derecho

- A la izquierda alineadacenter

- Izquierda alineada superior

- Izquierda alineada

- Bien alineadocenter

- Bien alineado superior

- Al fondo alineado

- Bien alineadocenteralign

___

### Various Complements
#### Vertical Suggestion Padding
CSSVariable(s) targeted:`var(--flexcyon-var-comps-sugg-vert-padding)`
Predeterminado: 7 (px)

#### Horizontal Suggestion Padding
CSSVariable(s) targeted:`var(--flexcyon-var-comps-sugg-horiz-padding)`
Predeterminado: 12 (px)

#### Compact Suggestion Mode
Supera los defectos. Usa el relleno 4px 8px.
.

CSSVariable(s) targeted:`var(--flexcyon-var-comps-compact-mode)`
Default:false(de clase)

___
### Omnisearch

#### Disable Omnisearch Icons

CSSClasse(s) targeted:`var(--flexcyon-omnisearch-no-icons)`
Default:false(de clase)

#### Omnisearch Body Left Margin

CSSClasse(s) targeted:`var(--flexcyon-omnisearch-body-margin-left-margin-left)`
Default:1.5 (rem)
