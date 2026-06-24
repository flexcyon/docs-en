---
title: 워크스페이스
---

가독성 라인 길이를 활성화할 때 파일 줄 너비와 흐리게 표시된 요소의 불투명도를 정의합니다.

허용되는 형식: x.y, rem

## 내비게이션

```md
Style Settings
|-- ...
|-- Flexcyon Style Settings
|   |-- Editor
|   |   |-- ...
|   |   |-- Workspace
|   |   |-- ...
|   |-- ...
|-- ...
```

## 환경 설정 옵션

### 파일 줄 너비

대상 CSS 변수: `var(--file-line-width)`

기본값: 50 (rem)

### 흐리게 표시된 요소의 불투명도

대상 CSS 변수: `var(--dimmed)`

기본값: 0.55

<span style="opacity: 0.55">샘플 흐리게 표시된 요소</span>

### 블록 레이블의 불투명도

대상 CSS 클래스: `var(--flexcyon-block-label-opacity)`

기본값: 0.55

<span style="opacity: 0.55">샘플 흐리게 표시된 요소</span>

### 상단 액션 정렬

대상 CSS 변수: `var(--flexcyon-top-actions-alignment)`

기본값: 중앙