---
title: Plugins
icon: material/hexagon-outline
---

Para la configuración de plugins compatibles oficialmente

Formatos aceptados: HEX, rem, x.y, %

## Navigation

```md
Style Settings
|-- ...
|-- Flexcyon Style Settings
|   |-- ...
|   |-- Plugins
|   |-- ...
```

## Configuration Options

### Alternate file tree

#### Folders font size

CSS Variable(s) targeted:`var(--oz-fta-folder-font-size)`

Default: 0.925 (rem)

<span style="font-size: 0.925rem"
>Muestra Árbol de archivo alternativo Folders tamaño de la fuente</span>

#### Folders font color

CSS Variable(s) targeted:`var(--oz-fta-folder-pane-file-name-color)`

Default (modo de luz):
<span class="col-sqr" style="background-color: #080808"
></span
>#080808

Default (modo oscuro):
<span class="col-sqr" style="background-color: #d3d5d3"
></span
>#d3d5d3

#### Active folder color

CSS Variables(s) targeted:`var(--oz-fta-all-panes-active-text-color)`

Default (modo de luz):
<span class="col-sqr" style="background-color: #080808"
></span
>#080808

Default (modo oscuro):
<span class="col-sqr" style="background-color: #d3d5d3"
></span
>#d3d5d3

#### Files font size

CSS Variable(s) targeted:`var(--oz-fta-file-font-size)`

Predeterminado: 0.9 (rem)

<span style="font-size: 0.9rem"
>Muestra Árbol de archivos alternativos tamaño de fuente</san>

#### Files font color

CSS Variable(s) targeted:`var(--oz-fta-file-pane-file-name-color)`

Default:
<span class="col-sqr" style="background-color: #6f768599"
></span
>#6f768599

#### Disable folder icons

CSS Variable(s) targeted:`var(--flexcyon-oz-folder-icons-disabled)`

Default:false(de clase)

#### Disable file tree header

CSS Variable(s) targeted:`var(--flexcyon-oz-file-tree-header-disabled)`

Default:false(de clase)

#### Enable Alternate folder count

CSS Variable(s) targeted:`var(--flexcyon-oz-alternate-folder-count)`

Default:false(de clase)

#### Enabled dimmed file extensions in file tree

CSS Variable(s) targeted:`var(--flexcyon-oz-dimmed-file-exts-enabled)`

Default:true(de clase)

__

### Full Calendar

Formatos aceptados: x.y, %

#### Opacity of dimmed full calendar items

CSS Variables(s) targeted:`var(--flexcyon-fc-dimmed-items-opacity)`

Predeterminado: 0.89

<span style="opacity: 0.89"
>Opacidad de muestra de elementos de calendario completo</span>

__

### Dataview

Formatos aceptados: px

#### Horizontal padding of dataview error messages

CSS Variables(s) targeted:`var(--flexcyon-dataview-horizontal-padding)`

Predeterminado: 8 (px)

__

### Canvas

Define estilos para el plugin Canvas núcleo.
.

Formatos aceptados: px, RGB

#### Blur inactive Canvas nodes

CSS Variable(s) targeted:`var(--flexcyon-canvas-blur-inactive-nodes)`

Default:false(de clase)

#### Blur intensity for inactive nodes

Usado con el ajuste anterior para establecer la intensidad de borda de los nodos de tela inactivos
y todas las flechas/edges.
.

CSS Variable(s) targeted:`var(--flexcyon-canvas-blur-intensity)`

Predeterminado: 1 (px)

#### Canvas card menu alignment

Configurar la alineación del menú de la tarjeta de lienzo.
.

CSS Classe(s) targeted:`.flexcyon-canvas-menu-bottom-left,`
`
.flexcyon-canvas-menu-bottom-right, .flexcyon-canvas-menu-top-center,
,
.flexcyon-canvas-menu-top-left, .flexcyon-canvas-menu-top-right,
,
.flexcyon-canvas-menu-lcenter-center, .flexcyon-canvas-menu-lcenter-top,
,
.flexcyon-canvas-menu-lcenter-bottom, .flexcyon-canvas-menu-rcenter-center,
,
.flexcyon-canvas-menu-rcenter-top, .flexcyon-canvas-menu-rcenter-bottom, .flexcyon-canvas-menu-recenter-align
`

Predeterminado: ninguno (clase selecto)

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

