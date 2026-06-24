---
title: 애니메이션
---

프롬프트, 모달, 탭 컨테이너의 전환 애니메이션 설정하기

허용되는 형식: ms

## 내비게이션

```md
Style Settings
|-- ...
|-- Flexcyon Style Settings
|   |-- Editor
|   |   |-- ...
|   |   |-- Animations
|   |   |-- ...
|   |-- ...
|-- ...
```

## 환경 설정 옵션

### 노트 애니메이션 유형

대상 CSS 클래스: `.flexcyon-anims-slide-rtl, .flexcyon-anims-slide-ltr,
.flexcyon-anims-slide-tb, .flexcyon-anims-slide-bt, .flexcyon-anims-spin-bt, .flexcyon-anims-spin-rl, .flexcyon-anims-scale-up`
> 변경 사항은 앱 새로고침/재시작 후에 적용될 수 있습니다

기본값: 없음(클래스 선택)

옵션:

- 왼쪽에서 오른쪽으로 슬라이드
- 오른쪽에서 왼쪽으로 슬라이드
- 위에서 아래로 슬라이드
- 아래에서 위로 회전
- 오른쪽에서 왼쪽으로 회전
- 스케일 업
- 페이드 인

### 모달 애니메이션 유형

대상 CSS 클래스: `.flexcyon-modal-anims-slide-rtl, .flexcyon-modal-anims-slide-ltr,
.flexcyon-modal-anims-slide-tb, .flexcyon-modal-anims-slide-bt, .flexcyon-modal-anims-spin-bt, .flexcyon-modal-anims-spin-rl, .flexcyon-modal-anims-scale-up`
> 변경 사항은 앱 새로고침/재시작 후에 적용될 수 있습니다

기본값: 없음(클래스 선택)

옵션:

- 왼쪽에서 오른쪽으로 슬라이드
- 오른쪽에서 왼쪽으로 슬라이드
- 위에서 아래로 슬라이드
- 아래에서 위로 회전
- 오른쪽에서 왼쪽으로 회전
- 스케일 업
- 페이드 인

### 애니메이션 지속 시간

대상 CSS 변수: `var(--flexcyon-anim-duration)`

기본값: 300 (ms)

### 애니메이션 이징 함수

대상 CSS 변수: `var(--flexcyon-anim-easing)`

기본값: ease-in

### 애니메이션 슬라이드 양

슬라이드 애니메이션이 이동할 픽셀 수입니다.

대상 CSS 변수: `var(--flexcyon-anim-slide-amount)`

기본값: 56.6311 (px)

### Style Settings 컨테이너에서 애니메이션 활성화

대상 CSS 변수: `var(--flexcyon-anim-style-settings-contain)`

기본값: false

### 스케일 애니메이션 초기 스케일링

대상 CSS 변수: `var(--flexcyon-anim-start-scale-amt)`

기본값: 0.33

### 애니메이션 초기 불투명도

대상 CSS 변수: `var(--flexcyon-anim-start-opacity)`

기본값: 0.55