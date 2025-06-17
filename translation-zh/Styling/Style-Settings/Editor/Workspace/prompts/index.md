---
title: 提示
icon: material/text-box
---

配置命令提示器, 快速切换器等提示 。

接受格式: px, vw, vh

## Navigation

```md
Style Settings
|-- ...
|-- Flexcyon Style Settings
| |-- Editor
| | |-- ...
| | |-- Workspace
| | | |-- ...
| | | |-- Prompts
| | | |-- ...
| | |-- ...
| |-- ...
|-- ...
```

## Configuration Prompts

### Prompt width

目标CSS变量:`var(--prompt-width)`

默认: 700 (px)

### Prompt max width

目标CSS变量:`var(--prompt-max-width)`

默认: 80 (vw)

### Prompt max height

目标CSS变量:`var(--prompt-max-height)`

默认: 70(vh)

### Prompt alignment

CSS Classe(s) targeted: `.flexcyon-prompt-align-bottom-left,
.flexcyon-prompt-align-bottom-center, .flexcyon-prompt-align-center-left,
.flexcyon-prompt-align-top-left, .flexcyon-prompt-align-top-center`

默认: 无( 类选择)
选项 :

- 左边
- 顶部center
- 中间左边 -左边
- 下边center

### Suggestion item vertical padding

目标CSS变量:`var(--flexcyon-suggestion-verti-padding)`

默认: 8 (px)

### Suggestion item horizontal padding

目标CSS变量:`var(--flexcyon-suggestion-horiz-padding)`

默认: 12 (px)
