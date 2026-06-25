---
title: 콜아웃
---

콜아웃 스타일 설정하기

허용되는 형식: px, rem, em, ms

## 내비게이션

```md
Style Settings
|-- ...
|-- Flexcyon Style Settings
|   |-- Editor
|   |   |-- ...
|   |   |-- 콜아웃
|   |   |-- ...
|   |-- ...
|-- ...
```

## 환경 설정 옵션

### 콜아웃 아이콘 오른쪽 패딩

대상 CSS 변수: `var(--flexcyon-callout-icon-right-padding)`

기본값: 4 (px)

### 첫 번째 코드블록 위쪽 여백

대상 CSS 변수: `var(--flexcyon-callout-first-codeblock-margin-top)`

기본값: 1 (rem)

### 콜아웃 메타데이터 배경 불투명도

대상 CSS 변수: `var(--flexcyon-callout-bg-opacity)`

기본값: 20%

<span style="opacity: 20%">샘플 배경 불투명도</span>

### 콜아웃 세로 여백

대상 CSS 변수: `var(--flexcyon-callout-vertical-margin)`

기본값: 1 (em)

### 콜아웃 세로 패딩

대상 CSS 변수: `var(--flexcyon-callout-vertical-padding)`

기본값: 12 (px)

### 콜아웃 가로 패딩

대상 CSS 변수: `var(--flexcyon-callout-horiz-padding)`

기본값: 24 (px)

### 콜아웃 모서리 둥글기

대상 CSS 변수: `var(--callout-radius)`

기본값: 2 (px)

### 콜아웃 추가 모서리 둥글기

대상 CSS 변수: `var(--flexcyon-callout-radix)`

기본값: 16 (px)

### 콜아웃 스타일 선택

대상 CSS 클래스: `.flexcyon-tui-callouts, .flexcyon-plain-callouts, .flexcyon-vert-callouts`

기본값: 없음 (클래스 선택)

옵션:

- TUI 콜아웃s
- Plain 콜아웃s
- Vertical 콜아웃s

### TUI 콜아웃에 대한 아이콘 비활성화


대상 CSS 클래스: `.flexcyon-tui-no-icons`

기본값: false (클래스 토글)

___
### 플래시카드 콜아웃

[플래시카드 콜아웃](../../../callout-metadata/flashcard)을 구성합니다.

#### 플래시카드 콜아웃 너비

대상 CSS 변수: `var(--flexcyon-callouts-flashcard-width)`

기본값: 250 (px)

#### 플래시카드 콜아웃 높이

대상 CSS 변수: `var(--flexcyon-callouts-flashcard-height)`

기본값: 250 (px)

#### 플래시카드 콜아웃 애니메이션 지속 시간

대상 CSS 변수: `var(--flexcyon-callout-flashcard-animation-duration)`

기본값: 500 (ms)

___
### 팝업 콜아웃

[팝업 콜아웃](../../../callout-metadata/popup)을 구성합니다.

#### 팝업 콜아웃 애니메이션 지속 시간

대상 CSS 변수: `var(--flexcyon-callout-pop-animation-duration)`

기본값: 200 (ms)