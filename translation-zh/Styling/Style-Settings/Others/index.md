---
title: 其他人员
icon: material/dots-horizontal
---

对于配置 vim 模式文本, 新建标签 appenance( ASCII 艺术), sidedock 图标,
,
工具提示半径

接受格式: px

□ 导航

```md
Style Settings
|-- 。
|-- Flexcyon Style Settings
|   |-- 。
|   |-- Others
```
□ 配置选项

虚拟文本

#### 启用维姆 模式文本

CSS目标变量:`var(--flexcyon-vim-mode-text-enable)`
默认 :true(类切换)

#### Vim 模式左侧文本定位

CSS目标变量:`var(--flexcyon-vim-mode-left-positioning)`
默认: 6 (px)

#### Vim 模式文本底部定位

CSS目标变量:`var(--flexcyon-vim-mode-left-positioning)`
默认 : - 4 (px)

插入模式文本

CSS目标变量:`var(--flexcyon-vim-insert-text)`
默认: "INSERT"

普通模式文本

CSS目标变量:`var(--flexcyon-vim-normal-text)`
默认: "NORMAL"

QQ 命令模式文本

CSS目标变量:`var(--flexcyon-vim-command-text)`
默认: "COMMAND"

 

新标签外观

自定义新空标签的占位

接受格式: px

#### 在空状态标题前添加

CSS目标类别:`.flexcyon-ascii-enable, .flexcyon-quote-enable`
> 更改此选项可能要重新装入/ 重新启动才能生效

默认: 无( 类选择)
选项 :

- ASCII艺术
- 引语

#### 在空状态标题前添加的背景

CSS目标变量:`var(--flexcyon-new-tab-bg-wrapper)`
默认 :`linear-gradient(to right, var(--text-accent), var(--color-blue), var(--color-cyan))`
引用

CSS目标变量:`var(--flexcyon-quote-val)`
默认: ""

#### 引用字体大小

