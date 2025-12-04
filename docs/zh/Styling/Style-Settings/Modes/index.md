---
title: Modes
icon: material/toggle-switch
---

配置 flexcyon 提供的一些独特模式。您还可以在此处配置辅助功能设置。

## 导航

```md
Style Settings
|-- ...
|-- Flexcyon Style Settings
| |-- Modes
| |-- ...
```

## 配置选项

### RTZ 模式

> 受 Shimmering Focus 主题启发的极端极简主义. 大多数 UI 元素在悬停之前不会显示.
> 不推荐在手机上使用. 不适与 Flex Max 模式使用.

目标 CSS 变量: `var(--flexcyon-rtz-mode)`

默认: false (类切换)

### Flex Max 模式

> 一个非常有主见的设置, 展示了这个主题的独特定制, 功能开箱即用. 如果某些选项不太适合您, 您可以禁用此模式并更多地自定义主题, 它将重置主题为全新的自定义. 还有其他启用的默认选项, 您可能喜欢也可能不喜欢. 请参阅下文, 了解它为您启用的选项列表.

> 如果您不知道从哪里开始自定义主题, 建议使用此模式。**若些希望广泛定制主题或不喜欢某些默认设置, 建议不使用此模式**

目标 CSS 变量: `var(--flexcyon-flex-max-mode)`

默认: true (类切换)

### Flex Max 模式启用设置

启用以下设置, 即使在样式设置中已将其关闭。

* 笑脸图标

* 确保社区插件图标优先

* 淡入标签动画

* 从左到右的模态动画

* 样式设置容器中的动画

* ASCII 艺术

* 水平标尺自定义字体

* 受 Powerlevel10k 启发的布局和状态栏风格

* 隐藏直到悬停状态栏

* 当前状态栏编辑模式为文本而非图标

* Vim 模式状态

* 彩色标题

* 扩展调色板

* 文件扩展名变暗

* 换行长文件名

* ASCII 复选框

* Clip Path 复选框

* 设置中的彩色图标

* 社区项目效果

* 在设置中不显示滚动条

* Alternate File Tree 插件的文件扩展名已变暗

* 禁用空状态标题

* 启用侧坞图标效果

* 小写代码块文件扩展名 (Live Preview 模式)

* 为代码块文件扩展名添加前缀 (Live Preview 模式)


您应该能够配置这些设置, 就像它们正常启用一样. 这主题还有许多其他设置选项供您探索, 其中一些默认情况下是启用的, 如平滑光标.

### 全局启用书写模式

> Like its cssclass counterpart, except applied globally

目标 CSS 变量: `var(--flexcyon-editor-writing)`

默认: false (类切换)

### 书写模式缩进

目标 CSS 变量: `var(--flexcyon-editor-writing-indentation)`

默认: 16 (px)

---

### 无障碍

切换辅助功能选项

> Note that changing these will change how the entire theme renders.
>
> Tweaking these values too much may make the theme look ugly

### 全局亮度比

目标 CSS 变量: `var(--flexcyon-brightness-ratio)`

默认: 1

### 全局对比度

目标 CSS 变量: `var(--flexcyon-contrast-ratio)`

默认: 1

> E.g. if you want slightly more contrast like on an OLED screen, try values
> between 1 to 1.5

### 全局饱和比

目标 CSS 变量: `var(--flexcyon-saturation-ratio)`

默认: 1

> Use to modify the saturation of colors
