---
title: 커서
---

커서 설정하기

## 내비게이션

```md
Style Settings
|-- ...
|-- Flexcyon Style Settings
| |-- Editor
| | |-- ...
| | |-- Cursor
| |-- ...
|-- ...
```

## 환경 설정 옵션

### 기본 커서 유형

대상 CSS 변수: `var(--flexcyon-cursor-type)`

앱에서 지정되지 않은 경우의 커서 유형을 설정합니다.
> VS Code 포크가 아닙니다

기본값: auto (변수 선택)

옵션: 전체 옵션 목록은 [MDN 커서 스타일링 문서](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/cursor)를 참조하세요.

### 부드러운 커서 활성화

대상 CSS 클래스: `var(--flexcyon-enable-smooth-cursor)`

기본값: true

> 실제로는 캐럿입니다, 이미 지적된 바와 같습니다.

### 부드러운 커서 전환 지속시간

대상 CSS 클래스: `var(--flexcyon-cursor-duration)`

기본값: 42.5 (ms)

### 부드러운 커서 타이밍 함수

대상 CSS 클래스: `var(--flexcyon-cursor-timing-fn)`

기본값: ease-in

### 부드러운 커서 최소 폭

대상 CSS 클래스: `var(--flexcyon-cursor-min-width)`

기본값: unset