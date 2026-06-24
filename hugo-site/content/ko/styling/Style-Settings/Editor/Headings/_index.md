---
title: 제목
---

폰트 굵기와 같은 제목과 관련된 스타일링을 위한 CSS 변수를 정의합니다.

허용되는 형식: px, 숫자, rem

## 내비게이션

```md
Style Settings
|-- ...
|-- Flexcyon Style Settings
|   |-- Editor
|   |   |-- ...
|   |   |-- 제목
|   |   |-- ...
|   |-- ...
|-- ...
```

## 환경 설정 옵션

### 색상이 적용된 제목 활성화

대상 CSS 변수: `var(--flexcyon-headings-coloured-enabled)`

기본값: true (클래스 토글)

> `--color-blue`, `--color-red` 등 Accent Color에서 상속됨

### 제목에 부드러운 빛 효과 활성화

대상 CSS 변수: `var(--flexcyon-headings-glow-enabled)`

기본값: false (클래스 토글)

### 전역적으로 제목 인디케이터 활성화에 대해

전역적으로 어떤 제목 앞에 제목 인디케이터를 표시할지 커스터마이징하세요.
노트별로 적용하려는 경우, [여기를 클릭하세요](../../../css-classes/heading-indicators)

___

## 제목 1

### 제목 1에 대한 제목 인디케이터를 전역적으로 활성화하기

대상 CSS 변수: `var(--flexcyon-headings-indicator-h1)`

기본값: false (클래스 토글)

> CSS 클래스와 동일한 기능은 [여기](../../../css-classes/heading-indicators/page-1)에서 확인할 수 있습니다.

### 제목 1 색상

대상 CSS 변수: `var(--flexcyon-h1-color)`

색상 표시가 활성화된 경우의 제목 1 색상입니다.

기본값: 파랑 (변수 선택)

옵션:

* 시안
* 파랑
* 보라
* 분홍
* 빨강
* 오렌지
* 노랑
* 초록

### 제목 1 글꼴 크기

대상 CSS 변수: `var(--h1-size)`

기본값: 1.818 (em)

<h1 style="font-size: 1.818em;">샘플 h1</h1>

### 제목 1 글꼴 굵기

대상 CSS 변수: `var(--h1-weight)`

기본값: 700

<h1 style="font-weight: 700;">샘플 h1</h1>

### 제목 1 줄 간격

대상 CSS 변수: `var(--h1-line-height)`

기본값: 1.2

### 제목 1에 밑줄 활성화하기

대상 CSS 변수: `var(--flexcyon-h1-underline-enabled)`

기본값: false (클래스 토글)
> 밑줄의 크기는 글꼴 굵기에 따라 조정됩니다.

### 제목 1 정렬

대상 CSS 변수: `var(--flexcyon-heading-1-alignment)`

기본값: 왼쪽 (클래스 선택)

옵션:

- 왼쪽
- 가운데
- 오른쪽

___

## 제목 2

### 제목 2에 대한 제목 인디케이터를 전역적으로 활성화하기

대상 CSS 변수: `var(--flexcyon-headings-indicator-h2)`

기본값: false (클래스 토글)

> CSS 클래스와 동일한 기능은 [여기에서 확인할 수 있습니다](../../../css-classes/heading-indicators/page-2)

### 제목 2 색상

대상 CSS 변수: `var(--flexcyon-h2-color)`

색상 표시가 활성화된 경우의 제목 2 색상입니다.

기본값: 보라 (변수 선택)

옵션:

* 시안
* 파랑
* 보라
* 분홍
* 빨강
* 오렌지
* 노랑
* 초록

### 제목 2 글꼴 크기

대상 CSS 변수: `var(--h2-size)`

기본값: 1.618 (em)

<h2 style="font-size: 1.618em;">샘플 h2</h2>

### 제목 2 글꼴 굵기

대상 CSS 변수: `var(--h2-weight)`

기본값: 675

<h2 style="font-weight: 675;">샘플 h2</h2>

### 제목 2 줄 간격

대상 CSS 변수: `var(--h2-line-height)`

기본값: 1.2

### 제목 2에 밑줄 활성화하기

대상 CSS 변수: `var(--flexcyon-h2-underline-enabled)`

기본값: false (클래스 토글)

### 제목 2 정렬

대상 CSS 변수: `var(--flexcyon-heading-2-alignment)`

기본값: 왼쪽 (클래스 선택)

옵션:

- 왼쪽
- 가운데
- 오른쪽

___

## 제목 3

### 제목 3에 대한 제목 인디케이터를 전역적으로 활성화하기

대상 CSS 변수: `var(--flexcyon-headings-indicator-h3)`

기본값: false (클래스 토글)

> CSS 클래스와 동일한 항목은 [여기에서 확인할 수 있습니다](../../../css-classes/heading-indicators/page-3)

### 제목 3 색상

대상 CSS 변수: `var(--flexcyon-h3-color)`

색상 표시가 활성화된 경우의 제목 3 색상입니다.

기본값: 시안 (변수 선택)

옵션:

* 시안
* 파랑
* 보라
* 분홍
* 빨강
* 오렌지
* 노랑
* 초록

### 제목 3 글꼴 크기

대상 CSS 변수: `var(--h3-size)`

기본값: 1.418 (em)

<h3 style="font-size: 1.418em;">샘플 h3</h3>

