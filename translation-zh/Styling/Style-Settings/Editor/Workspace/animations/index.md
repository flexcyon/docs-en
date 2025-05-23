---
title: 动画
icon: material/animation
---

配置提示、模式和标签容器的过渡动画。

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
CSS类目标:`.flexcyon-anims-slide-rtl, .flexcyon-anims-slide-ltr, .flexcyon-anims-slide-tb, .flexcyon-anims-slide-bt, .flexcyon-anims-spin-bt, .flexcyon-anims-spin-rl`
> Changes may need an app reload/restart to take effect

默认: 无( 选择类)
选项 :
- 左到右幻灯片
- 向左滑动
- 从上到下幻灯片
- 从下到上旋转
- 向左旋转

### Animation duration
目标CSS变量:`var(--flexcyon-anim-duration)`

默认: 0.5s

### Animation easing function
目标CSS变量:`var(--flexcyon-anim-easing)`

默认 :ease-in-out