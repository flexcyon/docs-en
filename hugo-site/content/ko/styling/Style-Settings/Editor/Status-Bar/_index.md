---
title: 상태바
---

상태바를 구성하기 위한 CSS 변수 정의

허용되는 형식: ms, px

## 내비게이션

```md
Style Settings
|-- ...
|-- Flexcyon Style Settings
|   |-- Editor
|   |   |-- ...
|   |   |-- 상태바
|   |   |-- ...
|   |-- ...
|-- ...
```

## 환경 설정 옵션

### 상태바

#### 트리거까지 숨기기

대상 CSS 클래스: `.flexcyon-status-hide-until-hover
.flexcyon-status-hide-until-hold`

기본값: 없음(클래스 선택)

옵션:

- 호버까지 숨기기
- 홀드까지 숨기기

#### 상태바 정렬
대상 CSS 클래스: `.flexcyon-status-right-align
.flexcyon-status-centre-align`

기본값: 없음(클래스 선택)

옵션:

- 가운데
- 오른쪽

왼쪽 정렬은 너무 하드코딩되었으므로 제거되었습니다.

#### 호버까지 숨기기 활성화 시 표시 텍스트

대상 CSS 변수: `var(--flexcyon-status-hide-until-hover-text)`

기본값: "상태 표시"

#### 호버 시 상태바 표시 이동 거리

대상 CSS 변수: `var(--flexcyon-status-hide-until-hover-translation)`

기본값: 1500 (px)

#### 호버 시 상태바 표시 전환 지속 시간

대상 CSS 변수: `var(--flexcyon-status-hide-hover-duration)`

기본값: 325 (ms)

#### 호버 시 상태바 표시 전환 타이밍 함수

대상 CSS 변수: `var(--flexcyon-status-hide-hover-function)`

기본값: ease-out

___
### 텍스트 구성

#### 모드 상태에 아이콘 대신 텍스트 사용

대상 CSS 변수: `var(--flexcyon-status-text-mode)`

기본값: false (클래스 토글)

#### 읽기 모드 텍스트

대상 CSS 변수: `var(--flexcyon-status-reading-text)`

기본값: "READ"

#### 소스 모드 텍스트

대상 CSS 변수: `var(--flexcyon-status-source-text)`

기본값: "SOURCE"

#### Live Preview 모드 텍스트

대상 CSS 변수: `var(--flexcyon-status-live-text)`

기본값: "LIVE"

___

### 상태바 스타일링

#### 모바일에서 상태바 표시

대상 CSS 변수: `var(--flexcyon-status-mobile-enabled)`

기본값: false (클래스 토글)

#### 상태바 글꼴 크기

대상 CSS 변수: `var(--status-bar-font-size)`

기본값: 13.7533 (px)

#### 상태바 스타일 선택

대상 CSS 클래스: `.flexcyon-status-style-angled,
.flexcyon-status-style-card, .flexcyon-status-style-pl10k`

기본값: 없음(클래스 선택)

옵션:

- Angled
- 카드
- Powerlevel10k

#### 상태바 텍스트 색상 활성화

대상 CSS 변수: `var(--flexcyon-status-text-enable-color)`

기본값: false (클래스 토글)

#### 새 탭에서 상태바 표시 안 함

대상 CSS 변수: `var(--flexcyon-no-status-in-new-tab)`

기본값: false (클래스 토글)

#### 새 탭에서 상태바 불투명도

대상 CSS 변수: `var(--flexcyon-status-new-tab-opacity)`

기본값: 0.55