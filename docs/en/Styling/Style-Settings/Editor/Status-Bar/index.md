---
title: Status Bar
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

### Status Bar

#### Hide until trigger

CSS Classe(s) targeted: `.flexcyon-status-hide-until-hover
.flexcyon-status-hide-until-hold`

Default: none (Class select)

Options:

- Hide until hover
- Hide until hold

#### Status bar alignment
CSS Classe(s) targeted: `.flexcyon-status-right-align
.flexcyon-status-centre-align`

Default: none (Class select)

Options:

- Centre
- Right

Left align was removed as it was too hardcoded.

#### Text when hide until hover enabled

CSS Variable(s) targeted: `var(--flexcyon-status-hide-until-hover-text)`

Default: "Show status"

#### Translation for showing status bar on hover

CSS Variable(s) targeted: `var(--flexcyon-status-hide-until-hover-translation)`

Default: 1500 (px)

#### Transition duration for showing status bar on hover

CSS Variable(s) targeted: `var(--flexcyon-status-hide-hover-duration)`

Default: 0.325 (s)

#### Transition timing function for showing status bar on hover

CSS Variable(s) targeted: `var(--flexcyon-status-hide-hover-function)`

Default: ease-out

___
### Text Configuration

#### Use text instead of icons for mode status

CSS Variable(s) targeted: `var(--flexcyon-status-text-mode)`

Default: false (class toggle)

#### Reading Mode Text

CSS Variable(s) targeted: `var(--flexcyon-status-reading-text)`

Default: "READ"

#### Source Mode Text

CSS Variable(s) targeted: `var(--flexcyon-status-source-text)`

Default: "SOURCE"

#### Live Preview Mode Text

CSS Variable(s) targeted: `var(--flexcyon-status-live-text)`

Default: "LIVE"

___

### Status Bar Styling

#### Show status bar on mobile

CSS Variable(s) targeted: `var(--flexcyon-status-mobile-enabled)`

Default: false (class toggle)

#### Status bar font size

CSS Variable(s) targeted: `var(--status-bar-font-size)`

Default: 13.7533 (px)

#### Select status bar style

CSS Classe(s) targeted: `.flexcyon-status-style-angled,
.flexcyon-status-style-card, .flexcyon-status-style-pl10k`

Default: none (class select)

Options:

- Angled
- Cards
- Powerlevel10k

#### Enable status text color

CSS Variable(s) targeted: `var(--flexcyon-status-text-enable-color)`

Default: false (class toggle)
