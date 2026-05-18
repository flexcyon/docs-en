---
title: 扩展调色板 - 组合样式
---

> `all-color1-color2-`

用法:

```md
> [!tip|all-red-blue] Title will be the color mix of red and blue colors of 
this theme
> The background color will be the color mix of red and blue colors of this theme
```

> ["bg-color1-color2"](../bg-styling/page-10) 和 ["title-color1-color2"](../title-styling/page-10) 的简写

您也可以在自己的 CSS 代码片段中使用这些颜色, 它们的形式如下：

> - `var(--color-color1-color2-mix)`: E.g. `var(--color-red-blue-mix)`
> - `var(--color-color1-color2-mix-bg)`: E.g. `var(--color-red-blue-mix-bg)`

需要启用此 ["样式设置" 选项](../../../style-settings/editor/accent-colors#启用扩展调色板).
