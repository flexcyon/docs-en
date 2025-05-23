---
title: 插件
icon: material/hexagon-outline
---

用于配置官方支持的插件

接受格式:HEX、rem、x.y,%

## Navigation
```md
Style Settings
|-- ...
|-- Flexcyon Style Settings
|   |-- ...
|   |-- Plugins
|   |-- ...
```

## Configuration Options

### Alternate file tree

#### Folders font size
目标CSS变量:`var(--oz-fta-folder-font-size)`

默认: 0.925 (rem)

<span style="font-size: 0.925rem"
>样本 另选文件树文件夹字体大小</span>

#### Folders font color
目标CSS变量:`var(--oz-fta-folder-pane-file-name-color)`

默认( 灯光模式) :<span class="col-sqr" style="background-color: #080808"
></span
>#080808

默认( 暗模式) :<span class="col-sqr" style="background-color: #d3d5d3"
></span
>#d3d5d3

#### Active folder color
目标CSS变量:`var(--oz-fta-all-panes-active-text-color)`

默认( 灯光模式) :<span class="col-sqr" style="background-color: #080808"
></span
>#080808
i
默认( 暗模式) :<span class="col-sqr" style="background-color: #d3d5d3"
></span
>#d3d5d3

#### Files font size
目标CSS变量:`var(--oz-fta-file-font-size)`

默认: 0.9 (rem)

<span style="font-size: 0.9rem"
>样本 替代文件树文件字体大小</san>

#### Files font color
目标CSS变量:`var(--oz-fta-file-pane-file-name-color)`

默认 :<span class="col-sqr" style="background-color: #6f768599"
></span
>#6f768599

#### Disable folder icons
目标CSS变量:`var(--flexcyon-oz-folder-icons-disabled)`

默认 :false(类切换)

#### Disable file tree header
目标CSS变量:`var(--flexcyon-oz-file-tree-header-disabled)`

默认 :false(类切换)

#### Enable Alternate folder count
目标CSS变量:`var(--flexcyon-oz-alternate-folder-count)`

默认 :false(类切换)

#### Enabled dimmed file extensions in file tree
目标CSS变量:`var(--flexcyon-oz-dimmed-file-exts-enabled)`

默认 :true(类切换)

___ 
### Full Calendar

接受格式: x.y,%

#### Opacity of dimmed full calendar items
目标CSS变量:`var(--flexcyon-fc-dimmed-items-opacity)`

默认: 0.89

<span style="opacity: 0.89"
>阴暗的完整日历项目的样本不透明</span>

___ 
### Dataview

接受格式: px

#### Horizontal padding of dataview error messages
目标CSS变量:`var(--flexcyon-dataview-horizontal-padding)`

默认: 8 (px)

___ 
### Canvas
定义 Canvas 核心插件的样式。

接受格式: px, RGB

#### Blur inactive Canvas nodes
目标CSS变量:`var(--flexcyon-canvas-blur-inactive-nodes)`

默认 :false(类切换)

#### Blur intensity for inactive nodes
与上一个设置一起用于设置不活动画布节点和所有箭头/尖端的模糊强度。

目标CSS变量:`var(--flexcyon-canvas-blur-intensity)`

默认: 1 (px)

#### Canvas card menu alignment
配置画布卡菜单的对齐 。

CSS类目标:`.flexcyon-canvas-menu-bottom-left, .flexcyon-canvas-menu-bottom-right, .flexcyon-canvas-menu-top-center, .flexcyon-canvas-menu-top-left, .flexcyon-canvas-menu-top-right, .flexcyon-canvas-menu-lcenter-center, .flexcyon-canvas-menu-lcenter-top, .flexcyon-canvas-menu-lcenter-bottom, .flexcyon-canvas-menu-rcenter-center, .flexcyon-canvas-menu-rcenter-top, .flexcyon-canvas-menu-rcenter-bottom, .flexcyon-canvas-menu-recenter-align`

默认: 无( 选择类)

选项 :
-左边

- 右边

- 顶部中心

- 左边

- 右边

- 左对齐中心

- 左对齐顶部

- 左对齐底部

- 右对齐中心

- 右对齐顶部

- 右对齐底部

- 右对齐中心对齐