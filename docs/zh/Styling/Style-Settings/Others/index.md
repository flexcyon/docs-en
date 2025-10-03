---
title: Others
icon: material/dots-horizontal
---

用于配置 Vim 模式文本, 新选项卡外观 (ASCII 艺术), 侧边栏图标, 工具提示半径

接受的格式: px

## 导航

```md
Style Settings
|-- ...
|-- Flexcyon Style Settings
| |-- ...
| |-- Others
```

## 配置选项

### Vim 模式文本

#### 启用 Vim 模式文本

目标 CSS 变量: `var(--flexcyon-vim-mode-text-enable)`

默认: true (类切换)

#### Vim 模式文本左定位

目标 CSS 变量: `var(--flexcyon-vim-mode-left-positioning)`

默认: 6 (px)

#### Vim 模式文本底部定位

目标 CSS 变量: `var(--flexcyon-vim-mode-left-positioning)`

默认: -4 (px)

#### Insert 模式文本

目标 CSS 变量: `var(--flexcyon-vim-insert-text)`

默认: "INSERT"

#### Normal 模式文本

目标 CSS 变量: `var(--flexcyon-vim-normal-text)`

默认: "NORMAL"

#### Command 模式文本

目标 CSS 变量: `var(--flexcyon-vim-command-text)`

默认: "COMMAND"

---

### 新选项卡外观

自定义新空选项卡的外观

接受的格式: px

#### 在空状态标题之前添加

目标 CSS 类: `.flexcyon-ascii-enable, .flexcyon-quote-enable`

> Changing this may take an app reload/restart to take effect

默认: none (类选项)

选项:

- ASCII Art (ASCII 艺术)
- Quote (引用)

#### 空状态标题前添加的背景

目标 CSS 变量: `var(--flexcyon-new-tab-bg-wrapper)`

默认: `linear-gradient(to right, var(--text-accent), var(--color-blue), var(--color-cyan))`

#### 引用

目标 CSS 变量: `var(--flexcyon-quote-val)`

默认: "This is a placeholder quote\ain the Flexcyon Theme."

#### 引用归因前缀

目标 CSS 变量: `var(--flexcyon-quote-credit-prefix)`

默认: "-"

#### 引用归因

目标 CSS 变量: `var(--flexcyon-quote-credit)`

默认: "bladeacer"

#### 引用字体大小

目标 CSS 变量: `var(--flexcyon-quote-font-size)`

默认: 24 (px)

> 换行符被转义为`\a`，而`\`则被转义为`\\`

#### ASCII 艺术

目标 CSS 变量: `var(--flexcyon-ascii-art)`

默认:

```md
" \a\
 **\*\***\_\_\_**\*\*** \a\
 **\_ \_\_**/** /**\_\_\***\* \*\***\_\_\_\_\***\* \*\*\*\***\_\_**\*\*** \a\
 ** /\_ ** /\_ _ \\_ |/\_/ **_/_ / / / ** \\_ \_\_ \\ \a\
 _ **/ \_ / / **/_> < / /\_\_ _ /_/ // /_/ / / / / \a\
 /_/ /_/ \\**_//_/|_| \\_**/ _\\**, / \\\_\_**//_/ /\_/ \a\
 /\_\_\_\_/ \a\a\a "
