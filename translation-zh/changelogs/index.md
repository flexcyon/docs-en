---
icon: material/script-text
title: 更改日志
---

#### Note

The changelogs show versions in order of most recent to least recent.
Or, if you prefer the changelogs in chronological order, you can use
the sidebar or hamburger menu to view the relevant sub-pages.

___ 

## Version 0.4.x

### Version 0.4.1 Quickfix Update

- 在光线模式下修复 TUI 渲染

- 不启用丝带时将左侧边栏切换

- 专门用建议高亮点修正文本亮点bg

- 修复未显示的嵌套

### Version 0.4.0 Light Mode Update

- 修改侧边栏背景亮度设置为`unset`. Was
previously causing issues like blurring Calender plugin content.

- WIP灯主题(混合弹性灯+折纸彩色调色板)

- 其他更改

- 为扩展调色板添加切换,默认情况下

  - Added table header size option

  - Updated documentation to show a small preview of colors/opacity applied by
  the theme

- 增加了主题功能的网络展示

- 删除复活节 鸡蛋模式

- 光和暗模式选项的样式选择器

- ASCII 艺术和引文现在继承了界面字体

- 改进了即时造型和树品垫

- 回归零(超极简模式),灵感来自Simmering Focus主题

## Version 0.3.x

### Version 0.3.6 Canvas Menu Update

- 固定边栏背景问题

- 防止标题指标显示在下调编辑器外的情况

- 小代码库重构

- 强调色略有变化

- 添加画布卡菜单对齐选项(多种选项)

### Version 0.3.5 Configuration Update

- 文件现在有自己的网站。

- 为标题添加软发光选项

- 可切换的彩虹元数据图标

- 增加全球亮度、对比率和饱和率的无障碍选项

- Added option to enable heading indicators globally, customisable for
different heading levels.

- 标题指标现在更好地继承标题的基础颜色

- 添加选项以配置弹出点名动画持续时间

- 添加选项以配置元数据容器左侧粘贴

### Version 0.3.4 Easter Egg Mode

- Made translation for hide until hover status bar configurable, useful for
longer status bars

- 固定文件探索器背景被打破

- 为文件夹样式添加了标记下的文件树选项

- 添加列表样式的点名元数据工具

- 添加可切换复活节彩蛋模式

### Version 0.3.3 QOL Update

- Added configurable indentation factor and dimming of collapsed headers for
Style Settings menu

- Added writing mode callout metadata utility, it increases text indent and
paragraph spacing

  - It also has a CSS class provider which allows you to apply the same text
  indent and paragraph spacing increments to the target note

- 添加 Rhombus 编辑器背景选项

- You can now use grid, dotted or rhombus as background options for the left
and right sidebar

- 这些覆盖左右侧边栏背景url选项

- 引文使用与ASCII艺术相同的颜色

- 默认引用更新为不是 Rickroll

- 增加了对 Kanban 插件的支持

- 在新标签空状态标题之前添加默认为无:

- 如果你使用引文或ASCII艺术, 请重新使用它

- 你现在可以配置引用或ASCII艺术的背景颜色

- 更改可能需要重新装入/重新启动程序才能生效

### Version 0.3.2 Animations

- 斯图林 调整到社区存储项, 现有布局

- 动画回归,目前的选项包括:

- 左到右幻灯片

- 向左滑动

- 从上到下幻灯片

- 从下到上幻灯片

- 从下到上旋转

- 向左旋转

- 为Powerlevel10k添加布局和状态样式

- 添加闪卡点名元数据工具

- 在空状态标题前添加自定义引用的选项

- 无法选择 ASCII 艺术, 默认选择 ASCII 艺术

- Added option to angle grid editor background

- Added background image option for modals (background image for settings,
prompts etc)

### Version 0.3.1 Tidying Up

- 为以下项目增加点名元数据:

- 网格和点背景

- 斜体和斜体标题和内容

- 对标题和内容进行破折、点、双层、超线、下划线和行穿

- 标题1至6样式

- 标题和内容的字体权重

- 添加标题字体大小选项

- 固定的微笑图标(希望是最后一次)

- 在左右边栏添加和配置图像背景的选项

- 微小修改悬浮中的导航项目,日历插件型号

- Slight tweaks to editor background dotted and grid background styling.

- 标签标题栏现在适应选定的布局样式

- 用于模糊 Canvas 核心 Canvas 插件的 Canvas 节点的添加选项

- 编辑器背景变化现在影响到Canvas核心插件。

- 可能需要应用程序重新装入/ 重新启动样式设置更改才能在 Canvas 中显示

