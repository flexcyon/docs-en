---
title: 动画
icon: material/animation
---

配置提示,模式和标签容器的过渡动画。
.

接受格式:s

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

CSS目标类别:`.flexcyon-anims-slip-rtl,.flexcyon-anims-slip-ltr,
,
.flexcyon-anims-slim-tb,.flexcyon-anims-slim-bt,.flexcyon-spin-bt,.flexcyon-anims-spin-rl ' .
> 更改可能需要重新装入/ 重新启动程序才能生效

默认: 无( 选择类)
选项 :

- 左到右幻灯片
- 向左滑动
- 从上到下幻灯片
- 从下到上旋转
- 向左旋转

### Animation duration

CSS目标变量:`var(--flexcyon-anim-duration)`
默认值: 0. 5s

### Animation easing function

CSS目标变量:`var(--flexcyon-anim-easing)`
默认 :ease-in-out

