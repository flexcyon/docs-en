---
title: 动画
---

配置提示模态和选项卡容器的过渡动画. 

接受的格式: ms

## 导航

```md
Style Settings
|-- flexcyon://Editor
|   |-- Animations
```

## 配置选项

### 笔记动画类型

目标 CSS 类: 

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

默认: Fade in (淡入) (类选项)

选项:

- None (无)

- Fade In (淡入)
- Scale Up (扩大)
- Pop In (弹出)
- Pulse In (脉冲)

- Slide Left to Right (从左向右滑动)
- Slide Right to Left (从右向左滑动)
- Slide Top to Bottom (从上到下滑动)
- Slide Bottom to Top (从下往上滑动)
- Slide Top-Left (左上滑动)
- Slide Top-Right (右上滑动)
- Slide Bottom-Left (左下滑动)
- Slide Bottom-Right (右下滑动)

- Spin Right to Left (从右向左旋转)
- Spin Left to Right (从左向右旋转)
- Spin Bottom to Top (从下到上旋转)
- Spin Top to Bottom (从上到下旋转)
- Flip Horizontal (X-Axis) [水平翻转 (X轴)]
- Flip Vertical (Y-Axis) [垂直翻转 (Y轴)]

- Blur In (Depth of Field) [模糊 (景深)]
- Bounce In (跳进去)
- Swing In (旋入)

- Glide In (滑入)
- Glide Out (滑出)
- Aura Glow (光环发光)
- TV Effect (Retro CRT) [电视效果 (复古 CRT)]
- Apparition (幻影)

### 模态动画类型

目标 CSS 类: 

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

默认: Pulse In (脉冲) (类选项)

选项:

- None (无)

- Fade In (淡入)
- Scale Up (扩大)
- Pop In (弹出)
- Pulse In (脉冲)

- Slide Left to Right (从左向右滑动)
- Slide Right to Left (从右向左滑动)
- Slide Top to Bottom (从上到下滑动)
- Slide Bottom to Top (从下往上滑动)
- Slide Top-Left (左上滑动)
- Slide Top-Right (右上滑动)
- Slide Bottom-Left (左下滑动)
- Slide Bottom-Right (右下滑动)

- Spin Right to Left (从右向左旋转)
- Spin Left to Right (从左向右旋转)
- Spin Bottom to Top (从下到上旋转)
- Spin Top to Bottom (从上到下旋转)
- Flip Horizontal (X-Axis) [水平翻转 (X轴)]
- Flip Vertical (Y-Axis) [垂直翻转 (Y轴)]

- Blur In (Depth of Field) [模糊 (景深)]
- Bounce In (跳进去)
- Swing In (旋入)

- Glide In (滑入)
- Glide Out (滑出)
- Aura Glow (光环发光)
- TV Effect (Retro CRT) [电视效果 (复古 CRT)]
- Apparition (幻影)

### 动画持续时间

目标 CSS 变量: `var(--flexcyon-anim-duration)`

默认: 300 (ms)

### 动画缓动函数

目标 CSS 变量: `var(--flexcyon-anim-easing)`

默认: ease-in-out

### 动画滑动量

滑动动画的滑动量. 

目标 CSS 变量: `var(--flexcyon-anim-slide-amount)`

默认: 56.6311 (px)

### 样式设置容器中启用动画

目标 CSS 变量: `var(--flexcyon-anim-style-settings-contain)`

默认: false

### 缩放动画初始缩放

目标 CSS 变量: `var(--flexcyon-anim-start-scale-amt)`

默认: 0.33
