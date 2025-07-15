---
title: 状态栏
icon: material/state-machine
---

定义CSS用于配置状态栏的变量

接受格式: s, px

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

CSS目标变量:`var(--flexcyon-status-hide-until-hover)`
默认 :false(类切换)

#### Text when hide until hover enabled

CSS目标变量:`var(--flexcyon-status-hide-until-hover-text)`
默认: “ 显示状态 ”

#### Translation for showing status bar on hover

CSS目标变量:`var(--flexcyon-status-hide-until-hover-translation)`
默认: 1500px

#### Transition duration for showing status bar on hover

CSS目标变量:`var(--flexcyon-status-hide-hover-duration)`
默认: 0.35(s)

#### Transition timing function for showing status bar on hover

CSS目标变量:`var(--flexcyon-status-hide-hover-function)`
默认 :ease-out

 
### Text Configuration

#### Use text instead of icons for mode status

CSS目标变量:`var(--flexcyon-status-text-mode)`
默认 :false(类切换)

#### Reading Mode Text

CSS目标变量:`var(--flexcyon-status-reading-text)`
默认: "READ"

#### Source Mode Text

CSS目标变量:`var(--flexcyon-status-source-text)`
默认: "资源"

#### Live Preview Mode Text

CSS目标变量:`var(--flexcyon-status-live-text)`
默认: "LIVE"

 

### Status Bar Styling

#### Show status bar on mobile

CSS目标变量:`var(--flexcyon-status-mobile-enabled)`
默认 :false(类切换)

#### Status bar font size

CSS目标变量:`var(--status-bar-font-size)`
默认: 12.5 (px)

#### Select status bar style

CSS目标类别:`.lexcyon-status-states-trounded,
,
.flexcyon-status-style-card,.flexcyon-status-style-pl10k ' .

默认: 无( 选择类)
选项 :

- 愤怒的
- 纸牌
- 动力级10k

#### Enable status text color

CSS目标变量:`var(--flexcyon-status-text-enable-color)`
默认 :false(类切换)

