---
title: Cursor
icon: material/cursor-text
---

配置光标。

## 导航

```md
Style Settings
|-- ...
|-- Flexcyon Style Settings
| |-- Editor
| | |-- ...
| | |-- Cursor
| |-- ...
|-- ...
```

## 配置选项

### 默认光标类型

目标 CSS 变量: `var(--flexcyon-cursor-type)`

当应用程序未指定光标类型时, 设置光标类型。

默认: auto (变量选项)

选项: 有关选项的完整列表, 请查看 [MDN 上的光标样式](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/cursor)

### 启用平滑光标

目标 CSS 类: `var(--flexcyon-enable-smooth-cursor)`

默认: true

### 平滑光标过渡持续时间

目标 CSS 类: `var(--flexcyon-cursor-duration)`

默认: 42.5 (ms)

### 平滑光标计时函数

目标 CSS 类: `var(--flexcyon-cursor-timing-fn)`

默认: ease-in

### 平滑光标最小宽度

目标 CSS 类: `var(--flexcyon-cursor-min-width)`

默认: unset
