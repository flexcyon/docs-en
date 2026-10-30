---
title: 줄
---

줄 번호, 상대적 줄 번호 및 활성 줄 설정하기

허용되는 형식: HEX, %, x.y

## 내비게이션

```md
Style Settings
|-- flexcyon://Editor
|   |-- Lines
```

## 환경 설정 옵션

### 활성 줄 강조

대상 CSS 변수: `var(--flexcyon-highlight-active-line)`

기본값: false (클래스 토글)

### 활성 줄 글로우

대상 CSS 변수: `var(--flexcyon-glow-active-line)`

기본값: false (클래스 토글)

### 활성 줄 글로우 x 오프셋

대상 CSS 변수: `var(--flexcyon-glow-active-offset-x)`

기본값: 1 (px)

### 활성 줄 글로우 y 오프셋

대상 CSS 변수: `var(--flexcyon-glow-active-offset-y)`

기본값: 1 (px)

### 활성 줄 글로우 흐림 강도

대상 CSS 변수: `var(--flexcyon-glow-active-blur-radius)`

기본값: 2 (px)

### 활성 텍스트 글로우 색상

대상 CSS 변수: `var(--flexcyon-glow-active-color)`

기본값: 일반 텍스트 (변수 선택)

옵션:

* 시안
* 파랑
* 보라
* 분홍
* 빨강
* 오렌지
* 노랑
* 초록
* Accent
* 일반 텍스트

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

기본값: none (클래스 토글)

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