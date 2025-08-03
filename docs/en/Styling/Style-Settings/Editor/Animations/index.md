---
title: Animations
icon: material/animation
---

Configure transition animations of prompts, modals and tab container.

Accepted Formats: s

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

### Animation type

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

### Animation duration

CSS Variable(s) targeted: `var(--flexcyon-anim-duration)`

Default: 0.3s

### Animation easing function

CSS Variable(s) targeted: `var(--flexcyon-anim-easing)`

Default: ease-in

### Animation slide amount
The amount of pixels the slide animations will slide

CSS Variable(s) targeted: `var(--flexcyon-anim-slide-amount)`

Default: 56.63105 (px)

