---
title: flexcyon's Multi Column Implementation (FMCi)
---

## About

flexcyon's Multi Column implementation (FMCi) was adapted
(with permission) from `@kneecaps`' (Obsidian Members Group, 
Ultra Lobster/Origami theme developer)
multi-column layout + aside float snippet.

I also took inspiration from `efemkay`'s MCL
(bare minimum core logic, reimplemented in SCSS)
and the Wikipedia theme's asides/infoboxes by `Bluemoondragon07`.

Asides/infoboxes float right alongside body text in Reading Mode,
place above paragraph where aside callout contents will render
beside. Not to be confused with Cornell Notes styling
("sticky notes" beside text content) like seen in themes like Willemstad.

> Think of it like the info boxes seen in Wikipedia, 
ITS and Fancy-a-story Theme.
>
> That being said flexcyon's rendition is more stripped down to
> the core feature(s).

Links to individual authors and more about them is under [credits](/credits#snippets).

### Options

Custom Callout / Callout Metadata:

- "multi-column"/"col"

> `multi-column` is kept for backwards compatibility

- "wide-`<value>`" (Accepted values from 0 to 100)

> Note: 
> 
> `wide-0` forces the callout to use the bare minimum width which fits text content
> `wide-1` does nothing but makes some people feel comfortable
> 
> It will try to respect fitting text content for all callouts in the same column
> before wide-x metadata. 

- "aside"/"infobox"

## Usage

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
