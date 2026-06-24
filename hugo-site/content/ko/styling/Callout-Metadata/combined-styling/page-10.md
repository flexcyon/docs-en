---
title: 확장 색상 팔레트 결합
---

> `all-color1-color2-`

사용법:

```md
> [!tip|all-red-blue] 제목은 이 테마의 빨간색과 파란색이 혼합된 색상이 됩니다.
> 배경색은 이 테마의 빨간색과 파란색이 혼합된 색상이 됩니다.
```

> ["bg-color1-color2"](../bg-styling/page-10)와 ["title-color1-color2"](../title-styling/page-10) 모두를 위한 단축형

이 색상을 사용자 정의 CSS 스니펫에서도 사용할 수 있으며, 다음과 같은 형식을 따릅니다.

> - `var(--color-color1-color2-mix)`: 예: `var(--color-red-blue-mix)`
> - `var(--color-color1-color2-mix-bg)`: 예: `var(--color-red-blue-mix-bg)`


[이 Style Settings 옵션](../../../style-settings/editor/accent-colors#enable-extended-color-palette)이 켜져 있어야 합니다.