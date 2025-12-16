---
title: Settings
icon: material/cogs
---

用于自定义设置的各种 UI 方面的外观。

接受的格式: x.y, rem, px

## 导航

```md
Style Settings
|-- ...
|-- Flexcyon Style Settings
| |-- ...
| |-- Settings
| |-- ...
|-- ...
```

## 配置选项

### 启用社区项目样式

目标 CSS 变量: `var(--flexcyon-settings-comm-item-enabled)`

默认: true (类切换)

### 社区项目的不透明性 (未选中)

目标 CSS 变量: `var(--flexcyon-comm-item-opacity)`

默认: 0.89

<span style="opacity: 0.89">Sample opacity of community items (unselected)</span>

### 工具提示左侧边距

目标 CSS 变量: `var(--flexcyon-settings-installed-tooltip-left-margin)`

默认: 1 (rem)

### 在设置中不显示滚动条

目标 CSS 变量: `var(--flexcyon-settings-scrollbar-removed)`

默认: true (类切换)

### 在设置中启用备用活跃项样式

目标 CSS 变量: `var(--flexcyon-enable-alt-active-item-effect)`

默认: true (类切换)

<!--- 
TODO: Add Input box padding settings here later.
--->

---

### 样式设置

为样式设置配置外观

接受的格式: px

#### 样式设置标题之间的缩进宽度

目标 CSS 变量: `var(--flexcyon-style-settings-indent-width)`

默认: 4 (px)

#### 暗淡的折叠样式设置标题

目标 CSS 变量: `var(--flexcyon-style-settings-dim-collapsed-headings)`

默认: true
