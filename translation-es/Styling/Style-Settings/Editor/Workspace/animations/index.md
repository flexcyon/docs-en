---
title: Animaciones
icon: material/animation
---

Configure animaciones de transición de los impulsos, modales y tab container.
.

Formatos aceptados: s

## Navigation

```md
Style Settings
|-- 。
|-- Flexcyon Style Settings
|   |-- Editor
|   |   |-- 。
|   |   |-- Workspace
|   |   |   |-- 。
|   |   |   |-- Animations
|   |   |   |-- 。
|   |   |-- 。
|   |-- 。
|-- 。
```

## Configuration Options

### Animation type

CSSClasse(s) targeted: `.flexcyon-nims-slide-rtl, .flexcyon-anims-slide-ltr,
,
.flexcyon-nims-slide-tb, .flexcyon-anims-slide-bt, .flexcyon-anims-spin-bt, .flexcyon-anims-spin-rl, .flexcyon-anims-scale-up`
> Los cambios pueden necesitar una nueva descarga de la aplicación/restaurante para tener efecto

Default: none (class select)
Opciones:

- Diapositiva de izquierda a derecha
- Diapositiva en derecho a la izquierda
- Diapositiva en Top to Bottom
- Girar en el fondo para arriba
- Girar en la derecha a la izquierda
- Escala arriba

### Animation duration

CSSVariable(s) targeted:`var(--flexcyon-anim-duration)`
Predeterminado: 0.3s

### Animation easing function

CSSVariable(s) targeted:`var(--flexcyon-anim-easing)`
Predeterminado: facilidad-n

### Animation slide amount
La cantidad de píxeles las animaciones de diapositivas se deslizarán

CSSVariable(s) targeted:`var(--flexcyon-anim-slide-amount)`
Default: 56.63105 (px)

