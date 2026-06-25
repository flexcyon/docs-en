---
title: 플러그인
---

공식적으로 지원되는 플러그인의 설정에 대한 내용

허용되는 형식: HEX, rem, x.y, %

## 내비게이션

```md
Style Settings
|-- ...
|-- Flexcyon Style Settings
|   |-- ...
|   |-- Plugins
|   |-- ...
```

## 환경 설정 옵션

### 대체 파일 트리

#### 폴더 글꼴 크기

대상 CSS 변수: `var(--oz-fta-folder-font-size)`

기본값: 0.925 (rem)

<span style="font-size: 0.925rem">샘플 대체 파일 트리 폴더 글꼴 크기</span>

#### 폴더 글꼴 색상

대상 CSS 변수: `var(--oz-fta-folder-pane-file-name-color)`

기본값(라이트 모드):
<span class="col-sqr" style="background-color: #080808"></span> #080808

기본값(다크 모드):
<span class="col-sqr" style="background-color: #d3d5d3"></span> #d3d5d3

#### 활성 폴더 색상

대상 CSS 변수: `var(--oz-fta-all-panes-active-text-color)`

기본값(라이트 모드):
<span class="col-sqr" style="background-color: #080808"></span> #080808

기본값(다크 모드):
<span class="col-sqr" style="background-color: #d3d5d3"></span> #d3d5d3

#### 파일 글꼴 크기

대상 CSS 변수: `var(--oz-fta-file-font-size)`

기본값: 0.9 (rem)

<span style="font-size: 0.9rem">샘플 대체 파일 트리 파일 글꼴 크기</span>

#### 파일 글꼴 색상

대상 CSS 변수: `var(--oz-fta-file-pane-file-name-color)`

기본값:
<span class="col-sqr" style="background-color: #6f768599"></span> #6f768599

#### 폴더 아이콘 비활성화

대상 CSS 변수: `var(--flexcyon-oz-folder-icons-disabled)`

기본값: false (클래스 토글)

#### 파일 트리 헤더 비활성화

대상 CSS 변수: `var(--flexcyon-oz-file-tree-header-disabled)`

기본값: false (클래스 토글)

#### 대체 폴더 개수 활성화

대상 CSS 변수: `var(--flexcyon-oz-alternate-folder-count)`

기본값: false (클래스 토글)

#### 파일 트리에서 희미한 파일 확장자 활성화

대상 CSS 변수: `var(--flexcyon-oz-dimmed-file-exts-enabled)`

기본값: true (클래스 토글)

___

### Full Calendar

허용되는 형식: x.y, %

#### 희미한 Full Calendar 항목의 불투명도

대상 CSS 변수: `var(--flexcyon-fc-dimmed-items-opacity)`

기본값: 0.89

<span style="opacity: 0.89">샘플 희미한 Full Calendar 항목의 불투명도</span>

___

### Dataview

허용되는 형식: px

#### Dataview 오류 메시지의 가로 패딩

대상 CSS 변수: `var(--flexcyon-dataview-horizontal-padding)`

기본값: 8 (px)

___

### 캔버스

핵심 캔버스 플러그인의 스타일을 정의합니다.

허용되는 형식: px, RGB

#### 비활성 캔버스 노드의 흐림 효과

대상 CSS 변수: `var(--flexcyon-canvas-blur-inactive-nodes)`

기본값: false (클래스 토글)

#### 비활성 노드의 흐림 강도

이전 설정과 함께 비활성 캔버스 노드와 모든 화살표/가장자리의 흐림 강도를 설정합니다.

대상 CSS 변수: `var(--flexcyon-canvas-blur-intensity)`

기본값: 1 (px)

#### 캔버스 카드 메뉴 정렬

캔버스 카드 메뉴의 정렬을 구성합니다.

대상 CSS 클래스: `.flexcyon-canvas-menu-bottom-left,`
`
.flexcyon-canvas-menu-bottom-right, .flexcyon-canvas-menu-top-center,
.flexcyon-canvas-menu-top-left, .flexcyon-canvas-menu-top-right,
.flexcyon-canvas-menu-lcenter-center, .flexcyon-canvas-menu-lcenter-top,
.flexcyon-canvas-menu-lcenter-bottom, .flexcyon-canvas-menu-rcenter-center,
.flexcyon-canvas-menu-rcenter-top, .flexcyon-canvas-menu-rcenter-bottom, .flexcyon-canvas-menu-recenter-align
`

