---
title: Lucide Icons
icon: material/emoticon-cool
---

自定 Callout / Callout 元数据: "`<lucide-icon-value>`"

用法:

```md
> [!info|lucide-git-fork] The callout icon will be replaced by the lucide git
fork icon
> The callout content will render as normal.
```

## 请注意
使用 Lucide 图标设置时, 整个 Callout 元数据或自定义标注部分必须与 Lucide 图标值匹配, 否则图标将无法呈现。

- 例如，`>[!lucide-git-fork|title-orange]` 而不是 `>[!note|lucide-git-fork title-orange]` 或 `>[!title-orange|lucide-git-fork]`

（您不能指定多个自定义标注类型，但可以使用标注元数据进行修改）

