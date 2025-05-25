---
title: 其他人员
icon: material/dots-horizontal
---

用于配置 vim 模式文本, 新建制表符 appance( ASCII 艺术), 侧面图标, 工具提示半径

接受格式: px

## Navigation
```md
Style Settings
|-- ...
|-- Flexcyon Style Settings
|   |-- ...
|   |-- Others
```

## Configuration Options

### Vim Mode Text
#### Enable Vim Mode Text
目标CSS变量:`var(--flexcyon-vim-mode-text-enable)`

默认 :true(类切换)

#### Vim mode text left positioning
目标CSS变量:`var(--flexcyon-vim-mode-left-positioning)`

默认: 6 (px)

#### Vim mode text bottom positioning
目标CSS变量:`var(--flexcyon-vim-mode-left-positioning)`

默认 : - 4 (px)

#### Insert Mode Text
目标CSS变量:`var(--flexcyon-vim-insert-text)`

默认: "INSERT"

#### Normal Mode Text
目标CSS变量:`var(--flexcyon-vim-normal-text)`

默认: "NORMAL"

#### Command Mode Text
目标CSS变量:`var(--flexcyon-vim-command-text)`

默认: "COMMAND"

___ 
### New Tab Appearance
自定义新空标签的占位

接受格式: px

#### Add before empty state title
CSS类目标:`.flexcyon-ascii-enable, .flexcyon-quote-enable`
> Changing this may take an app reload/restart to take effect

默认: 无( 选择类)
选项 :
- ASCII艺术
- 引语

#### Background for add before empty state title
目标CSS变量:`var(--flexcyon-new-tab-bg-wrapper)`

默认 :`linear-gradient(to right, var(--text-accent), var(--color-blue), var(--color-cyan))`

#### Quote
目标CSS变量:`var(--flexcyon-quote-val)`

默认: ""

#### Quote font size
目标CSS变量:`var(--flexcyon-quote-font-size)`

默认: 24 (px)
> Line breaks are escaped as `\a` and `\` is escaped as `\\`

#### ASCII Art
目标CSS变量:`var(--flexcyon-ascii-art)`

默认 :
```md
" \a\
    _______________                                       \a\
    ___  ____/__  /________  ____________  ______________ \a\
    __  /_   __  /_  _ \\_  |/_/  ___/_  / / /  __ \\_  __ \\ \a\
    _  __/   _  / /  __/_
>  < / /__ _  /_/ // /_/ /  / / / \a\
    /_/      /_/  \\___//_/|_| \\___/ _\\__, / \\____//_/ /_/ \a\
                                    /____/                \a\a\a "
