---
title: 설정
---

설정의 다양한 UI 요소의 모양을 커스터마이징하기 위한 것입니다.

허용되는 형식: x.y, rem, px

## 내비게이션

```md
Style Settings
|-- ...
|-- Flexcyon Style Settings
|   |-- ...
|   |-- Settings
|   |-- ...
|-- ...
```

## 환경 설정 옵션

### 커뮤니티 아이템 효과 활성화

대상 CSS 변수: `var(--flexcyon-settings-comm-item-enabled)`

기본값: true (클래스 토글)

### 커뮤니티 아이템(비선택 상태)의 불투명도

대상 CSS 변수: `var(--flexcyon-comm-item-opacity)`

기본값: 0.89

<span style="opacity: 0.89">커뮤니티 아이템(비선택 상태)의 샘플 불투명도</span>

### 설치된 툴팁 왼쪽 여백

대상 CSS 변수: `var(--flexcyon-settings-installed-tooltip-left-margin)`

기본값: 1 (rem)

### 설정에서 스크롤바 표시 안 함

대상 CSS 변수: `var(--flexcyon-settings-scrollbar-removed)`

기본값: true (클래스 토글)

### 설정에서 대체 활성 아이템 효과 활성화

대상 CSS 변수: `var(--flexcyon-enable-alt-active-item-effect)`

기본값: true (클래스 토글)

___

### Style Settings

Style Settings에 대한 모양을 설정합니다.

허용되는 형식: px

#### Style Settings 제목 간의 들여쓰기 폭

대상 CSS 변수: `var(--flexcyon-style-settings-indent-width)`

기본값: 4 (px)

#### 축소된 Style Settings 제목을 흐리게 표시

대상 CSS 변수: `var(--flexcyon-style-settings-dim-collapsed-headings)`

기본값: true