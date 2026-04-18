---
title: Animations
icon: material/animation
---

Configure transition animations of prompts, modals and tab container.

Accepted Formats: ms

## Navigation

```md
Style Settings
|-- ...
|-- Flexcyon Style Settings
|   |-- Editor
|   |   |-- ...
|   |   |-- Animations
|   |   |-- ...
|   |-- ...
|-- ...
```

## Configuration Options

### Note Animation type

CSS Classe(s) targeted: `.flexcyon-anims-slide-rtl, .flexcyon-anims-slide-ltr,
.flexcyon-anims-slide-tb, .flexcyon-anims-slide-bt, .flexcyon-anims-spin-bt, .flexcyon-anims-spin-rl, .flexcyon-anims-scale-up`
> Changes may need an app reload/restart to take effect

Default: none (class select)

Options:

- Slide in Left to Right
- Slide in Right to Left
- Slide in Top to Bottom
- Rotate in Bottom to Top
- Rotate in Right to Left
- Scale Up
- Fade In

### Modal Animation type

CSS Classe(s) targeted: `.flexcyon-modal-anims-slide-rtl, .flexcyon-modal-anims-slide-ltr,
.flexcyon-modal-anims-slide-tb, .flexcyon-modal-anims-slide-bt, .flexcyon-modal-anims-spin-bt, .flexcyon-modal-anims-spin-rl, .flexcyon-modal-anims-scale-up`
> Changes may need an app reload/restart to take effect

Default: none (class select)

Options:

- Slide in Left to Right
- Slide in Right to Left
- Slide in Top to Bottom
- Rotate in Bottom to Top
- Rotate in Right to Left
- Scale Up
- Fade In

### Animation duration

CSS Variable(s) targeted: `var(--flexcyon-anim-duration)`

Default: 300 (ms)

### Animation easing function

CSS Variable(s) targeted: `var(--flexcyon-anim-easing)`

Default: ease-in

### Animation slide amount
The amount of pixels the slide animations will slide

CSS Variable(s) targeted: `var(--flexcyon-anim-slide-amount)`

Default: 56.6311 (px)

### Enable Animations in Style Settings Container

CSS Variable(s) targeted: `var(--flexcyon-anim-style-settings-contain)`

Default: false

### Scale animation initial scaling

CSS Variable(s) targeted: `var(--flexcyon-anim-start-scale-amt)`

Default: 0.33

### Animation initial opacity

CSS Variable(s) targeted: `var(--flexcyon-anim-start-opacity)`

Default: 0.55
