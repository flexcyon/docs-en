---
title: Status Bar
icon: material/state-machine
---

定义 CSS 变量以配置状态栏。

接受的格式: s, px

## 导航

```md
Style Settings
|-- ...
|-- Flexcyon Style Settings
| |-- Editor
| | |-- ...
| | |-- Status Bar
| | |-- ...
| |-- ...
|-- ...
```

## 配置选项

### 状态栏

#### 隐藏直到触发

目标 CSS 类: `.flexcyon-status-hide-until-hover
.flexcyon-status-hide-until-hold`

默认: none (类选项)

选项:

- Hide until hover (隐藏直到鼠标悬停)
- Hide until hold (隐藏直到按住)

#### 状态栏对齐

目标 CSS 类: `.flexcyon-status-left-align
.flexcyon-status-centre-align`

默认: none (类选项)

选项:

- Left (左)
- Centre (中心)

#### 在启用悬停之前隐藏文本

目标 CSS 变量: `var(--flexcyon-status-hide-until-hover-text)`

默认: "Show status"

#### 悬停时显示状态栏的几何平移

目标 CSS 变量: `var(--flexcyon-status-hide-until-hover-translation)`

默认: 1500 (px)

#### 悬停时显示状态栏的过渡持续时间

目标 CSS 变量: `var(--flexcyon-status-hide-hover-duration)`

默认: 0.35 (s)

#### 悬停状态栏显示的转换定时函数

目标 CSS 变量: `var(--flexcyon-status-hide-hover-function)`

默认: ease-out

---

### 文本配置

#### 使用文本而不是图标表示模式状态

目标 CSS 变量: `var(--flexcyon-status-text-mode)`

默认: false (类切换)

#### Reading Mode 文本

目标 CSS 变量: `var(--flexcyon-status-reading-text)`

默认: "READ"

#### Source Mode 文本

目标 CSS 变量: `var(--flexcyon-status-source-text)`

默认: "SOURCE"

#### Live Preview 文本

目标 CSS 变量: `var(--flexcyon-status-live-text)`

默认: "LIVE"

---

### 状态栏样式

#### 在手机上显示状态栏

目标 CSS 变量: `var(--flexcyon-status-mobile-enabled)`

默认: false (类切换)

#### 状态栏字体大小

目标 CSS 变量: `var(--status-bar-font-size)`

默认: 13.753255 (px)

#### 选择状态栏样式

目标 CSS 类: `.flexcyon-status-style-angled,
.flexcyon-status-style-card, .flexcyon-status-style-pl10k`

默认: none (类选项)

选项:

- Angled (倾斜)
- Cards (卡片)
- Powerlevel10k

#### 启用状态文本颜色

目标 CSS 变量: `var(--flexcyon-status-text-enable-color)`

默认: false (类切换)
