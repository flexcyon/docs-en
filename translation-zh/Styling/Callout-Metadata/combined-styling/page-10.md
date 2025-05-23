---
title: 扩展调色板 - 组合样式
icon: material/palette-outline
---
> `all-color1-color2-`
用法 :
```md
> [!tip|all-red-blue] Title will be the color mix of red and blue colors of this theme
> The background color will be the color mix of red and blue colors of this theme
```
> Shorthand for both ["bg-color1-color2"](../bg-styling/page-10.md) and ["title-color1-color2"](../title-styling/page-10.md)

也可以在自己的css片段中使用这种颜色,其形式为:
> - `var(--color-color1-color2-mix)`: E.g. `var(--color-red-blue-mix)`
> - `var(--color-color1-color2-mix-bg)`: E.g. `var(--color-red-blue-mix-bg)`


要求[this Style Settings option](../../Style-Settings/Editor/Accent-Colors/index.md#enabled-extended-color-palette)