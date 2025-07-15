---
title: 其他人员
icon: material/dots-horizontal
---

对于配置vim模式文本,新制表符 aperance(ASCII 艺术),侧式图标,
,
工具提示半径

接受格式: px

## Navigation

```md
Style Settings
|-- 。
|-- Flexcyon Style Settings
|   |-- 。
|   |-- Others
```
## Configuration Options

### Vim Mode Text

#### Enable Vim Mode Text

CSS目标变量:`var(--flexcyon-vim-mode-text-enable)`
默认 :true(类切换)

#### Vim mode text left positioning

CSS目标变量:`var(--flexcyon-vim-mode-left-positioning)`
默认: 6 (px)

#### Vim mode text bottom positioning

CSS目标变量:`var(--flexcyon-vim-mode-left-positioning)`
默认 : - 4 (px)

#### Insert Mode Text

CSS目标变量:`var(--flexcyon-vim-insert-text)`
默认: "INSERT"

#### Normal Mode Text

CSS目标变量:`var(--flexcyon-vim-normal-text)`
默认: "NORMAL"

#### Command Mode Text

CSS目标变量:`var(--flexcyon-vim-command-text)`
默认: "COMMAND"

 

### New Tab Appearance

自定义新空标签的占位

接受格式: px

#### Add before empty state title

CSS目标类别:`.flexcyon-ascii-enable, .flexcyon-quote-enable`
> 更改此选项可能要重新装入/ 重新启动才能生效

默认: 无( 选择类)
选项 :

- ASCII艺术
- 引语

#### Background for add before empty state title

CSS目标变量:`var(--flexcyon-new-tab-bg-wrapper)`
默认 :`linear-gradient(to right, var(--text-accent), var(--color-blue), var(--color-cyan))`
#### Quote

CSS目标变量:`var(--flexcyon-quote-val)`
默认 : “ 这是引用 Flexcyon 主题的占位符 。 ”

#### Quote Attribution Prefix

CSS目标变量:`var(--flexcyon-quote-credit-prefix)`
默认: "-"

#### Quote Attribution

CSS目标变量:`var(--flexcyon-quote-credit)`
默认: "刀锋"

#### Quote font size