CSS目标变量:`var(--flexcyon-quote-font-size)`
默认: 24 (px)
> 换行符作为`\a`和`\`以`\\`
ASCII艺术

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
ASCII 艺术字体大小限制

CSS目标变量:`var(--flexcyon-ascii-max-font-size)`
默认: 14 (px)

ASCII 艺术线高度

CSS目标变量:`var(--flexcyon-ascii-line-height)`
> 更改引用的行高 welll

默认:1

#### 禁用空状态标题

CSS目标变量:`var(--flexcyon-empty-state-title-disable)`
默认 :true(类切换)

#### 禁用空状态动作

CSS目标变量:`var(--flexcyon-empty-state-actions-disable)`
默认 :false(类切换)

 

### 边停靠图标

配置侧对接图标

#### 启用侧对接图标效果
> 悬浮的彩虹效应
CSS目标变量:`var(--flexcyon-sidedock-icon-effects)`
默认 :true(类切换)

#### 隐藏侧对接丝带

CSS目标变量:`var(--flexcyon-sidedock-ribbon-hidden)`
默认 :false(类切换)

 

* 工具提示半径

配置工具提示半径

#### 小半径

CSS目标变量:`var(--radius-s)`
默认: 2 (px)

#### 中半径

CSS目标变量:`var(--radius-m)`
默认: 4( px)

####Large半径

CSS目标变量:`var(--radius-l)`
默认: 6 (px)

____________________ 额外large半径

CSS目标变量:`var(--radius-xl)`
默认: 8 (px)

 

++ 侧边栏背景

在左右侧边栏配置背景图像。

接受格式: px,%

#### 在侧边栏选择背景

CSS目标类别:`.flexcyon-sidebar-bg-dots, .flexcyon-sidebar-bg-grid, flexcyon-sidebar-bg-rhombus`
> 覆盖下面的背景图像声明,在左侧和左侧配置
> 右侧边栏

默认: 无( 类选择)
选项 :

- 绳子
- 点缀
-罗姆布斯

#### 左侧边栏背景图像 URL

CSS目标变量:`var(--flexcyon-bg-image-sidebar-left-url)`
默认: url (")
> 要工作, 请在双引号之间添加您的 URL, 例如:
`url("https://fake_domain/not_a_real_image.png")`
#### 右侧栏背景图像 URL

CSS目标变量:`var(--flexcyon-bg-image-sidebar-right-url)`
默认: url (")
> 要工作, 请在双引号之间添加您的 URL, 例如:
`url("https://fake_domain/not_a_real_image.png")`
• 侧边栏背景图像混合模式

CSS目标变量:`var(--flexcyon-bg-image-blend-mode)`
默认 :darken

• 侧边栏背景图像重复

CSS目标变量:`var(--flexcyon-bg-image-repeat)`
默认 :no-repeat

• 侧边栏背景图像模糊

CSS目标变量:`var(--flexcyon-bg-image-blur)`
默认:1px
> 将在下次更新时更改为 0px

++ 侧边栏背景图像亮度

CSS目标变量:`var(--flexcyon-bg-image-brightness)`
默认 :unset
> 接受百分比值为55%

++ 侧边栏背景图像大小

CSS目标变量:`var(--flexcyon-bg-image-size)`
默认 :contain

++ 侧边栏背景图像位置

CSS目标变量:`var(--flexcyon-bg-image-position)`
默认 :center

 

++ 模块背景

在设置菜单、 提示等背景中配置背景图像

接受格式: px,%

QQ 模式背景图像 URL

CSS目标变量:`var(--flexcyon-modal-bg-url)`
默认: url (")
> 要工作, 请在双引号之间添加您的 URL, 例如:
`url("https://fake_domain/not_a_real_image.png")`
\\\ 背景图像混合模式

CSS目标变量:`var(--flexcyon-modal-image-blend-mode)`
默认 :lighten

QQ 模式背景图像重复

CSS目标变量:`var(--flexcyon-modal-image-repeat)`
默认 :no-repeat

\\\ 背景图像模糊

CSS目标变量:`var(--flexcyon-modal-image-blur)`
默认:1px

\\\ 背景图像亮度

CSS目标变量:`var(--flexcyon-bg-modal-brightness)`
默认 :unset
> 接受百分比值为55%

QQ 模块背景图像大小

CSS目标变量:`var(--flexcyon-modal-image-size)`
默认 :cover

QQ 模块背景图像位置

CSS目标变量:`var(--flexcyon-modal-image-position)`
默认 :center

 

### 复活节彩蛋模式

堕地，见[here for reasons](../../../README/page-5.md)[here for reasons](../../../README/page-5.md)。

 

* 无障碍

切换访问选项
> 注意改变这些会改变整个主题的形成方式。
>
> 调整这些价值可能让主题看起来很丑陋

全球亮度比

CSS目标变量:`var(--flexcyon-brightness-ratio)`
默认:1

全球对比比

CSS目标变量:`var(--flexcyon-contrast-ratio)`
默认:1
> 例如,如果想要像OLED屏幕上那样略作对比,请尝试数值
> 1 到1.

全球饱和率

CSS目标变量:`var(--flexcyon-saturation-ratio)`
默认:1
> 用于修改颜色饱和度

 
□ 模式

QQ 返回零模式
> 由"闪烁焦点"主题启发的极端最小主义。 多数UI 元素
> 在徘徊之前不显示。 不推荐移动。

CSS目标变量:`var(--flexcyon-rtz-mode)`
默认 :false(类切换)

QQ 启用写入 全球模式
> 和它的csslass对应的一样,除了全球应用

CSS目标变量:`var(--flexcyon-editor-writing)`
默认 :false(类切换)

### 写入模式缩进

CSS目标变量:`var(--flexcyon-editor-writing-indentation)`
默认: 16 (px)