- 调整帆布控制和卡片菜单的样式

- 改变面包屑的造型,以使用ASCII而不是emoji

### Version 0.3.0 TUI Layout

- 在卡片布局中添加提示的 TUI

- 默认启用

- 更改表格样式

- Added cssclasses for heading indicators, callout metadata for tilting callout
title and content

- 对日历插件添加支持

- Tweaked existing styling for Full Calendar plugin

- 微软的社区用品型式

- 固定的微笑图标对齐问题

- 愤怒的布局现在适用于更多的UI元素

- 现在应该更明显地看到主动的排水沟

- 添加快速对齐选项,使用样式设置配置:

- 左边

- 顶部center

- 中间左边

-左边

- 下边center

- [See the documentation](../index.md) for more details

___ 

## Version 0.2.x

### Version 0.2.2 Layout styling

- 固定双引号复选框背景颜色

- 添加对“断层统计”插件的支持

- 用于社区物品效应的小型型式调整

- Added card, angled options for workspace layout

- 如果您想要改变布局, 需要重新装入或重新启动应用程序

- Vim mode status text and status bar mode (reading/live preview etc) text now
has a color option:

- 默认切换

- 为状态栏添加卡片、角度(受Powerlevel10k启发)样式

- 影响vim模式状态文本

- 添加状态栏字体大小选项

### Version 0.2.1 Small Update

- 已删除的窗口动画,因为它们不是表演者。

- 更新扩展颜色,以便`*-color1-color2`和`*-color-2-color` will
always return the same color mix when using in callout metadata utilities.

- 使活动文件背景效果更加一致

- 添加 ASCII 艺术线高度选项

- 为点和网格编辑背景选项添加 cssclass

- 为内含标题添加样式选项

### Version 0.2.0 Aesthetics Update

- 添加点名垂直边距、边框半径选项

- 添加图像边框半径选项

- Added extended color palette (can be used as callout metadata utilities or in
css variables)

- Added popup callout, adapted from
[Ukiyo](https://github.com/technerium/obsidian-ukiyo)由 Vaykinov 和 wizentex 编写的主题

- 新注释、新文件夹等顶级动作的固定不透明

- Added window animations for modals, prompts and settings.
Choose from the following options:

- 无(默认行为的更正)

- 向上滑动

- 向下滑动

- 左向右滑动

- 向左滑动

-  您也可以配置动画持续时间

- 在阅读模式和编辑模式中切换属性显示的选项

- 默认情况下不会显示阅读模式中的属性

- 不显示编辑模式中的属性默认已禁用

- 添加选项以启用最小化(文件夹/外线)树

- 为文件探索者添加彩虹文件夹

- 添加点和网格背景选项

-见[documentation](../index.md)详情

___ 

## Version 0.1.x

### Version 0.1.1 Hotfixes

- 添加了修改 ASCII 复选框字体大小的选项

- 移动上的固定微笑图标

- 增加标题和背景色调元数据工具

- 在阅读模式和直播预览中切换属性可见度的附加选项

- 对 Dataview 插件添加支持

- 添加彩虹弹点(默认损坏)

- 更多的UI元素因一致性而暗淡

- 媒体嵌入器现在有可设定的垂直边距

### Version 0.1.0: Utilities Update

- 添加对空格重复插件的支持

- 添加Breadcrumbs插件的支持

- 增加标题下划线选项

- 设置中添加的替代活动项效果

- 为提示添加自定义选项

- 添加替代文件探索器样式

- 为改变链接颜色添加选项

- 添加了 ASCII 复选框

- 为下列项目增加点名公用事业:

- 没有图标

- 无标题

- 透明背景

- 大写、大写、小写标题和内容

- RTL, LTR, (英语),中间标题和内容

- 塔特加基语(普通RTL)

- 纵向LTR

- 为下列人员增加分类:

- 塔特加基语(普通RTL)

- 纵向LTR

-见[documentation](../index.md)详情

Credits:

- `@OWA/bennyyip`在 Obisidian 成员团体的Discord 上为 Tategaki 片断

- `@Tuck`在 Obsidian Members 组 Discord 上,用于修改链接颜色的选项

### Version 0.0.5: Minor Changes

- 使ASCII艺术响应,你可以设置字体大小 li光标打开

- 状态栏不与命令模式输入文本重叠

- 添加选项以启用移动状态栏

- 在标题的打印中添加行高选项

- 添加隐藏左侧丝带的选项

- 增加对全球顶级行动进行协调的选项

