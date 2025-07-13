---
title: Status Bar
icon: material/state-machine
---

DefinesCSSvariables para configurar la barra de estado

Formatos aceptados: s, px

## Navigation

```md
Style Settings
|-- 。
|-- Flexcyon Style Settings
|   |-- Editor
|   |   |-- 。
|   |   |-- Status Bar
|   |   |-- 。
|   |-- 。
|-- 。
```

## Opciones de configuración

### Status Bar Hide until Hover

##### Escóndete hasta el buceador

CSSVariable(s) targeted:`var(--flexcyon-status-hide-until-hover)`
Default:false(de clase)

##### Texto cuando se esconde hasta que se haya habilitado el soporte

CSSVariable(s) targeted:`var(--flexcyon-status-hide-until-hover-text)`
Predeterminado: "Mostrar estado"

### Traducción para mostrar la barra de estado en la palanca

CSSVariable(s) targeted:`var(--flexcyon-status-hide-until-hover-translation)`
Predeterminado: 1500px

#### Duración de la transición para mostrar la barra de estado en la palanca

CSSVariable(s) targeted:`var(--flexcyon-status-hide-hover-duration)`
Default: 0.35 (s)

#### Función de sincronización de transición para mostrar barra de estado en el aparador

CSSVariable(s) targeted:`var(--flexcyon-status-hide-hover-function)`
Default:ease-out

___
### Configuración de texto

##### Use texto en lugar de iconos para el estado de modo

CSSVariable(s) targeted:`var(--flexcyon-status-text-mode)`
Default:false(de clase)

##### Texto del modo lectura

CSSVariable(s) targeted:`var(--flexcyon-status-reading-text)`
Default: "READ"

##### Texto del Modo Fuente

CSSVariable(s) targeted:`var(--flexcyon-status-source-text)`
Default: "SOURCE"

#### Live Preview Mode Text

CSSVariable(s) targeted:`var(--flexcyon-status-live-text)`
Default: "LIVE"

___

### Status Bar Styling

##### Mostrar la barra de estado en móvil

CSSVariable(s) targeted:`var(--flexcyon-status-mobile-enabled)`
Default:false(de clase)

##### Tamaño de la fuente de la barra de estado

CSSVariable(s) targeted:`var(--status-bar-font-size)`
Predeterminado: 12.5 (px)

##### Seleccione estilo de barra de estado

CSSClasse(s) targeted: `.flexcyon-tatus-style-angled,
,
.flexcyon-tatus-style-card, .flexcyon-status-style-pl10k`
Default: none (class select)
Opciones:

- Angled
- Tarjetas
- Powerlevel10k

##### Color de texto de estado habilitado

CSSVariable(s) targeted:`var(--flexcyon-status-text-enable-color)`
Default:false(de clase)

