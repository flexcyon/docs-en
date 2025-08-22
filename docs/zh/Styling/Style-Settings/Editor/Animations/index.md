---
title: Animations
icon: material/animation
---

配置提示模态和选项卡容器的过渡动画。

接受的格式: s

## 导航

```md
Style Settings
|-- ...
|-- Flexcyon Style Settings
| |-- Editor
| | |-- ...
| | |-- Animations
| | |-- ...
| |-- ...
|-- ...
```

## 配置选项

### 动画类型

CSS Classe(s) targeted: `.flexcyon-anims-slide-rtl, .flexcyon-anims-slide-ltr,
.flexcyon-anims-slide-tb, .flexcyon-anims-slide-bt, .flexcyon-anims-spin-bt, .flexcyon-anims-spin-rl, .flexcyon-anims-scale-up`

> 更改可能需要重新加载应用程序或重新启动才能生效

默认: none (类选项)

选项:

- Slide in Left to Right (从左向右滑动)
- Slide in Right to Left (从右向左滑动)
- Slide in Top to Bottom (从上到下滑动)
- Rotate in Bottom to Top (从下到上旋转)
- Rotate in Right to Left (从右向左旋转)
- Scale Up (扩大)

### 动画持续时间

目标 CSS 变量: `var(--flexcyon-anim-duration)`

默认: 0.3s

### 动画缓动函数

目标 CSS 变量: `var(--flexcyon-anim-easing)`

默认: ease-in

### 动画滑动量

滑动动画的滑动量。

目标 CSS 变量: `var(--flexcyon-anim-slide-amount)`

默认: 56.63105 (px)
