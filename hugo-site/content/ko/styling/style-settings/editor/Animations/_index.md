---
title: 애니메이션
---

프롬프트, 모달, 탭 컨테이너의 전환 애니메이션 설정하기

허용되는 형식: ms

## 내비게이션

```md
Style Settings
|-- flexcyon://Editor
|   |-- Animations
```

## 환경 설정 옵션

### 노트 애니메이션 유형

대상 CSS 클래스:

`.flexcyon-anims-fade-in, .flexcyon-anims-scale-up,
.flexcyon-anims-pop-in, .flexcyon-anims-pulse-in`,

`.flexcyon-anims-slide-ltr, .flexcyon-anims-slide-rtl, 
.flexcyon-anims-slide-tb, .flexcyon-anims-slide-bt,
.flexcyon-anims-slide-tl, .flexcyon-anims-slide-tr,
.flexcyon-anims-slide-bl, .flexcyon-anims-slide-br`,

`.flexcyon-anims-spin-rl, .flexcyon-anims-spin-lr,
.flexcyon-anims-spin-bt, .flexcyon-anims-spin-tb,
.flexcyon-anims-flip-x, .flexcyon-anims-flip-y`,

`.flexcyon-anims-blur-in, .flexcyon-anims-bounce-in,
.flexcyon-anims-swing-in`,

`.flexcyon-anims-glide-in, .flexcyon-anims-aura-glow,
.flexcyon-anims-tv-effect, .flexcyon-anims-apparition`,

기본값: 페이드 인 (클래스 선택)

옵션:

- 없음

- 페이드 인
- 스케일 업
- 팝 인 (스프링)
- 펄스 인

- 왼쪽에서 오른쪽으로 슬라이드
- 오른쪽에서 왼쪽으로 슬라이드
- 위에서 아래로 슬라이드
- 아래에서 위로 슬라이드
- 왼쪽 위에서 슬라이드
- 오른쪽 위에서 슬라이드
- 왼쪽 아래에서 슬라이드
- 오른쪽 아래에서 슬라이드

- 오른쪽에서 왼쪽으로 회전
- 왼쪽에서 오른쪽으로 회전
- 아래에서 위로 회전
- 위에서 아래로 회전
- 가로 뒤집기 (X축)
- 세로 뒤집기 (Y축)

- 블러 인 (피사계 심도)
- 바운스 인
- 스윙 인

- 글라이드 인
- 글라이드 아웃
- 오라 글로우
- TV 효과 (레트로 CRT)
- 어패리션

### 모달 애니메이션 유형

대상 CSS 클래스:

`.flexcyon-modal-anims-fade-in, .flexcyon-modal-anims-scale-up,
.flexcyon-modal-anims-pop-in, .flexcyon-modal-anims-pulse-in`,

`.flexcyon-modal-anims-slide-ltr, .flexcyon-modal-anims-slide-rtl, 
.flexcyon-modal-anims-slide-tb, .flexcyon-modal-anims-slide-bt,
.flexcyon-modal-anims-slide-tl, .flexcyon-modal-anims-slide-tr,
.flexcyon-modal-anims-slide-bl, .flexcyon-modal-anims-slide-br`,

`.flexcyon-modal-anims-spin-rl, .flexcyon-modal-anims-spin-lr,
.flexcyon-modal-anims-spin-bt, .flexcyon-modal-anims-spin-tb,
.flexcyon-modal-anims-flip-x, .flexcyon-modal-anims-flip-y`,

`.flexcyon-modal-anims-blur-in, .flexcyon-modal-anims-bounce-in,
.flexcyon-modal-anims-swing-in`,

`.flexcyon-modal-anims-glide-in, .flexcyon-modal-anims-aura-glow,
.flexcyon-modal-anims-tv-effect, .flexcyon-modal-anims-apparition`,

기본값: 펄스 인 (클래스 선택)

옵션:

- 없음

- 페이드 인
- 스케일 업
- 팝 인 (스프링)
- 펄스 인

- 왼쪽에서 오른쪽으로 슬라이드
- 오른쪽에서 왼쪽으로 슬라이드
- 위에서 아래로 슬라이드
- 아래에서 위로 슬라이드
- 왼쪽 위에서 슬라이드
- 오른쪽 위에서 슬라이드
- 왼쪽 아래에서 슬라이드
- 오른쪽 아래에서 슬라이드

- 오른쪽에서 왼쪽으로 회전
- 왼쪽에서 오른쪽으로 회전
- 아래에서 위로 회전
- 위에서 아래로 회전
- 가로 뒤집기 (X축)
- 세로 뒤집기 (Y축)

- 블러 인 (피사계 심도)
- 바운스 인
- 스윙 인

- 글라이드 인
- 글라이드 아웃
- 오라 글로우
- TV 효과 (레트로 CRT)
- 어패리션

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