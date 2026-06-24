---
title: 코드 블록
---

테마의 코드 블록 설정하기

허용되는 형식: px

## 내비게이션

```md
Style Settings
|-- ...
|-- Flexcyon Style Settings
|   |-- Editor
|   |   |-- ...
|   |   |-- Code Blocks
|   |   |-- ...
|   |-- ...
|-- ...
```

## 환경 설정 옵션

### Flexcyon 구문 강조 모드

대상 CSS 클래스: `.flexcyon-syntax-catppuccin,
.flexcyon-syntax-lego, .flexcyon-syntax-monochrome`

기본값: 없음(클래스 선택)
옵션:

- Catppuccin
- Lego
- Monochrome

### 코드 블록 파일 확장자에 대하여
코드 블록 파일 확장자를 커스터마이징하며, 이는 Live Preview 모드에서만 나타납니다.

### 코드 블록 파일 확장자를 소문자로 변경하기

대상 CSS 클래스: `.flexcyon-codeblock-fmt-ext`

기본값: false(클래스 토글)

### 코드 블록 파일 확장자 앞에 접두사 추가하기

대상 CSS 클래스: `.flexcyon-codeblock-prefix-ext`

기본값: false(클래스 토글)

### 코드 블록 확장자 앞에 접두사 커스터마이징하기

대상 CSS 변수: `var(--flexcyon-codeblock-ext-prefix)`

기본값: “.”

### 코드 블록 파일 확장자 글꼴 굵기

대상 CSS 변수: `var(--flexcyon-code-file-ext-font-w)`

기본값: 500