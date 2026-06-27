---
title: flexcyon's Multi Column 实现 (FMCi)
---

## 关于 FMCi

flexcyon's Multi Column 实现 (FMCi) (经许可）改编自于
`@kneecaps`（OMG Discord, Ultra Lobster, Origami 主题开发人员)
的 multi-column 与 aside float CSS 代码段.

我还从 `efemkay` 的 MCL (最低限度核心逻辑, 在 SCSS 中重新实现)
和 `Bluemoondragon07` 的 Wikipedia (维基百科) 主题 aside/infoboxes
中获得了灵感.

在 Reading Mode (阅读模式) 下, asides/infoboxes 直接浮动在正文旁边,
放置在段落上方, 侧边栏标注内容将显示在旁边.

> 不要与 Willemstad 等主题中的 Cornell Notes (康奈尔笔记) 样式
> (文本内容旁边的 "便签") 混淆.

> 您可以把它想象成类似于 Wikipedia (维基百科), ITS 和 Fancy-a-Story
主题中 的 infoboxes.
>
> 请注意，与其他主题相比，此主题的呈现更精简到核心功能

关于原作者的链接及更多信息, 请参见 [鸣谢章节](/credits#snippets).

### 选项

自定义 Callout / Callout 元数据:

- "multi-column"/"col"

> 保留 `multi-column` 是为了向后兼容

- "wide-`<value>`" (可接受的值范围为 0 到 100)

> 注:
> 
> `wide-0` 强制 callout 使用适合文本内容的最小宽度
> `wide-1` 没什么作用
> 
> 它将尝试尊重同一列中所有标注的合适文本内容
> 在 `wide-x` 元数据之前.

- "aside"/"infobox"

## 用法

### Multi Column

```md
> [!multi-column] Title will not be displayed
>>[!note|transparent-bg] Placeholder title
>> Placeholder content
>
>>[!info] Placeholder title
>> Placeholder content
```

```md
> [!col] Title will not be displayed
>>[!note|transparent-bg] Placeholder title
>> Placeholder content
>
>>[!info|wide-3] Placeholder title
>> Placeholder content
```

### Aside/Infobox

```md
> [!aside] Aside title
> Aside content. I with title will render in
> reading mode floating to the right of text content.

Place asides above text paragraphs which you
want to have positioned to the left of the aside callout.
```

```md
> [!infobox] Infobox title
> Infobox content. I with title will render in
> reading mode floating to the right of text content.

Place asides above text paragraphs which you
want to have positioned to the left of the infobox callout.
```
