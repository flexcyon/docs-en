---
title: 版式
icon: material/page-layout-sidebar-left
---

配置工作空间布局 。

## Navigation

```md
Style Settings
|-- ...
|-- Flexcyon Style Settings
| |-- Editor
| | |-- ...
| | |-- Workspace
| | | |-- ...
| | | |-- Layout
| | |-- ...
| |-- ...
|-- ...
```

## Configuration Options

### Select workspace layout

CSS Classe(s) targeted: `.flexcyon-workspace-card-layout,
.flexcyon-workspace-angled-layout, .flexcyon-workspace-pl10k-layout`

默认: 无( 类选择)

选项 :

- 卡片布局
- 愤怒的布局
- 动力级10k布局
  > Workspace layout changes may need app reload or restart to take effect

### Enable TUI add-on for cards layout

目标CSS变量:`var(--flexcyon-workspace-cards-tui-ext)`

默认 :true(类切换)
