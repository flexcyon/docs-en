---
title: 动画
icon: material/animation
---

配置提示、模式和标签容器的过渡动画。
.

接受格式:s

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

CSS 类目标:`.flexcyon-anims-slip-rtl,.flexcyon-anims-slip-ltr,
,
.flexcyon-anims-slim-tb,.flexcyon-anims-slim-bt,.flexcyon-spin-bt,.flexcyon-anims-spin-rl ' .
> Changes may need an app reload/restart to take effect

默认: 无( 类选择)
选项 :

- 左到右幻灯片
- 向左滑动
- 从上到下幻灯片
- 从下到上旋转
- 向左旋转

### Animation duration

目标CSS变量:`var(--flexcyon-anim-duration)`

默认: 0. 5s

### Animation easing function

目标CSS变量:`var(--flexcyon-anim-easing)`

默认 :ease-in-out

