---
title: 状态栏
icon: material/state-machine
---

定义用于配置状态栏的 CSS 变量

接受格式: s, px

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

默认: 1500px

#### Transition duration for showing status bar on hover
目标CSS变量:`var(--flexcyon-status-hide-hover-duration)`

默认: 0.35(s)

#### Transition timing function for showing status bar on hover
目标CSS变量:`var(--flexcyon-status-hide-hover-function)`

默认 :ease-out

___ 
### Text Configuration

#### Use text instead of icons for mode status
目标CSS变量:`var(--flexcyon-status-text-mode)`

默认 :false(类切换)

#### Reading Mode Text
目标CSS变量:`var(--flexcyon-status-reading-text)`

默认: "READ"

#### Source Mode Text
目标CSS变量:`var(--flexcyon-status-source-text)`

默认: "SOURCE"

#### Live Preview Mode Text
目标CSS变量:`var(--flexcyon-status-live-text)`

默认: "LIVE"

___ 
### Status Bar Styling

#### Show status bar on mobile
目标CSS变量:`var(--flexcyon-status-mobile-enabled)`

默认 :false(类切换)

#### Status bar font size
目标CSS变量:`var(--status-bar-font-size)`

默认: 12.5 (px)

#### Select status bar style
CSS类目标:`.flexcyon-status-style-angled, .flexcyon-status-style-card, .flexcyon-status-style-pl10k`

默认: 无( 选择类)
选项 :
- 倾斜
- 卡片
- Powerlevel10k

#### Enable status text color
目标CSS变量:`var(--flexcyon-status-text-enable-color)`

默认 :false(类切换)