기본값: 없음 (클래스 선택)

옵션:

- 하단 왼쪽

- 하단 오른쪽

- 상단 중앙

- 상단 왼쪽

- 상단 오른쪽

- 왼쪽 정렬 중앙

- 왼쪽 정렬 상단

- 왼쪽 정렬 하단

- 오른쪽 정렬 중앙

- 오른쪽 정렬 상단

- 오른쪽 정렬 하단

- 오른쪽 정렬 중앙 정렬

___

### Various Complements
#### 세로 제안 패딩
대상 CSS 변수: `var(--flexcyon-var-comps-sugg-vert-padding)`

기본값: 7 (px)

#### 가로 제안 패딩
대상 CSS 변수: `var(--flexcyon-var-comps-sugg-horiz-padding)`

기본값: 12 (px)

#### 컴팩트 제안 모드
기본값을 덮어씁니다. 4px 8px 패딩을 사용합니다.

대상 CSS 변수: `var(--flexcyon-var-comps-compact-mode)`

기본값: false (클래스 토글)

___

### Omnisearch

#### Omnisearch 아이콘 비활성화

대상 CSS 클래스: `var(--flexcyon-omnisearch-no-icons)`

기본값: false (클래스 토글)

#### Omnisearch 본문 왼쪽 여백

대상 CSS 클래스: `var(--flexcyon-omnisearch-body-margin-left-margin-left)`

기본값: 1.45 (rem)

___

### Bases

#### Bases 뷰 세로 패딩

대상 CSS 변수: `var(--flexcyon-bases-padding-horiz)`

기본값: 16 (px)

#### Bases 뷰 가로 패딩

대상 CSS 변수: `var(--flexcyon-bases-padding-horiz)`

기본값: 16 (px)

#### Bases 임베드 패딩

대상 CSS 변수: `var(--bases-embed-padding)`

기본값: 4 (px)

___

#### Bases 카드 뷰

##### Bases 카드 라벨 불투명도

대상 CSS 변수: `var(--flexcyon-bases-cards-label-opacity)`

기본값: 0.85

##### 카드 뷰 항목 이미지가 발견되지 않았을 때 기본 문자열

대상 CSS 변수: `var(--bases-no-img-str)`

기본값: "이 파일에 대한 이미지 경로를 찾을 수 없습니다"

##### Bases 카드 모서리 둥글기

대상 CSS 변수: `var(--bases-border-r)`

기본값: 16 (px)

##### Bases 카드 그룹 패딩

대상 CSS 변수: `var(--bases-cards-group-padding)`

기본값: 16 (px)

##### Bases 카드 상단 패딩

대상 CSS 변수: `var(--flexcyon-bases-card-padding-top)`

기본값: 8 (px)

##### Bases 카드 오른쪽 패딩

대상 CSS 변수: `var(--flexcyon-bases-card-padding-right)`

기본값: 0 (px)

##### Bases 카드 하단 패딩

대상 CSS 변수: `var(--flexcyon-bases-card-padding-bottom)`

기본값: 0 (px)

##### Bases 카드 왼쪽 패딩

대상 CSS 변수: `var(--flexcyon-bases-card-padding-left)`

기본값: 2 (px)

##### Bases 카드 뷰 플렉스 성장률

이는 카드 뷰가 탭 크기에 따라 얼마나 길게 스케일링되는지를 나타내는 계수입니다.

대상 CSS 변수: `var(--flexcyon-bases-card-flex-grow)`

기본값: 0.55

___

#### Bases 테이블 뷰

##### Bases 테이블 셀 왼쪽 패딩

대상 CSS 변수: `var(--flexcyon-bases-td-padding-l)`

기본값: 2 (px)

##### Bases 테이블 셀 내용 정렬

대상 CSS 변수: `var(--flexcyon-bases-table-content-alignment)`

기본값: 왼쪽 (변수 선택)

옵션:

- 왼쪽
- 중앙
- 오른쪽