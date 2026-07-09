---
title: 모드
---

Flexcyon이 제공하는 몇 가지 독특한 모드를 설정해 보세요.

## 내비게이션

```md
Style Settings
|-- flexcyon://Modes
```

## 환경 설정 옵션

### 모드 선택
대상 CSS 클래스: `.flexcyon-flex-max-mode, .flexcyon-rtz-mode`

기본값: Flex Max Mode (클래스 선택)

옵션:

- none
- Flex Max Mode
- Return To Zero Mode

### Return to Zero 모드에 대하여

Shimmering Focus 테마에서 영감을 받은 극단적인 미니멀리즘입니다. 대부분의 UI 요소는
마우스를 가져다 대야만 표시됩니다.
> 모바일에서는 권장하지 않습니다.

### Flex Max 모드에 대하여

이 테마의 독창적인 커스터마이징을 강조하는 매우 고집스러운 설정으로, 기본적으로 작동하는
기능들을 제공합니다. 일부 옵션이 마음에 들지 않는다면 이 모드를 비활성화하고 직접 테마를
더 세밀하게 커스터마이징할 수 있습니다. 그러면 커스터마이징 측면에서 테마가 깨끗한 상태로
초기화됩니다.

또한 기본적으로 활성화된 다른 옵션들도 있으니, 마음에 들 수도 그렇지 않을 수도 있습니다.
이 모드가 사용자를 대신해 활성화하는 옵션 목록은 아래를 참고하세요.

이 모드는 커스터마이징을 어디서부터 시작해야 할지 모르는 사용자에게 추천합니다.
**테마를 광범위하게 커스터마이징하려는 분**이나 이 기본 설정이 마음에 들지 않는 분들은
**이 모드를 비활성화하는 것이 좋습니다**.

### Flex Max 모드 활성화 설정 옵션

Style Settings에서 비활성화되어 있어도 다음 설정을 활성화합니다.

* 스마일 아이콘

* 커뮤니티 플러그인 아이콘이 우선 적용되도록 설정

* 빈 상태 제목 앞에 ASCII 아트 추가

* 빈 상태 제목 비활성화

* 사용자 정의 가로선 문자열

* Powerlevel10k에서 영감받은 상태바 스타일

* 마우스 호버 시까지 숨김 상태바

* 현재 상태바 편집 모드를 아이콘 대신 텍스트로 표시

* Vim 모드 상태

* 색상 헤더

* 확장된 색상 팔레트

* ASCII 체크박스

* 클립 경로 체크박스

* 설정 내 색상 아이콘

* 커뮤니티 항목 효과

* 설정 내 스크롤바 표시 안 함

* 대체 파일 트리 플러그인용 파일 확장자 흐리게 표시

* 사이드 도크 아이콘 효과 활성화

* 코드 블록 파일 확장자 소문자 처리 (Live Preview)

* 코드 블록 파일 확장자에 접두사 추가 (Live Preview)

이 설정들은 일반적으로 활성화된 것처럼 구성할 수 있습니다.
테마에는 이 외에도 많은 설정 옵션이 있으며, 그중 일부는 부드러운 커서처럼 기본적으로
활성화되어 있습니다.

### Typewriter 모드

대상 CSS 클래스: `var(--flexcyon-typewriter-mode)`

소스 및 Live Preview 모드에서 활성 라인을 제외한 모든 라인의 불투명도를 낮춥니다.

기본값: false (클래스 토글)

### Typewriter 모드 불투명도

Typewriter 모드에서 비활성 라인의 흐린 불투명도

대상 CSS 변수: `var(--flexcyon-typewriter-mode-opacity)`

기본값: 0.55

### Reverse 모드

UI의 렌더링을 반전시킵니다.

대상 CSS 변수: `var(--flexcyon-reverse-mode)`

기본값: false (클래스 토글)

### Writing Mode 전역 활성화

> CSS 클래스와 유사하지만 전역적으로 적용됩니다.

대상 CSS 변수: `var(--flexcyon-editor-writing)`

기본값: false (클래스 토글)

### Writing Mode 들여쓰기

대상 CSS 변수: `var(--flexcyon-editor-writing-indentation)`

기본값: 16 (px)
