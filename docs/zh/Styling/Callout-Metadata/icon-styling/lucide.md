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
使用 Lucide 图标设置时, 整个 Callout 元数据或自定义标注部分必须与 Lucide 图标值匹配, 否则图标将无法呈现.

- 例如 `>[!lucide-git-fork|title-orange bg-blue]` 而不是 `>[!bg-blue|lucide-git-fork title-orange]` 或 `>[!lucide-git-fork title-orange|bg-blue]`

您不能在同一个 Callout 类型或元数据中使用 Lucide 图标标注类型.

此功能至少需要 **Obsidian 1.9.12 版本**.
