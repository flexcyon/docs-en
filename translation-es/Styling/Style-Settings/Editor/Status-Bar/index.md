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

## Configuration Options

### Status Bar Hide Until Hover

#### Hide until hover

CSSVariable(s) targeted:`var(--flexcyon-status-hide-until-hover)`
Default:false(de clase)

#### Text when hide until hover enabled

CSSVariable(s) targeted:`var(--flexcyon-status-hide-until-hover-text)`
Predeterminado: "Mostrar estado"

#### Translation for showing status bar on hover

CSSVariable(s) targeted:`var(--flexcyon-status-hide-until-hover-translation)`
Predeterminado: 1500px

#### Transition duration for showing status bar on hover

CSSVariable(s) targeted:`var(--flexcyon-status-hide-hover-duration)`
Default: 0.35 (s)

#### Transition timing function for showing status bar on hover

CSSVariable(s) targeted:`var(--flexcyon-status-hide-hover-function)`
Default:ease-out

___
### Text Configuration

#### Use text instead of icons for mode status

CSSVariable(s) targeted:`var(--flexcyon-status-text-mode)`
Default:false(de clase)

#### Reading Mode Text

CSSVariable(s) targeted:`var(--flexcyon-status-reading-text)`
Default: "READ"

#### Source Mode Text

CSSVariable(s) targeted:`var(--flexcyon-status-source-text)`
Default: "SOURCE"

#### Live Preview Mode Text

CSSVariable(s) targeted:`var(--flexcyon-status-live-text)`
Default: "LIVE"

___

### Status Bar Styling

#### Show status bar on mobile

CSSVariable(s) targeted:`var(--flexcyon-status-mobile-enabled)`
Default:false(de clase)

#### Status bar font size

CSSVariable(s) targeted:`var(--status-bar-font-size)`
Predeterminado: 12.5 (px)

#### Select status bar style

CSSClasse(s) targeted: `.flexcyon-tatus-style-angled,
,
.flexcyon-tatus-style-card, .flexcyon-status-style-pl10k`
Default: none (class select)
Opciones:

- Angled
- Tarjetas
- Powerlevel10k

#### Enable status text color

CSSVariable(s) targeted:`var(--flexcyon-status-text-enable-color)`
Default:false(de clase)

