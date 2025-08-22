---
title: Layout
icon: material/page-layout-sidebar-left
---

配置工作区布局。

## 导航

```md
Style Settings
|-- ...
|-- Flexcyon Style Settings
| |-- Editor
| | |-- ...
| | |-- Layout
| | |-- ...
| |-- ...
|-- ...
```

## 配置选项

### 选择工作区布局

目标 CSS 类: `.flexcyon-workspace-card-layout,
.flexcyon-workspace-angled-layout, .flexcyon-workspace-pl10k-layout`

默认: none (类选项)

选项:

- Cards Layout (卡片布局)
- Angled Layout (倾斜布局)
- Powerlevel10k Layout (Powerlevel10k 灵感布局)

> 工作区布局更改可能需要重新加载或重新启动应用程序才能生效

### 启用 TUI 附加进行卡片布局

目标 CSS 变量: `var(--flexcyon-workspace-cards-tui-ext)`

默认: true (类切换)
