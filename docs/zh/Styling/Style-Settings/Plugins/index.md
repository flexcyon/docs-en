---
title: Plugins
icon: material/hexagon-outline
---

For configuration of officially supported plugins

接受的格式: HEX, rem, x.y, %

## 导航

```md
Style Settings
|-- ...
|-- Flexcyon Style Settings
| |-- ...
| |-- Plugins
| |-- ...
```

## 配置选项

### Alternate file tree 插件

#### 文件夹字体大小

目标 CSS 变量: `var(--oz-fta-folder-font-size)`

默认: 0.925 (rem)

<span style="font-size: 0.925rem">Sample Alternate file tree Folders font size</span>

#### 文件夹字体颜色

目标 CSS 变量: `var(--oz-fta-folder-pane-file-name-color)`

默认 (灯光模式):
<span class="col-sqr" style="background-color: #080808"></span> #080808

默认 (暗模式):
<span class="col-sqr" style="background-color: #d3d5d3"></span> #d3d5d3

#### 活跃文件夹颜色

目标 CSS 变量: `var(--oz-fta-all-panes-active-text-color)`

默认 (灯光模式):
<span class="col-sqr" style="background-color: #080808"></span> #080808

默认 (暗模式):
<span class="col-sqr" style="background-color: #d3d5d3"></span> #d3d5d3

#### 文件字体大小

目标 CSS 变量: `var(--oz-fta-file-font-size)`

默认: 0.9 (rem)

<span style="font-size: 0.9rem">Sample Alternate file tree Files font size</san>

#### 文件字体颜色

目标 CSS 变量: `var(--oz-fta-file-pane-file-name-color)`

默认:
<span class="col-sqr" style="background-color: #6f768599"></span> #6f768599

#### 不使用文件夹图标

目标 CSS 变量: `var(--flexcyon-oz-folder-icons-disabled)`

默认: false (类切换)

#### 不使用文件树头

目标 CSS 变量: `var(--flexcyon-oz-file-tree-header-disabled)`

默认: false (类切换)

#### 启用备用文件夹计数

目标 CSS 变量: `var(--flexcyon-oz-alternate-folder-count)`

默认: false (类切换)

#### 在文件树中启用暗显的文件扩展名

目标 CSS 变量: `var(--flexcyon-oz-dimmed-file-exts-enabled)`

默认: true (类切换)

---

### Full Calendar 插件

接受的格式: x.y, %

#### 暗淡 Full Calendar 插件项目的不透明度

目标 CSS 变量: `var(--flexcyon-fc-dimmed-items-opacity)`

默认: 0.89

<span style="opacity: 0.89">Sample opacity of dimmed full calendar items</span>

---

### Dataview 插件

接受的格式: px

#### Dataview 插件错误消息的水平填充

目标 CSS 变量: `var(--flexcyon-dataview-horizontal-padding)`

默认: 8 (px)

---

### Canvas 插件

定义核心 Canvas 插件的样式

接受的格式: px, RGB

#### 模糊非活跃 Canvas 节点

目标 CSS 变量: `var(--flexcyon-canvas-blur-inactive-nodes)`

默认: false (类切换)

#### 非活跃节点的模糊强度

与前面的设置一起使用，以设置非活动画布节点的模糊强度
以及所有箭头/边。

目标 CSS 变量: `var(--flexcyon-canvas-blur-intensity)`

默认: 1 (px)

#### Canvas 卡菜单对齐

配置 Canvas 卡菜单的对齐方式。

目标 CSS 类: `.flexcyon-canvas-menu-bottom-left,`
`.flexcyon-canvas-menu-bottom-right, .flexcyon-canvas-menu-top-center,
.flexcyon-canvas-menu-top-left, .flexcyon-canvas-menu-top-right,
.flexcyon-canvas-menu-lcenter-center, .flexcyon-canvas-menu-lcenter-top,
.flexcyon-canvas-menu-lcenter-bottom, .flexcyon-canvas-menu-rcenter-center,
.flexcyon-canvas-menu-rcenter-top, .flexcyon-canvas-menu-rcenter-bottom, .flexcyon-canvas-menu-recenter-align`

默认: none (类选项)

选项:

- Bottom left (左下角)

- Bottom right (右下角)

- Top center (顶部中心)

- Top left (左上角)

- Top right (右上角)

- Left aligned center (左对齐中心)

- Left aligned top (左对齐顶部)

- Left aligned bottom (左对齐底部)

- Right aligned center (右对齐中心)

- Right aligned top (右对齐顶部)

- Right aligned bottom (右对齐底部)

- Right aligned center align (右对齐中心对齐)

---

### Various Complements 插件

#### 垂直建议填充

目标 CSS 变量: `var(--flexcyon-var-comps-sugg-vert-padding)`

默认: 7 (px)

#### 水平建议填充

目标 CSS 变量: `var(--flexcyon-var-comps-sugg-horiz-padding)`

默认: 12 (px)

#### 紧凑型建议模式

覆盖默认值。使用 padding 4px 8px.

目标 CSS 变量: `var(--flexcyon-var-comps-compact-mode)`

默认: false (类切换)

---

### Omnisearch 插件

#### 不使用 Omnisearch 图标

目标 CSS 类: `var(--flexcyon-omnisearch-no-icons)`

默认: false (类切换)

#### Omnisearch 机身左边缘

目标 CSS 类: `var(--flexcyon-omnisearch-body-margin-left-margin-left)`

默认: 1.45 (rem)

<!---
TODO: Add Bases section for this and English docs
--->
