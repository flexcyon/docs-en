---
title: 워크스페이스 구성 요소
---

가독성 라인 길이를 활성화할 때의 파일 줄 너비와 View Header, 타이틀바, 상태바 등
그 밖의 워크스페이스 구성 요소를 정의합니다.

허용되는 형식: x.y, rem

## 내비게이션

```md
Style Settings
|-- flexcyon://Editor
|   |-- Workspace Components
```

## 환경 설정 옵션

### 파일 줄 너비

대상 CSS 변수: `var(--file-line-width)`

기본값: 50 (rem)

### 에디터 위쪽 여백

대상 CSS 변수: `var(--flexcyon-editor-margin-top)`

기본값: 18 (px)

### 상단 액션 정렬

상단 액션(새 노트, 새 폴더 등을 만들 수 있는 아이콘들)의 정렬입니다.

대상 CSS 변수: `var(--flexcyon-top-actions-alignment)`

기본값: 가운데 (변수 선택)

옵션:
- 왼쪽
- 가운데
- 오른쪽
