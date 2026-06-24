---
title: 프롬프트
---

명령 프롬프트, 빠른 전환기 등 프롬프트 설정하기

허용되는 형식: px, vw, vh

## 내비게이션

```md
Style Settings
|-- ...
|-- Flexcyon Style Settings
|   |-- Editor
|   |   |-- ...
|   |   |-- Workspace
|   |   |   |-- ...
|   |   |   |-- Prompts
|   |   |   |-- ...
|   |   |-- ...
|   |-- ...
|-- ...
```

## 환경 설정 프롬프트

### 프롬프트 너비

대상 CSS 변수: `var(--prompt-width)`

기본값: 700 (px)

### 프롬프트 최대 너비

대상 CSS 변수: `var(--prompt-max-width)`

기본값: 80 (vw)

### 프롬프트 최대 높이

대상 CSS 변수: `var(--prompt-max-height)`

기본값: 70 (vh)

### 프롬프트 정렬

대상 CSS 클래스: `.flexcyon-prompt-align-bottom-left,
.flexcyon-prompt-align-bottom-center, .flexcyon-prompt-align-center-left,
.flexcyon-prompt-align-top-left, .flexcyon-prompt-align-top-center`

기본값: 없음 (클래스 선택)

옵션:

- 왼쪽 상단
- 가운데 상단
- 왼쪽 가운데
- 왼쪽 하단
- 가운데 하단

### 제안 항목 세로 패딩

대상 CSS 변수: `var(--flexcyon-suggestion-verti-padding)`

기본값: 8 (px)

### 제안 항목 가로 패딩

대상 CSS 변수: `var(--flexcyon-suggestion-horiz-padding)`

기본값: 12 (px)