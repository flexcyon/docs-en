---
title: 표
---

읽기 모드에서 표 테두리의 색상과 표의 너비를 정의합니다.

허용되는 형식: HEX, %, x.y

## 내비게이션

```md
Style Settings
|-- ...
|-- Flexcyon Style Settings
|   |-- Editor
|   |   |-- ...
|   |   |-- Table
|   |   |-- ...
|   |-- ...
|-- ...
```

## 환경 설정 옵션

### 표 테두리 색상

대상 CSS 변수: `var(--table-border-color)`

기본값:
<span class="col-sqr" style="background-color: #6f768566"></span> #6f768566

### 읽기 모드에서 표의 너비

대상 CSS 변수: `var(--flexcyon-table-reading-mode-width)`

기본값: 100%

### 테이블 헤더 글꼴 크기

대상 CSS 변수: `var(--table-header-size)`

기본값: 큰 글꼴 (UI 글꼴 크기)

옵션:

- 더 작은 글꼴 (UI 글꼴 크기)
- 작은 글꼴 (UI 글꼴 크기)
- 중간 글꼴 (UI 글꼴 크기)
- 큰 글꼴 (UI 글꼴 크기)

<span style="font-size: large;">샘플 테이블 헤더</span>

### 테이블 헤더 세로 패딩
대상 CSS 변수: `var(--flexcyon-th-verti-padding)`

기본값: 5 (px)

### 테이블 헤더 가로 패딩
대상 CSS 변수: `var(--flexcyon-th-horiz-padding)`

기본값: 10 (px)

### 테이블 헤더 Live Preview 스케일링

읽기 모드와 비교했을 때 Live Preview 테이블 헤더 패딩을 스케일링하는 비율입니다.

대상 CSS 변수: `var(--flexcyon-th-live-pad-scale)`

기본값: 0.2

### 표 셀 글꼴 크기

대상 CSS 변수: `var(--table-text-size)`

기본값: 중간 글꼴 (UI 글꼴 크기)

옵션:

- 더 작은 글꼴 (UI 글꼴 크기)
- 작은 글꼴 (UI 글꼴 크기)
- 중간 글꼴 (UI 글꼴 크기)
- 큰 글꼴 (UI 글꼴 크기)

<span style="font-size: large;">샘플 표 셀</span>

### 표 셀 세로 패딩
대상 CSS 변수: `var(--flexcyon-td-verti-padding)`

기본값: 5 (px)

### 표 셀 가로 패딩
대상 CSS 변수: `var(--flexcyon-td-horiz-padding)`

기본값: 10 (px)

### 표 셀 Live Preview 스케일링

읽기 모드와 비교했을 때 Live Preview 표 셀 패딩을 스케일링하는 비율입니다.

대상 CSS 변수: `var(--flexcyon-td-live-pad-scale)`

기본값: 0.2

> 구체적으로는 지정된 값과 비교한 패딩의 스케일링