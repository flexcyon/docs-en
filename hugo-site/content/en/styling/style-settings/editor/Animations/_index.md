---
title: Animations
---

Configure transition animations of prompts, modals and tab container.

Accepted Formats: ms

## Navigation

```md
Style Settings
|-- flexcyon://Editor
|   |-- Animations
```

## Configuration Options

### Note Animation type

CSS Classe(s) targeted: 

`.flexcyon-anims-fade-in, .flexcyon-anims-scale-up,
.flexcyon-anims-pop-in, .flexcyon-anims-pulse-in`,

`.flexcyon-anims-slide-ltr, .flexcyon-anims-slide-rtl, 
.flexcyon-anims-slide-tb, .flexcyon-anims-slide-bt,
.flexcyon-anims-slide-tl, .flexcyon-anims-slide-tr,
.flexcyon-anims-slide-bl, .flexcyon-anims-slide-br`,

`.flexcyon-anims-spin-rl, .flexcyon-anims-spin-lr,
.flexcyon-anims-spin-bt, .flexcyon-anims-spin-tb,
.flexcyon-anims-flip-x, .flexcyon-anims-flip-y`,

`.flexcyon-anims-blur-in, .flexcyon-anims-bounce-in,
.flexcyon-anims-swing-in`,

`.flexcyon-anims-glide-in, .flexcyon-anims-aura-glow,
.flexcyon-anims-tv-effect, .flexcyon-anims-apparition`,

Default: Fade In (class select)

Options:

- None

- Fade In
- Scale Up
- Pop In (Spring)
- Pulse In

- Slide Left to Right
- Slide Right to Left
- Slide Top to Bottom
- Slide Bottom to Top
- Slide Top-Left
- Slide Top-Right
- Slide Bottom-Left
- Slide Bottom-Right

- Spin Right to Left
- Spin Left to Right
- Spin Bottom to Top
- Spin Top to Bottom
- Flip Horizontal (X-Axis)
- Flip Vertical (Y-Axis)

- Blur In (Depth of Field)
- Bounce In
- Swing In

- Glide In
- Glide Out
- Aura Glow
- TV Effect (Retro CRT)
- Apparition

### Modal Animation type

CSS Classe(s) targeted: 

`.flexcyon-modal-anims-fade-in, .flexcyon-modal-anims-scale-up,
.flexcyon-modal-anims-pop-in, .flexcyon-modal-anims-pulse-in`,

`.flexcyon-modal-anims-slide-ltr, .flexcyon-modal-anims-slide-rtl, 
.flexcyon-modal-anims-slide-tb, .flexcyon-modal-anims-slide-bt,
.flexcyon-modal-anims-slide-tl, .flexcyon-modal-anims-slide-tr,
.flexcyon-modal-anims-slide-bl, .flexcyon-modal-anims-slide-br`,

`.flexcyon-modal-anims-spin-rl, .flexcyon-modal-anims-spin-lr,
.flexcyon-modal-anims-spin-bt, .flexcyon-modal-anims-spin-tb,
.flexcyon-modal-anims-flip-x, .flexcyon-modal-anims-flip-y`,

`.flexcyon-modal-anims-blur-in, .flexcyon-modal-anims-bounce-in,
.flexcyon-modal-anims-swing-in`,

`.flexcyon-modal-anims-glide-in, .flexcyon-modal-anims-aura-glow,
.flexcyon-modal-anims-tv-effect, .flexcyon-modal-anims-apparition`,

Default: Pulse In (class select)

Options:

- None

- Fade In
- Scale Up
- Pop In (Spring)
- Pulse In

- Slide Left to Right
- Slide Right to Left
- Slide Top to Bottom
- Slide Bottom to Top
- Slide Top-Left
- Slide Top-Right
- Slide Bottom-Left
- Slide Bottom-Right

- Spin Right to Left
- Spin Left to Right
- Spin Bottom to Top
- Spin Top to Bottom
- Flip Horizontal (X-Axis)
- Flip Vertical (Y-Axis)

- Blur In (Depth of Field)
- Bounce In
- Swing In

- Glide In
- Glide Out
- Aura Glow
- TV Effect (Retro CRT)
- Apparition

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
