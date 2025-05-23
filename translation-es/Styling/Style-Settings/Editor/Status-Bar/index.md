---
title: Status Bar
icon: material/state-machine
---

Define las variables CSS para configurar la barra de estado

Formatos aceptados: s, px

## Navigation
```md
Style Settings
|-- ...
|-- Flexcyon Style Settings
|   |-- Editor
|   |   |-- ...
|   |   |-- Status Bar
|   |   |-- ...
|   |-- ...
|-- ...
```

## Configuration Options

### Status Bar Hide Until Hover

#### Hide until hover
CSS Variable(s) targeted:`var(--flexcyon-status-hide-until-hover)`

Default:false(de clase)

#### Text when hide until hover enabled
CSS Variable(s) targeted:`var(--flexcyon-status-hide-until-hover-text)`

Predeterminado: "Mostrar estado"

#### Translation for showing status bar on hover
CSS Variable(s) targeted:`var(--flexcyon-status-hide-until-hover-translation)`

Predeterminado: 1500px

#### Transition duration for showing status bar on hover
CSS Variable(s) targeted:`var(--flexcyon-status-hide-hover-duration)`

Default: 0.35 (s)

#### Transition timing function for showing status bar on hover
CSS Variable(s) targeted:`var(--flexcyon-status-hide-hover-function)`

Predeterminado: facilidad de salida

___
### Text Configuration

#### Use text instead of icons for mode status
CSS Variable(s) targeted:`var(--flexcyon-status-text-mode)`

Default:false(de clase)

#### Reading Mode Text
CSS Variable(s) targeted:`var(--flexcyon-status-reading-text)`

Default: "READ"

#### Source Mode Text
CSS Variable(s) targeted:`var(--flexcyon-status-source-text)`

Default: "SOURCE"

#### Live Preview Mode Text
CSS Variable(s) targeted:`var(--flexcyon-status-live-text)`

Default: "LIVE"

___
### Status Bar Styling

#### Show status bar on mobile
CSS Variable(s) targeted:`var(--flexcyon-status-mobile-enabled)`

Default:false(de clase)

#### Status bar font size
CSS Variable(s) targeted:`var(--status-bar-font-size)`

Predeterminado: 12.5 (px)

#### Select status bar style
CSS Classe(s) targeted:`.flexcyon-status-style-angled, .flexcyon-status-style-card, .flexcyon-status-style-pl10k`

Predeterminado: ninguno (clase selecto)
Opciones:
- Angled
- Tarjetas
- Powerlevel10k

#### Enable status text color
CSS Variable(s) targeted:`var(--flexcyon-status-text-enable-color)`

Default:false(de clase)