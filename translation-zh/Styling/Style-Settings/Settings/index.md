---
title: 设置
icon: material/cogs
---

用于自定义设置的 UI 不同方面的外观 。

接受格式: x.y, rem, px

## Navigation
```md
Style Settings
|-- ...
|-- Flexcyon Style Settings
|   |-- ...
|   |-- Settings
|   |-- ...
|-- ...
```

## Configuration Options

### Smiley Toggle Icons in Settings
目标CSS变量:`var(--flexcyon-settings-smiley-icons-enabled)`

默认 :true(类切换)

### Coloured Icons in Settings
目标CSS变量:`var(--flexcyon-settings-coloured-icons)`

默认 :false(类切换)

### Enable community item effects
目标CSS变量:`var(--flexcyon-settings-comm-item-enabled)`

默认 :true(类切换)

### Opacity of community items (unselected)
目标CSS变量:`var(--flexcyon-comm-item-opacity)`

默认: 0.89

<span style="opacity: 0.89"
>社区物品样本不透明(未选定)</span>

### Installed tooltip left margin
目标CSS变量:`var(--flexcyon-settings-installed-tooltip-left-margin)`

默认:1 (rem)

### Do not show scrollbar in settings
目标CSS变量:`var(--flexcyon-settings-scrollbar-removed)`

默认 :true(类切换)

### Enabled alternate active item effect in settings
目标CSS变量:`var(--flexcyon-enable-alt-active-item-effect)`

默认 :true(类切换)

___ 

### Style Settings
配置样式设置的外观

接受格式: px

#### Indentation width between style settings headings
目标CSS变量:`var(--flexcyon-style-settings-indent-width)`

默认: 4(px)

#### Dim collapsed style settings headings
目标CSS变量:`var(--flexcyon-style-settings-dim-collapsed-headings)`

默认 :true