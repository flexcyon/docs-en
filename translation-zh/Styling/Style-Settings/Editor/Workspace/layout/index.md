---
title: 版式
icon: material/page-layout-sidebar-left
---

Configure the workspace layout.

## Navigation

```md
Style Settings
|-- ...
|-- Flexcyon Style Settings
|   |-- Editor
|   |   |-- ...
|   |   |-- Workspace
|   |   |   |-- ...
|   |   |   |-- Layout
|   |   |-- ...
|   |-- ...
|-- ...
```

## Configuration Options

### Select workspace layout

CSS Classe(s) targeted: `.flexcyon-workspace-card-layout,
.flexcyon-workspace-angled-layout, .flexcyon-workspace-pl10k-layout`

默认: 无( 类选择)

选项 :

- Cards Layout
- Angled Layout
- Powerlevel10k Layout
> Workspace layout changes may need app reload or restart to take effect

### Enable TUI add-on for cards layout

目标CSS变量:`var(--flexcyon-workspace-cards-tui-ext)`

默认 :true(类切换)

