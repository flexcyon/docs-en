---
title: 模式
---

配置 flexcyon 提供的一些独特模式. 您还可以在此处配置辅助功能设置. 

## 导航

```md
Style Settings
|-- flexcyon://模式 s
```

## 配置选项

### 选择模式
目标 CSS 类: `.flexcyon-flex-max-mode, .flexcyon-rtz-mode`

默认: Flex Max 模式 (class select)

选项:

- none (无)
- Flex Max 模式
- Return To Zero (RTZ) 模式

### 关于 Return to Zero 模式

受 Shimmering Focus 主题启发的极端极简主义. 大多数 UI 元素在悬停之前不会显示.
> 不建议在手机上使用

### 关于 Flex Max 模式


一个非常有主见的设置, 展示了这个主题的独特定制, 功能开箱即用.

如果您不太喜欢某些选项, 您可以不使用此模式并更多地自定义主题. 这将使主题重新设置为全新的自定义模式.

有些被启用的默认选项. 请参阅下文, 了解它为您启用的选项.

对于不知道从哪里开始定制的用户, 建议使用此模式. 对于那些希望 **广泛定制主题** 
或可能不喜欢这组默认设置的人, **建议避免使用此模式**.


### Flex Max 模式启用设置选项

启用以下设置, 即使它们在 *样式设置中未启用*

* 笑脸图标

* 确保社区插件图标优先

* 在空状态标题前添加 ASCII 艺术

* 用空状态标题

* 定义水平规则字符串

* Powerlevel10k 为灵感的状态栏风格

* 藏直到悬停状态栏

* 前状态栏编辑模式为文本而非图标

* Vim 模式状态

* 彩色标题

* 展调色板

* ASCII 复选框

* 剪辑路径复选框

* 设置中的彩色图标

* 社区项目效果

* 在设置中不显示滚动条

* 备用文件树插件的文件扩展名已变暗

* 启用侧坞图标效果

* 降低代码块文件扩展名 (Live Preview)

* 为代码块文件扩展名添加前缀 (Live Preview)


您应该能够配置这些设置, 就像它们正常启用一样.
该主题还有许多其他设置选项供您探索, 其中一些默认情况下是启用的, 如平滑光标.


### Typewriter 模式

目标 CSS 类: `var(--flexcyon-typewriter-mode)`

在 Source 和 Live Preview 模式下, 降低除活动行之外的所有行的不透明度.

默认: false (类切换)
  
### Typewriter 模式 Opacity

Typewriter 模式下变暗的非活动线的不透明度

目标 CSS 变量: `var(--flexcyon-typewriter-mode-opacity)`

默认: 0.55

### Reverse 模式

反转 UI 中内容的内容顺序.

目标 CSS 变量: `var(--flexcyon-reverse-mode)`

默认: false (类切换)

### 全局启用 Writing 模式

> 与它 cssclass 类似, 但全局启用

目标 CSS 变量: `var(--flexcyon-editor-writing)`

默认: false (类切换)

### Writing 模式缩进

目标 CSS 变量: `var(--flexcyon-editor-writing-indentation)`

默认: 16 (px)
