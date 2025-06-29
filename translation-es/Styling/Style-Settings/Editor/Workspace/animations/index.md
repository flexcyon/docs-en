---
title: Animations
icon: material/animation
---

Configurar animaciones de transición de los impulsos, modales y tab container.

Formatos aceptados: s

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
,
.flexcyon-anims-slide-tb, .flexcyon-anims-slide-bt, .flexcyon-anims-spin-bt, .flexcyon-anims-spin-rl`
> Changes may need an app reload/restart to take effect

Predeterminado: ninguno (clase selecto)
Opciones:

- Diapositiva de izquierda a derecha
- Diapositiva en derecho a la izquierda
- Diapositiva en Top to Bottom
- Girar en el fondo para arriba
- Girar en la derecha a la izquierda

### Animation duration

CSS Variable(s) targeted:`var(--flexcyon-anim-duration)`

Predeterminado: 0.5s

### Animation easing function

CSS Variable(s) targeted:`var(--flexcyon-anim-easing)`

Default:ease-in-out

