---
title: flexcyon Multi Column Implementation (FMCi)
---

## 소개

flexcyon Multi Column implementation (FMCi)은 `@kneecaps`(Obsidian Members Group,
Ultra Lobster/Origami 테마 개발자)의 다단 레이아웃 + aside float 스니펫을
(허락을 받아) 각색한 것입니다.

`efemkay`의 MCL(핵심 로직만 최소한으로 가져와 SCSS로 재구현)과
`Bluemoondragon07`의 Wikipedia 테마 aside/infobox에서도 영감을 얻었습니다.

Aside/infobox는 읽기 모드에서 본문 텍스트 옆으로 오른쪽에 떠서 표시됩니다.
aside 콜아웃의 내용이 옆에 렌더링되기를 원하는 문단 위에 배치하세요.
Willemstad 같은 테마에서 볼 수 있는 코넬 노트 스타일(텍스트 내용 옆의 "스티키 노트")과
혼동하지 마세요.

> Wikipedia, ITS, Fancy-a-story 테마에서 볼 수 있는 정보 상자를
떠올리면 됩니다.
>
> 다만 flexcyon의 구현은 다른 테마에 비해 핵심 기능 위주로
> 더 간소화되어 있습니다.

개별 저자에 대한 링크와 자세한 내용은 [credits](/credits#코드-조각)에 있습니다.

### 옵션

커스텀 콜아웃 / 콜아웃 메타데이터:

- "multi-column"/"col"

> `multi-column`은 하위 호환성을 위해 유지됩니다

- "wide-`<value>`" (허용되는 값은 0에서 100까지)

> 참고:
>
> `wide-0`은 콜아웃이 텍스트 내용에 맞는 최소 너비를 사용하도록 강제합니다
> `wide-1`은 아무 일도 하지 않지만 일부 사람들에게 안정감을 줍니다
>
> wide-x 메타데이터보다, 같은 열에 있는 모든 콜아웃의 텍스트 내용이 알맞게
> 들어가도록 하는 것을 우선합니다.

- "aside"/"infobox"

## 사용법

### 다단(Multi Column)

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
