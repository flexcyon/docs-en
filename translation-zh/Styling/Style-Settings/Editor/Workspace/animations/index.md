---
title: 动画
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
|   |   |-- Workspace
|   |   |   |-- ...
|   |   |   |-- Animations
|   |   |   |-- ...
|   |   |-- ...
|   |-- ...
|-- ...
```

## Configuration Options

### Animation type

CSS Classe(s) targeted: `.flexcyon-anims-slide-rtl, .flexcyon-anims-slide-ltr,
.flexcyon-anims-slide-tb, .flexcyon-anims-slide-bt, .flexcyon-anims-spin-bt, .flexcyon-anims-spin-rl`
> Changes may need an app reload/restart to take effect

默认: 无( 类选择)
Options: 

- Slide in Left to Right
- Slide in Right to Left
- Slide in Top to Bottom
- Rotate in Bottom to Top
- Rotate in Right to Left

### Animation duration

目标CSS变量:`var(--flexcyon-anim-duration)`

默认: 0. 5s

### Animation easing function

目标CSS变量:`var(--flexcyon-anim-easing)`

默认 :ease-in-out