```

> ASCII 艺术字符串需要转义以便 CSS 渲染, 换行符是
> 转义为 `\a`，而 `\` 则转义为 `\\`

#### ASCII 艺术字体大小限制

目标 CSS 变量: `var(--flexcyon-ascii-max-font-size)`

默认: 14 (px)

#### ASCII 艺术线条高度

目标 CSS 变量: `var(--flexcyon-ascii-line-height)`

> Changes line height for quote as welll

默认: 1

#### 不使用空状态标题

目标 CSS 变量: `var(--flexcyon-empty-state-title-disable)`

默认: true (类切换)

#### 不使用空状态操作

目标 CSS 变量: `var(--flexcyon-empty-state-actions-disable)`

默认: false (类切换)

---

### 工作区侧停靠带

配置工作区侧停靠带图标

#### 启用工作区侧停靠带图标样式

> 悬停时的彩虹效果

目标 CSS 变量: `var(--flexcyon-sidedock-icon-effects)`

默认: true (类切换)

### 工作区侧停靠带宽度

目标 CSS 变量: `var(--flexcyon-sidedock-ribbon-width)`

默认: 48 (px)

### 将工作区功能区放置在顶部

目标 CSS 变量: `var(--flexcyon-ribbon-top)`

默认: false (类切换)

### 将 Vault 切换器放置在顶部

目标 CSS 变量: `var(--flexcyon-vault-switch-top)`

默认: false (类切换)

### Vault 切换器的逆序及其动作

目标 CSS 变量: `var(--flexcyon-vault-reverse)`

默认: false (类切换)

---

### 工具提示半径

配置工具提示半径

#### 小半径

目标 CSS 变量: `var(--radius-s)`

默认: 2 (px)

#### 中等半径

目标 CSS 变量: `var(--radius-m)`

默认: 4 (px)

#### 大半径

目标 CSS 变量: `var(--radius-l)`

默认: 6 (px)

#### 特大半径

目标 CSS 变量: `var(--radius-xl)`

默认: 8 (px)

---

### 侧边栏背景

在左侧栏和右侧栏中配置背景图像。

接受的格式: px, %

#### 在侧边栏中选择背景

目标 CSS 类: `.flexcyon-sidebar-bg-dots, .flexcyon-sidebar-bg-grid, flexcyon-sidebar-bg-rhombus`

> 覆盖下面的背景图像声明，在左侧和右侧进行配置
> 右侧边栏

默认: none (类选项)

选项:

- Grid (网格)
- Dotted (点缀)
- Rhombus (菱形)

#### 左侧边栏背景图片 url

目标 CSS 变量: `var(--flexcyon-bg-image-sidebar-left-url)`

默认: url("")

> 为了使 URL 正常操作, 请在双引号之间添加您的 URL, 例如值:
> `url（“https://fake_domain/not_a_real_image.png")`

#### 右侧边栏背景图片 url

目标 CSS 变量: `var(--flexcyon-bg-image-sidebar-right-url)`

默认: url("")

> 为了使 URL 正常操作, 请在双引号之间添加您的 URL, 例如值:
> `url（“https://fake_domain/not_a_real_image.png")`

#### 侧边栏背景图像混合模式

目标 CSS 变量: `var(--flexcyon-bg-image-blend-mode)`

默认: darken

#### 侧边栏背景图像重复

目标 CSS 变量: `var(--flexcyon-bg-image-repeat)`

默认: no-repeat

#### 侧边栏背景图像模糊

目标 CSS 变量: `var(--flexcyon-bg-image-blur)`

默认: 0 (px)

#### 侧边栏背景图像亮度

目标 CSS 变量: `var(--flexcyon-bg-image-brightness)`

默认: unset

> 接受百分比值，如 55%

#### 侧边栏背景图像大小

目标 CSS 变量: `var(--flexcyon-bg-image-size)`

默认: contain

#### 侧边栏背景图像位置

目标 CSS 变量: `var(--flexcyon-bg-image-position)`

默认: center

---

### 模态背景

在设置菜单, 提示等背景中配置背景图像


接受的格式: px, %

#### 模态背景图像 url

目标 CSS 变量: `var(--flexcyon-modal-bg-url)`

默认: url("")

> 为了使 URL 正常操作, 请在双引号之间添加您的 URL, 例如值:
> `url（“https://fake_domain/not_a_real_image.png")`

#### 模态背景图像混合模式

目标 CSS 变量: `var(--flexcyon-modal-image-blend-mode)`

默认: lighten

#### 模态背景图像重复

目标 CSS 变量: `var(--flexcyon-modal-image-repeat)`

默认: no-repeat

#### 模态背景图像模糊

目标 CSS 变量: `var(--flexcyon-modal-image-blur)`

默认: 0 (px)

#### 模态背景图像亮度

目标 CSS 变量: `var(--flexcyon-bg-modal-brightness)`

默认: unset

> 接受百分比值，如 55%

#### 模态背景图像大小

目标 CSS 变量: `var(--flexcyon-modal-image-size)`

默认: cover

#### 模态背景图像位置

目标 CSS 变量: `var(--flexcyon-modal-image-position)`

默认: center