CSS目标变量:`var(--flexcyon-quote-font-size)`
默认: 24 (px)
> 换行符作为`\a`和`\`以`\\`
#### ASCII Art

CSS目标变量:`var(--flexcyon-ascii-art)`
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
> ASCII 艺术串需要逃脱CSS换成这样,换行就是
> 以`\a`和`\`以`\\`
#### ASCII art font size limit

CSS目标变量:`var(--flexcyon-ascii-max-font-size)`
默认: 14 (px)

#### ASCII art line height

CSS目标变量:`var(--flexcyon-ascii-line-height)`
> 更改引用的行高 welll

默认:1

#### Disable Empty State title

CSS目标变量:`var(--flexcyon-empty-state-title-disable)`
默认 :true(类切换)

#### Disable Empty State Actions

CSS目标变量:`var(--flexcyon-empty-state-actions-disable)`
默认 :false(类切换)

 

### Side Dock

配置侧对接图标

#### Enable side dock icon effects
> 悬浮的彩虹效应

CSS目标变量:`var(--flexcyon-sidedock-icon-effects)`
默认 :true(类切换)

### Side Dock Ribbon Width

CSS目标变量:`var(--flexcyon-sidedock-ribbon-width)`
默认: 48 (px)

 

### Tooltip radius

配置工具提示半径

#### Small radius

CSS目标变量:`var(--radius-s)`
默认: 2 (px)

#### Medium radius

CSS目标变量:`var(--radius-m)`
默认: 4( px)

#### Large radius

CSS目标变量:`var(--radius-l)`
默认: 6 (px)

#### Extra large radius

CSS目标变量:`var(--radius-xl)`
默认: 8 (px)

 

### Sidebar Background

在左右侧边栏配置背景图像。
.

接受格式: px,%

#### Select background in sidebar

CSS目标类别:`.flexcyon-sidebar-bg-dots, .flexcyon-sidebar-bg-grid, flexcyon-sidebar-bg-rhombus`
> 覆盖下面的背景图像声明,在左侧和左侧配置
> 右侧边栏

默认: 无( 选择类)
选项 :

- 绳子
- 点缀
-罗姆布斯

#### Left sidebar background image url

CSS目标变量:`var(--flexcyon-bg-image-sidebar-left-url)`
默认: url (")
> 要工作, 请在双引号之间添加您的 URL, 例如:
`url("https://fake_domain/not_a_real_image.png")`
#### Right sidebar background image url

CSS目标变量:`var(--flexcyon-bg-image-sidebar-right-url)`
默认: url (")
> 要工作, 请在双引号之间添加您的 URL, 例如:
`url("https://fake_domain/not_a_real_image.png")`
#### Sidebar Background image blend mode

CSS目标变量:`var(--flexcyon-bg-image-blend-mode)`
默认 :darken

#### Sidebar Background image repeat

CSS目标变量:`var(--flexcyon-bg-image-repeat)`
默认 :no-repeat

#### Sidebar Background image blur

CSS目标变量:`var(--flexcyon-bg-image-blur)`
默认:1px
> 将在下次更新时更改为 0px

#### Sidebar Background image brightness

CSS目标变量:`var(--flexcyon-bg-image-brightness)`
默认 :unset
> 接受百分比值为55%

#### Sidebar Background image size

CSS目标变量:`var(--flexcyon-bg-image-size)`
默认 :contain

#### Sidebar Background image position

CSS目标变量:`var(--flexcyon-bg-image-position)`
默认 :center

 

### Modal Background

在设置菜单、 提示等背景中配置背景图像

接受格式: px,%

#### Modal Background image url

CSS目标变量:`var(--flexcyon-modal-bg-url)`
默认: url (")
> 要工作, 请在双引号之间添加您的 URL, 例如:
`url("https://fake_domain/not_a_real_image.png")`
#### Modal Background image blend mode

CSS目标变量:`var(--flexcyon-modal-image-blend-mode)`
默认 :lighten

#### Modal Background image repeat

CSS目标变量:`var(--flexcyon-modal-image-repeat)`
默认 :no-repeat

#### Modal Background image blur

CSS目标变量:`var(--flexcyon-modal-image-blur)`
默认:1px

#### Modal Background image brightness

CSS目标变量:`var(--flexcyon-bg-modal-brightness)`
默认 :unset
> 接受百分比值为55%

#### Modal background image size

CSS目标变量:`var(--flexcyon-modal-image-size)`
默认 :cover

#### Modal background image position

CSS目标变量:`var(--flexcyon-modal-image-position)`
默认 :center

 

### Easter egg mode

堕地。 见[here for reasons](../../../README/page-5.md)。

 

### Accessibility

切换访问选项
> 注意改变这些会改变整个主题的形成方式。
>
> 调整这些价值可能让主题看起来很丑陋

### Global brightness ratio

CSS目标变量:`var(--flexcyon-brightness-ratio)`
默认:1

### Global contrast ratio

CSS目标变量:`var(--flexcyon-contrast-ratio)`
默认:1
> 例如,如果想要像OLED屏幕上那样略作对比,请尝试数值
> 1至1.5岁

### Global saturation ratio

CSS目标变量:`var(--flexcyon-saturation-ratio)`
默认:1
> 用于修改颜色饱和度

 
## Modes

### Return to Zero mode
> 由"闪烁焦点"主题启发的极端最小主义。 多数UI 元素
> 在徘徊之前不显示。 不推荐移动。

CSS目标变量:`var(--flexcyon-rtz-mode)`
默认 :false(类切换)

### Enable Writing Mode globally
> 和它的csslass对应的一样,除了全球应用

CSS目标变量:`var(--flexcyon-editor-writing)`
默认 :false(类切换)

### Writing mode indentation

CSS目标变量:`var(--flexcyon-editor-writing-indentation)`
默认: 16 (px)

