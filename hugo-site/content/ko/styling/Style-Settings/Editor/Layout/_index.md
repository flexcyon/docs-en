---
title: 레이아웃
---

워크스페이스 레이아웃 설정하기

## 내비게이션

```md
Style Settings
|-- ...
|-- Flexcyon Style Settings
|   |-- Editor
|   |   |-- ...
|   |   |-- Layout
|   |   |-- ...
|   |-- ...
|-- ...
```

## 환경 설정 옵션

### 워크스페이스 레이아웃 선택

대상 CSS 클래스: `.flexcyon-workspace-card-layout,
.flexcyon-workspace-angled-layout, .flexcyon-workspace-pl10k-layout`

기본값: 없음(클래스 선택)

옵션:

- 카드 레이아웃
- Angled 레이아웃
- Powerlevel10k 레이아웃

> 워크스페이스 레이아웃 변경 시 앱 새로고침 또는 재시작이 필요할 수 있습니다.

### 카드 레이아웃용 TUI 부가 기능 활성화

대상 CSS 변수: `var(--flexcyon-workspace-cards-tui-ext)`

기본값: true(클래스 토글)