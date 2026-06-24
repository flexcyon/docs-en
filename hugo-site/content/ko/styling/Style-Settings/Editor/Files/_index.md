---
title: 파일
---

파일 트리와 폴더 스타일 설정하기

## 내비게이션

```md
Style Settings
|-- ...
|-- Flexcyon Style Settings
|   |-- Editor
|   |   |-- ...
|   |   |-- Files
|   |   |-- ...
|   |-- ...
|-- ...
```

## 환경 설정 옵션

### 파일 탐색기에서 희미하게 표시된 파일 확장자 활성화

대상 CSS 클래스: `var(--flexcyon-file-exp-dimmed-file-exts-enabled)`

기본값: true (클래스 토글)

### 희미하게 표시된 파일 확장자 글꼴 크기

대상 CSS 변수: `var(--flexcyon-exp-dimmed-nav-size)`

기본값: 13.3623 (px)

### 활성 파일 인디케이터 활성화

대상 CSS 클래스: `var(--flexcyon-enable-active-file-indicator)`

기본값: false (클래스 토글)

### 활성 파일 인디케이터 값

대상 CSS 변수: `var(--flexcyon-active-indicator)`

기본값: ">> "

### 세로 내비게이션 활성화

대상 CSS 변수: `var(--flexcyon-vertical-nav)`

기본값: false (클래스 토글)

### 폴더 스타일 선택

대상 CSS 클래스: `.flexcyon-rainbow-folders, .flexcyon-alt-folder-style, .flexcyon-md-file-tree-style`

기본값: 없음 (클래스 선택)

옵션:

- 레인보우 폴더
- 대체 폴더 스타일
- 마크다운 파일 트리 스타일

### 레인보우 폴더의 텍스트 대신 색상 배경 사용

대상 CSS 클래스: `var(--flexcyon-is-bg-rainbow)`

기본값: false

### 미니멀리스트 트리 활성화

대상 CSS 변수: `var(--flexcyon-minimalist-tree)`

기본값: false (클래스 토글)

### 세로 트리 항목 패딩

대상 CSS 클래스: `var(--flexcyon-tree-item-verti-padding)`

기본값: 2 (px)

### 가로 트리 항목 패딩

대상 CSS 클래스: `var(--flexcyon-tree-item-horiz-padding)`

기본값: 10 (px)

### 긴 파일 이름 줄바꿈

긴 파일 이름의 끝부분을 생략하는 대신 새 줄에 맞춰 표시합니다.

대상 CSS 변수: `var(--flexcyon-wrap-long-filenames)`

기본값: true (클래스 토글)