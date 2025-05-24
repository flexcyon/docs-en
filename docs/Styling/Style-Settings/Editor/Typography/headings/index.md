---
title: 标题
icon: material/format-header-pound
---

定义与字体权重等标题相关的 CSS 变量。

接受格式: px, 数字, rem

## Navigation
```md
Style Settings
|-- ...
|-- Flexcyon Style Settings
|   |-- Editor
|   |   |-- ...
|   |   |-- Typography
|   |   |   |-- Headings
|   |   |   |-- ...
|   |   |-- ...
|   |-- ...
|-- ...
```

## Configuration Options

### Enable coloured headings
目标CSS变量:`var(--flexcyon-headings-coloured-enabled)`

默认 :true(类切换)
> Inherits from accent colors like `--color-blue`, `--color-red` etc

### Enable soft glow for headings
目标CSS变量:`var(--flexcyon-headings-glow-enabled)`

默认 :false(类切换)

### Enable heading indicators globally
定制全球面前哪些标题有标题指标。 如果你打算逐笔应用,[click here](../../../../CSS-Classes/heading-indicators/index.md)

#### For Heading 1
目标CSS变量:`var(--flexcyon-headings-indicator-h1)`

默认 :false(类切换)
> The CSS Class equivalent can be [found here](../../../../CSS-Classes/heading-indicators/page-1.md)

#### For Heading 2
目标CSS变量:`var(--flexcyon-headings-indicator-h2)`

默认 :false(类切换)
> The CSS Class equivalent can be [found here](../../../../CSS-Classes/heading-indicators/page-2.md)

#### For Heading 3
目标CSS变量:`var(--flexcyon-headings-indicator-h3)`

默认 :false(类切换)
> The CSS Class equivalent can be [found here](../../../../CSS-Classes/heading-indicators/page-3.md)

#### For Heading 4
目标CSS变量:`var(--flexcyon-headings-indicator-h4)`

默认 :false(类切换)
> The CSS Class equivalent can be [found here](../../../../CSS-Classes/heading-indicators/page-4.md)

#### For Heading 5
目标CSS变量:`var(--flexcyon-headings-indicator-h5)`

默认 :false(类切换)
> The CSS Class equivalent can be [found here](../../../../CSS-Classes/heading-indicators/page-5.md)

#### For Heading 6
目标CSS变量:`var(--flexcyon-headings-indicator-h6)`

默认 :false(类切换)
> The CSS Class equivalent can be [found here](../../../../CSS-Classes/heading-indicators/page-6.md)

___ 
### Font size
#### Heading 1 font size
目标CSS变量:`var(--h1-size)`

默认: 1.802(em)

<h1 style="font-weight: 700; font-size: 1.802em;"
>样本 h1</h1>

#### Heading 2 font size
目标CSS变量:`var(--h2-size)`

默认: 1.602 (em)

<h2 style="font-weight: 675; font-size: 1.602em;"
>样本 h2</h2>

#### Heading 3 font size
目标CSS变量:`var(--h3-size)`

默认: 1.424 (em)

<h3 style="font-weight: 650; font-size: 1.424em;"
>样本 h3</h3>

#### Heading 4 font size
目标CSS变量:`var(--h4-size)`

默认: 1. 266 (em)

<h4 style="font-weight: 625; font-size: 1.266;"
>样本 h4</h4>

#### Heading 5 font size
目标CSS变量:`var(--h5-size)`

默认: 1.125 (em)

<h5 style="font-weight: 600; font-size: 1.125em;"
>样本 h5</h5>

#### Heading 6 font size
目标CSS变量:`var(--h6-size)`

默认: 1(em)

<h6 style="font-weight: 575; font-size: 1em;"
>样本 h6</h6>

___ 
### Font weight

#### Heading 1 font weight
目标CSS变量:`var(--h1-weight)`

默认: 700

<h1 style="font-weight: 700; font-size: 1.802em;"
>样本 h1</h1>

#### Heading 2 font weight
目标CSS变量:`var(--h2-weight)`

默认: 675

<h2 style="font-weight: 675; font-size: 1.602em;"
>样本 h2</h2>

#### Heading 3 font weight
目标CSS变量:`var(--h3-weight)`

默认: 650

<h3 style="font-weight: 650; font-size: 1.424em;"
>样本 h3</h3>

#### Heading 4 font weight
目标CSS变量:`var(--h4-weight)`

默认: 625

<h4 style="font-weight: 625; font-size: 1.266;"
>样本 h4</h4>

#### Heading 5 font weight
目标CSS变量:`var(--h5-weight)`

默认: 600

<h5 style="font-weight: 600; font-size: 1.125em;"
>样本 h5</h5>

#### Heading 6 font weight
目标CSS变量:`var(--h6-weight)`

默认: 575

<h6 style="font-weight: 575; font-size: 1em;"
>样本 h6</h6>

___ 
### Line Height

#### Heading 1 line height
目标CSS变量:`var(--h1-line-height)`

默认: 1.2

#### Heading 2 line height
目标CSS变量:`var(--h2-line-height)`

默认: 1.2

#### Heading 3 line height
目标CSS变量:`var(--h3-line-height)`

默认: 1.3

#### Heading 4 line height
目标CSS变量:`var(--h4-line-height)`

默认: 1.4

#### Heading 5 line height
目标CSS变量:`var(--h5-line-height)`

默认: 1.5

#### Heading 6 line height
目标CSS变量:`var(--h6-line-height)`

默认: 1.5

___ 
### Underline

#### Enable underline for Heading 1
目标CSS变量:`var(--flexcyon-h1-underline-enabled)`

默认 :false(类切换)
> The size of the underline scales with your font weight

#### Enable underline for Heading 2
目标CSS变量:`var(--flexcyon-h2-underline-enabled)`

默认 :false(类切换)

#### Enable underline for Heading 3
目标CSS变量:`var(--flexcyon-h3-underline-enabled)`

默认 :false(类切换)

#### Enable underline for Heading 4
目标CSS变量:`var(--flexcyon-h4-underline-enabled)`

默认 :false(类切换)

#### Enable underline for Heading 5
目标CSS变量:`var(--flexcyon-h5-underline-enabled)`

默认 :false(类切换)

#### Enable underline for Heading 6
目标CSS变量:`var(--flexcyon-h6-underline-enabled)`

默认 :false(类切换)