```
> The ASCII art string needs to be escaped for CSS to render it, line breaks are escaped as `\a` and `\` is escaped as `\\`

#### ASCII art font size limit
目标CSS变量:`var(--flexcyon-ascii-max-font-size)`

默认: 14 (px)

#### ASCII art line height
目标CSS变量:`var(--flexcyon-ascii-line-height)`
> Changes line height for quote as welll

默认:1

#### Disable Empty State title
目标CSS变量:`var(--flexcyon-empty-state-title-disable)`

默认 :true(类切换)

#### Disable Empty State Actions
目标CSS变量:`var(--flexcyon-empty-state-actions-disable)`

默认 :false(类切换)

___ 
### Side Dock Icons
配置侧对接图标

#### Enable side dock icon effects
> Rainbow effect on hover
目标CSS变量:`var(--flexcyon-sidedock-icon-effects)`

默认 :true(类切换)

#### Hide the side dock ribbon
目标CSS变量:`var(--flexcyon-sidedock-ribbon-hidden)`

默认 :false(类切换)

___ 
### Tooltip radius
配置工具提示半径

#### Small radius
目标CSS变量:`var(--radius-s)`

默认: 2 (px)

#### Medium radius
目标CSS变量:`var(--radius-m)`

默认: 4(px)

#### Large radius
目标CSS变量:`var(--radius-l)`

默认: 6 (px)

#### Extra large radius
目标CSS变量:`var(--radius-xl)`

默认: 8 (px)

___ 
### Sidebar Background 
在左右侧边栏配置背景图像。

接受格式: px,%

#### Select background in sidebar
CSS类目标:`.flexcyon-sidebar-bg-dots, .flexcyon-sidebar-bg-grid, flexcyon-sidebar-bg-rhombus`
> Overrides background image declaration below, configures in both left and right sidebar

默认: 无( 选择类)
选项 :
- 绳子
- 点缀
-罗姆布斯

#### Left sidebar background image url
目标CSS变量:`var(--flexcyon-bg-image-sidebar-left-url)`

默认: url ("")
> For urls to work, add your URL between the double quotes e.g. a value of:
`url("https://fake_domain/not_a_real_image.png")`

#### Right sidebar background image url
目标CSS变量:`var(--flexcyon-bg-image-sidebar-right-url)`

默认: url ("")
> For urls to work, add your URL between the double quotes e.g. a value of:
`url("https://fake_domain/not_a_real_image.png")`

#### Sidebar Background image blend mode
目标CSS变量:`var(--flexcyon-bg-image-blend-mode)`

默认 :darken

#### Sidebar Background image repeat
目标CSS变量:`var(--flexcyon-bg-image-repeat)`

默认 :no-repeat

#### Sidebar Background image blur
目标CSS变量:`var(--flexcyon-bg-image-blur)`

默认: 1px
> Will be changed to 0px next update

#### Sidebar Background image brightness
目标CSS变量:`var(--flexcyon-bg-image-brightness)`

默认 :unset
> Accepts percentage values like 55%

#### Sidebar Background image size
目标CSS变量:`var(--flexcyon-bg-image-size)`

默认 :contain

#### Sidebar Background image position
目标CSS变量:`var(--flexcyon-bg-image-position)`

默认 :center

___ 
### Modal Background
在设置菜单、 提示等背景中配置背景图像

接受格式: px,%

#### Modal Background image url
目标CSS变量:`var(--flexcyon-modal-bg-url)`

默认: url ("")
> For urls to work, add your URL between the double quotes e.g. a value of:
`url("https://fake_domain/not_a_real_image.png")`

#### Modal Background image blend mode
目标CSS变量:`var(--flexcyon-modal-image-blend-mode)`

默认 :lighten

#### Modal Background image repeat
目标CSS变量:`var(--flexcyon-modal-image-repeat)`

默认 :no-repeat

#### Modal Background image blur
目标CSS变量:`var(--flexcyon-modal-image-blur)`

默认: 1px

#### Modal Background image brightness
目标CSS变量:`var(--flexcyon-bg-modal-brightness)`

默认 :unset
> Accepts percentage values like 55%

#### Modal background image size
目标CSS变量:`var(--flexcyon-modal-image-size)`

默认 :cover

#### Modal background image position
目标CSS变量:`var(--flexcyon-modal-image-position)`

默认 :center

___ 
### Easter egg mode
堕地。见[here for reasons](../../../README/page-5.md)。

___ 
### Accessibility
切换无障碍选项
> Note that changing these will change how the entire theme renders. 
>
> Tweaking these values too much may make the theme look ugly

### Global brightness ratio
目标CSS变量:`var(--flexcyon-brightness-ratio)`

默认:1

### Global contrast ratio
目标CSS变量:`var(--flexcyon-contrast-ratio)`

默认:1
> E.g. if you want slightly more contrast like on an OLED screen, try values between 1 to 1.5

### Global saturation ratio
目标CSS变量:`var(--flexcyon-saturation-ratio)`

默认:1
> Use to modify the saturation of colors

___ 
### Return to Zero mode
> Extreme minimalism inspired by the Shimmering Focus theme. Most UI elements are not displayed until hovered on. Will not recommend on mobile.

目标CSS变量:`var(--flexcyon-rtz-mode)`

默认 :false(类切换)