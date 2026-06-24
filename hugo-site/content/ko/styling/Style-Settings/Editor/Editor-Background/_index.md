---
title: 편집기 배경
---

편집기 배경 설정하기

허용되는 형식: px, deg

## 내비게이션

```md
Style Settings
|-- ...
|-- Flexcyon Style Settings
|   |-- Editor
|   |   |-- ...
|   |   |-- Editor Background
|   |   |-- ...
|   |-- ...
|-- ...
```

## 환경 설정 옵션

### 배경 유형 선택

대상 CSS 클래스: `.flexcyon-editor-grid, .flexcyon-editor-dots, .flexcyon-editor-rhombus`

기본값: 없음(클래스 선택)

옵션:

- 격자 배경
- 점선 배경
- 마름모 배경

### 격자 및 마름모 배경의 회전 값

대상 CSS 변수: `var(--flexcyon-editor-bg-rotation)`

기본값: 0 (deg)

### 격자/점선 배경의 각 점/선 간의 너비

대상 CSS 변수: `var(--flexcyon-editor-bg-width)`

기본값: 15 (px)

### 점선 배경의 점 크기

대상 CSS 변수: `var(--flexcyon-editor-dot-size)`

기본값: 2 (px)