### 제목 3 글꼴 굵기

대상 CSS 변수: `var(--h3-weight)`

기본값: 650

<h3 style="font-weight: 650;">샘플 h3</h3>

### 제목 3 줄 간격

대상 CSS 변수: `var(--h3-line-height)`

기본값: 1.3

### 제목 3에 밑줄 활성화하기

대상 CSS 변수: `var(--flexcyon-h3-underline-enabled)`

기본값: false (클래스 토글)

### 제목 3 정렬

대상 CSS 변수: `var(--flexcyon-heading-3-alignment)`

기본값: 왼쪽 (클래스 선택)

옵션:

- 왼쪽
- 가운데
- 오른쪽

___

## 제목 4

### 제목 4에 대한 제목 인디케이터를 전역적으로 활성화하기

대상 CSS 변수: `var(--flexcyon-headings-indicator-h4)`

기본값: false (클래스 토글)

> CSS 클래스와 동일한 기능은 [여기에서 확인할 수 있습니다](../../../css-classes/heading-indicators/page-4)

### 제목 4 색상

대상 CSS 변수: `var(--flexcyon-h4-color)`

색상 표시가 활성화된 경우의 제목 4 색상입니다.

기본값: 분홍 (변수 선택)

옵션:

* 시안
* 파랑
* 보라
* 분홍
* 빨강
* 오렌지
* 노랑
* 초록

### 제목 4 글꼴 크기

대상 CSS 변수: `var(--h4-size)`

기본값: 1.218 (em)

<h4 style="font-size: 1.218em;">샘플 h4</h4>

### 제목 4 글꼴 굵기

대상 CSS 변수: `var(--h4-weight)`

기본값: 625

<h4 style="font-weight: 625;">샘플 h4</h4>

### 제목 4 줄 간격

대상 CSS 변수: `var(--h4-line-height)`

기본값: 1.4

### 제목 4에 밑줄 활성화하기

대상 CSS 변수: `var(--flexcyon-h4-underline-enabled)`

기본값: false (클래스 토글)

### 제목 4 정렬

대상 CSS 변수: `var(--flexcyon-heading-4-alignment)`

기본값: 왼쪽 (클래스 선택)

옵션:

- 왼쪽
- 가운데
- 오른쪽

___

## 제목 5

### 제목 5에 대한 제목 인디케이터를 전역적으로 활성화하기

대상 CSS 변수: `var(--flexcyon-headings-indicator-h5)`

기본값: false (클래스 토글)

> CSS 클래스와 동일한 항목은 [여기에서 확인할 수 있습니다](../../../css-classes/heading-indicators/page-5)

### 제목 5 색상

대상 CSS 변수: `var(--flexcyon-h5-color)`

색상 표시가 활성화된 경우의 제목 5 색상입니다.

기본값: 초록 (변수 선택)

옵션:

* 시안
* 파랑
* 보라
* 분홍
* 빨강
* 오렌지
* 노랑
* 초록

### 제목 5 글꼴 크기

대상 CSS 변수: `var(--h5-size)`

기본값: 1.118 (em)

<h5 style="font-size: 1.118em;">샘플 h5</h5>

### 제목 5 글꼴 굵기

대상 CSS 변수: `var(--h5-weight)`

기본값: 600

<h5 style="font-weight: 600;">샘플 h5</h5>

### 제목 5 줄 간격

대상 CSS 변수: `var(--h5-line-height)`

기본값: 1.5

### 제목 5에 밑줄 활성화하기

대상 CSS 변수: `var(--flexcyon-h5-underline-enabled)`

기본값: false (클래스 토글)

### 제목 5 정렬

대상 CSS 변수: `var(--flexcyon-heading-5-alignment)`

기본값: 왼쪽 (클래스 선택)

옵션:

- 왼쪽
- 가운데
- 오른쪽

___

## 제목 6

### 제목 6에 대한 제목 인디케이터를 전역적으로 활성화하기

대상 CSS 변수: `var(--flexcyon-headings-indicator-h6)`

기본값: false (클래스 토글)

> CSS 클래스와 동일한 내용은 [여기에서 확인할 수 있습니다](../../../css-classes/heading-indicators/page-6)

### 제목 6 색상

대상 CSS 변수: `var(--flexcyon-h6-color)`

색상 표시가 활성화된 경우의 제목 6 색상입니다.

기본값: 노랑 (변수 선택)

옵션:

* 시안
* 파랑
* 보라
* 분홍
* 빨강
* 오렌지
* 노랑
* 초록

### 제목 6 글꼴 크기

대상 CSS 변수: `var(--h6-size)`

기본값: 1.018 (em)

<h6 style="font-size: 1.018em;">샘플 h6</h6>

### 제목 6 글꼴 굵기

대상 CSS 변수: `var(--h6-weight)`

기본값: 575

<h6 style="font-weight: 575;">샘플 h6</h6>

### 제목 6 줄 간격

대상 CSS 변수: `var(--h6-line-height)`
기본값: 1.5

### 제목 6에 밑줄 활성화하기

대상 CSS 변수: `var(--flexcyon-h6-underline-enabled)`

기본값: false (클래스 토글)

### 제목 6 정렬

대상 CSS 변수: `var(--flexcyon-heading-6-alignment)`

기본값: 왼쪽 (클래스 선택)

옵션:

- 왼쪽
- 가운데
- 오른쪽