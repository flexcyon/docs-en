---
title: 아이콘
---

## 내비게이션

```md
Style Settings
|-- flexcyon://Editor
|   |-- Icons
```

## 환경 설정 옵션

### 아이콘 1의 확대 비율

대상 CSS 변수: `var(--upsize)`

기본값: 103%

<span style="scale: 103%">샘플 확대 비율 1</span>

### 아이콘 2의 확대 비율

대상 CSS 변수: `var(--expand)`

기본값: 110%

<span style="scale: 110%">샘플 확대 비율 2</span>

### 설정에서 스마일리 토글 아이콘

대상 CSS 클래스: `.flexcyon-settings-smiley-icons-enabled`

기본값: false (클래스 토글)

### ASCII 아이콘 세트 로드

일부 아이콘을 ASCII 아이콘으로 대체합니다. 스마일리 아이콘과 함께 사용할 때 가장 잘 어울립니다. 이 설정은 대상이 되는 특정 아이콘에 대해 Iconic 같은 커뮤니티 플러그인의 선언을 덮어씁니다. 아래 설정으로 이를 방지할 수 있습니다.

대상 CSS 클래스: `.flexcyon-ascii-icon-set`

기본값: false (클래스 토글)

### 커뮤니티 플러그인 아이콘이 우선하도록 보장

아이콘을 수정하는 커뮤니티 플러그인의 수정 사항이 이 테마보다 우선하도록 보장합니다. 해당 커뮤니티 플러그인이 활성화되어 있고 이 설정도 활성화되어 있으면 스마일리 아이콘과 ASCII 아이콘은 렌더링되지 않습니다. 이 설정은 현재 Iconic 플러그인에서만 동작합니다. 아이콘 관련 플러그인을 모두 지원하면 성능에 지나치게 악영향을 주기 때문입니다.

대상 CSS 클래스: `.flexcyon-ensure-plugin-icon`

기본값: true (클래스 토글)

### 설정에서 색상 아이콘

제거, 옵션, 단축키 등 설정의 버튼에 색상 아이콘을 표시합니다. 현재 구현은 이전 Obsidian 버전에서는 동작하지 않을 수 있습니다.

대상 CSS 변수: `var(--flexcyon-settings-coloured-icons)`

기본값: false (클래스 토글)
