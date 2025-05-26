---
title: 。icon: material/state-machine
---

Defines CSS variables to configure the status bar

Accepted Formats: s, px

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

。CSS。:`var(--flexcyon-status-hide-until-hover)`

。:false(。)

#### Text when hide until hover enabled

。CSS。:`var(--flexcyon-status-hide-until-hover-text)`

Default: "Show status"

#### Translation for showing status bar on hover

。CSS。:`var(--flexcyon-status-hide-until-hover-translation)`

Default: 1500px

#### Transition duration for showing status bar on hover

。CSS。:`var(--flexcyon-status-hide-hover-duration)`

Default: 0.35 (s)

#### Transition timing function for showing status bar on hover

。CSS。:`var(--flexcyon-status-hide-hover-function)`

。:ease-out

 
### Text Configuration

#### Use text instead of icons for mode status

。CSS。:`var(--flexcyon-status-text-mode)`

。:false(。)

#### Reading Mode Text

。CSS。:`var(--flexcyon-status-reading-text)`

Default: "READ"

#### Source Mode Text

。CSS。:`var(--flexcyon-status-source-text)`

Default: "SOURCE"

#### Live Preview Mode Text

。CSS。:`var(--flexcyon-status-live-text)`

Default: "LIVE"

 

### Status Bar Styling

#### Show status bar on mobile

。CSS。:`var(--flexcyon-status-mobile-enabled)`

。:false(。)

#### Status bar font size

。CSS。:`var(--status-bar-font-size)`

Default: 12.5 (px)

#### Select status bar style

CSS Classe(s) targeted: `.flexcyon-status-style-angled,
.flexcyon-status-style-card, .flexcyon-status-style-pl10k`

。: 无( 。)
。:

- Angled
- Cards
- Powerlevel10k

#### Enable status text color

。CSS。:`var(--flexcyon-status-text-enable-color)`

。:false(。)

