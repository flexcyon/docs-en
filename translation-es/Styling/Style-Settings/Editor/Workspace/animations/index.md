---
title: Animaciones
icon: material/animation
---

Configurar animaciones de transición de los impulsos, modales y tab container.

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

## Opciones de configuración

### Animation type

CSSClasse(s) targeted: `.flexcyon-nims-slide-rtl, .flexcyon-anims-slide-ltr,
,
.flexcyon-nims-slide-tb, .flexcyon-anims-slide-bt, .flexcyon-anims-spin-bt, .flexcyon-anims-spin-rl`
> Los cambios pueden necesitar una nueva descarga de la aplicación/restaurante para tener efecto

Predeterminado: ninguno (clase selecto)
Opciones:

- Diapositiva de izquierda a derecha
- Diapositiva en derecho a la izquierda
- Diapositiva en Top to Bottom
- Girar en el fondo para arriba
- Girar en la derecha a la izquierda

### Duración de la animación

CSSVariable(s) targeted:`var(--flexcyon-anim-duration)`
Predeterminado: 0.5s

### Función de estimulación

CSSVariable(s) targeted:`var(--flexcyon-anim-easing)`
Default:ease-in-out

