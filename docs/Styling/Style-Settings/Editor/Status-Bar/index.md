---
title: 状态栏
icon: material/state-machine
---

定义CSS用于配置状态栏的变量

接受格式: s, px

□ 导航

```md
Style Settings
|-- 。
|-- Flexcyon Style Settings
|   |-- Editor
|   |   |-- 。
|   |   |-- Status Bar
|   |   |-- 。
|   |-- 。
|-- 。
```

□ 配置选项

QQ 状态栏隐藏到 Hover

#### 隐藏到徘徊

CSS目标变量:`var(--flexcyon-status-hide-until-hover)`
默认 :false(类切换)

#### 隐藏时文本, 直到启用徘徊

CSS目标变量:`var(--flexcyon-status-hide-until-hover-text)`
默认: “ 显示状态 ”

显示悬浮状态栏的翻译

CSS目标变量:`var(--flexcyon-status-hide-until-hover-translation)`
默认: 1500px

* 显示悬浮状态栏的过渡期

CSS目标变量:`var(--flexcyon-status-hide-hover-duration)`
默认: 0.35(s)

盘旋时显示状态栏的过渡计时功能

CSS目标变量:`var(--flexcyon-status-hide-hover-function)`
默认 :ease-out

 
QQ 文本配置

#### 模式状态使用文本而不是图标

CSS目标变量:`var(--flexcyon-status-text-mode)`
默认 :false(类切换)

#### 读取模式文本

CSS目标变量:`var(--flexcyon-status-reading-text)`
默认: "READ"

#### 源模式文本

CSS目标变量:`var(--flexcyon-status-source-text)`
默认: "资源"

QQ 现场预览模式文本

CSS目标变量:`var(--flexcyon-status-live-text)`
默认: "LIVE"

 

QQ 状态栏样式

#### 在移动中显示状态栏

CSS目标变量:`var(--flexcyon-status-mobile-enabled)`
默认 :false(类切换)

#### 状态栏字体大小

CSS目标变量:`var(--status-bar-font-size)`
默认: 12.5 (px)

#### 选择状态栏样式

CSS目标类别:`.lexcyon-status-style-倾斜
.flexcyon-status-style-card,.flexcyon-style-style-pl10k ' 

默认: 无( 类选择)
选项 :

- 愤怒
- 纸牌
- 动力级10k

#### 启用状态文本颜色

CSS目标变量:`var(--flexcyon-status-text-enable-color)`
默认 :false(类切换)

