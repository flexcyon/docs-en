---
title: 줄 번호
---

줄 번호 및 상대적 줄 번호 설정하기

허용되는 형식: HEX, %, x.y

## 내비게이션

```md
Style Settings
|-- ...
|-- Flexcyon Style Settings
|   |-- Editor
|   |   |-- ...
|   |   |-- Line Numbers
|   |   |-- ...
|   |-- ...
|-- ...
```

## 환경 설정 옵션

### 활성 줄 강조

대상 CSS 변수: `var(--flexcyon-highlight-active-line)`

기본값: false (클래스 토글)

### 상대적 줄 번호 활성화

대상 CSS 변수: `var(--flexcyon-enable-rel-nums)`

기본값: false (클래스 토글)

### 상대적 줄 번호와 일반 줄 번호를 다른 줄에 표시

대상 CSS 변수: `var(--flexcyon-no-num-with-relative)`

기본값: false

### 상대적 줄 번호만 표시

대상 CSS 변수: `var(--flexcyon-relative-num-only)`

기본값: false

### 상대적 줄 번호 스타일 구성

대상 CSS 변수: `var(--flexcyon-roman-rel-nums)`,
`var(--flexcyon-roman-greek-nums), var(--flexcyon-roman-chinese-nums)`

기본값: 없음 (클래스 토글)

옵션:

- 로마자
- 그리스어
- 중국어

### 활성 줄 번호를 문자열로 교체
자신만의 문자열로 활성 줄 번호를 커스터마이징하세요. 기본값은 "->"입니다.

대상 CSS 변수: `var(--flexcyon-repl-active-line-num-str)`

기본값: false (클래스 토글)

### 교체된 활성 줄 번호 문자열 값

대상 CSS 변수: `var(--flexcyon-repl-active-line-str)`

기본값: "->"

### 교체된 활성 줄 번호 문자열 자간

대상 CSS 변수: `var(--flexcyon-repl-active-str-space)`

기본값: 0 (px)