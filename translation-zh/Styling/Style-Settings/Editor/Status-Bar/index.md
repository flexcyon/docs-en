---
title: 状态栏
icon: material/state-machine
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

目标CSS变量:`var(--flexcyon-status-hide-until-hover)`

默认 :false(类切换)

#### Text when hide until hover enabled

目标CSS变量:`var(--flexcyon-status-hide-until-hover-text)`

Default: "Show status"

#### Translation for showing status bar on hover

目标CSS变量:`var(--flexcyon-status-hide-until-hover-translation)`

Default: 1500px

#### Transition duration for showing status bar on hover

目标CSS变量:`var(--flexcyon-status-hide-hover-duration)`

Default: 0.35 (s)

#### Transition timing function for showing status bar on hover

目标CSS变量:`var(--flexcyon-status-hide-hover-function)`

默认 :ease-out

 
### Text Configuration

#### Use text instead of icons for mode status

目标CSS变量:`var(--flexcyon-status-text-mode)`

默认 :false(类切换)

#### Reading Mode Text

目标CSS变量:`var(--flexcyon-status-reading-text)`

Default: "READ"

#### Source Mode Text

目标CSS变量:`var(--flexcyon-status-source-text)`

Default: "SOURCE"

#### Live Preview Mode Text

目标CSS变量:`var(--flexcyon-status-live-text)`

Default: "LIVE"

 

### Status Bar Styling

#### Show status bar on mobile

目标CSS变量:`var(--flexcyon-status-mobile-enabled)`

默认 :false(类切换)

#### Status bar font size

目标CSS变量:`var(--status-bar-font-size)`

Default: 12.5 (px)

#### Select status bar style

CSS Classe(s) targeted: `.flexcyon-status-style-angled,
.flexcyon-status-style-card, .flexcyon-status-style-pl10k`

默认: 无( 类选择)
选项 :

- Angled
- Cards
- Powerlevel10k

#### Enable status text color

目标CSS变量:`var(--flexcyon-status-text-enable-color)`

默认 :false(类切换)

