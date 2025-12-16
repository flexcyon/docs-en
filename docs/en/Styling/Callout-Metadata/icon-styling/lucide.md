---
title: Lucide Icons
icon: material/emoticon-cool
---

Custom Callout / Callout Metadata: "`<lucide-icon-value>`"

Usage:

```md
> [!info|lucide-git-fork] The callout icon will be replaced by the lucide git
fork icon
> The callout content will render as normal.
```

## Note
When using lucide icon setting, either the entire callout metadata or custom callout section must match the lucide icon value else the icon will not render.

- E.g. `>[!lucide-git-fork|title-orange bg-blue]` instead of `>[!bg-blue|lucide-git-fork title-orange]` or `>[!lucide-git-fork title-orange|bg-blue]`

In short, you cannot use Lucide icon callout type within the same callout type or metadata.

This feature **requires at least Obsidian Version 1.9.12**.
