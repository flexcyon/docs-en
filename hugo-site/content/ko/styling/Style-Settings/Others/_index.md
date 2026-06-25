---
title: 기타
---

vim 모드 텍스트 구성, 새 탭 모양(ASCII 아트), 사이드독 아이콘,
툴팁 모서리 둥글기

허용되는 형식: px

## 내비게이션

```md
Style Settings
|-- ...
|-- Flexcyon Style Settings
|   |-- ...
|   |-- Others
```

## 환경 설정 옵션

### Vim 모드 텍스트

#### Vim 모드 텍스트 활성화

대상 CSS 변수: `var(--flexcyon-vim-mode-text-enable)`

기본값: true (클래스 토글)

#### Vim 모드 텍스트 왼쪽 위치 지정

대상 CSS 변수: `var(--flexcyon-vim-mode-left-positioning)`

기본값: 6 (px)

#### Vim 모드 텍스트 아래쪽 위치 지정

대상 CSS 변수: `var(--flexcyon-vim-mode-left-positioning)`

기본값: -4 (px)

#### 삽입 모드 텍스트

대상 CSS 변수: `var(--flexcyon-vim-insert-text)`

기본값: "INSERT"

#### 일반 모드 텍스트

대상 CSS 변수: `var(--flexcyon-vim-normal-text)`

기본값: "NORMAL"

#### 명령 모드 텍스트

대상 CSS 변수: `var(--flexcyon-vim-command-text)`

기본값: "COMMAND"

___

### 새 탭 모양

새로운 빈 탭의 모양을 사용자 정의하세요.

허용되는 형식: px

#### 빈 상태 제목 앞에 추가

대상 CSS 클래스: `.flexcyon-ascii-enable, .flexcyon-quote-enable`
> 이 변경사항은 앱 새로고침/재시작 후 적용됩니다.

기본값: 없음 (클래스 선택)

옵션:

- ASCII Art
- 인용문

#### 새 탭 글꼴 그룹

대상 CSS 변수: `var(--flexcyon-new-tab-font-group)`

> ASCII 아트가 잘 보이려면 다음과 같은 고정폭 글꼴을 사용하는 것이 좋습니다:
> Source Code Pro

기본값: 없음 (클래스 선택)

옵션:

- 고정폭 글꼴
- 인터페이스 글꼴
- 텍스트

#### 빈 상태 제목 앞에 추가할 배경

대상 CSS 변수: `var(--flexcyon-new-tab-bg-wrapper)`

기본값: `linear-gradient(to right, var(--text-accent), var(--color-blue), var(--color-cyan))`

#### 인용문

대상 CSS 변수: `var(--flexcyon-quote-val)`

기본값: "This is a placeholder quote\ain the Flexcyon Theme."

#### 인용문 출처 접두사

대상 CSS 변수: `var(--flexcyon-quote-credit-prefix)`

기본값: "-"

#### 인용문 출처

대상 CSS 변수: `var(--flexcyon-quote-credit)`

기본값: "bladeacer"

#### 인용문 글꼴 크기

대상 CSS 변수: `var(--flexcyon-quote-font-size)`

기본값: 24 (px)

> 줄바꿈은 `\a`로, `\`는 `\\`로 에스케이프됩니다.

#### ASCII Art

대상 CSS 변수: `var(--flexcyon-ascii-art)`

기본값:

```md
" \a\
    _______________                                       \a\
    ___  ____/__  /________  ____________  ______________ \a\
    __  /_   __  /_  _ \\_  |/_/  ___/_  / / /  __ \\_  __ \\ \a\
    _  __/   _  / /  __/_>  < / /__ _  /_/ // /_/ /  / / / \a\
    /_/      /_/  \\___//_/|_| \\___/ _\\__, / \\____//_/ /_/ \a\
                                    /____/                \a\a\a "
```

> CSS에서 렌더링하려면 ASCII 아트 문자열을 에스케이프해야 하며, 줄바꿈은 `\a`로, `\`는 `\\`로 에스케이프됩니다.

개별 ASCII 아트를 관리하고 구성하려면 CSS 스크립트를 사용하는 것을 강력히 권장합니다.

예제는 [여기](https://github.com/bladeacer/obsi-snip-coll/blob/main/snippets/flexcyon/new-tab/placeholder-ascii)에서 확인할 수 있습니다.

#### ASCII 아트 글꼴 크기 제한

대상 CSS 변수: `var(--flexcyon-ascii-max-font-size)`

기본값: 14 (px)

#### ASCII 아트 행 높이

대상 CSS 변수: `var(--flexcyon-ascii-line-height)`
> 인용문의 행 높이도 변경됩니다.

기본값: 1

#### ASCII 아트 스케일링 팩터

대상 CSS 변수: `var(--flexcyon-ascii-scaling-factor)`

기본값: 1

#### ASCII 아트 텍스트 정렬

대상 CSS 변수: `var(--flexcyon-ascii-alignment)`

기본값: 왼쪽

옵션:

- 왼쪽
- 가운데
- 오른쪽

#### 빈 상태 제목 비활성화

대상 CSS 변수: `var(--flexcyon-empty-state-title-disable)`

기본값: true (클래스 토글)

#### 빈 상태 액션 비활성화

대상 CSS 변수: `var(--flexcyon-empty-state-actions-disable)`

기본값: true (클래스 토글)

___

### 사이드 도크

사이드 도크 아이콘 설정하기

#### 사이드 도크 아이콘 효과 활성화
> 호버 시 무지개 효과

대상 CSS 변수: `var(--flexcyon-sidedock-icon-effects)`

기본값: true (클래스 토글)

### 사이드 도크 리본 너비

대상 CSS 변수: `var(--flexcyon-sidedock-ribbon-width)`

기본값: 48 (px)

### 워크스페이스 리본을 상단에 배치

대상 CSS 변수: `var(--flexcyon-ribbon-top)`

기본값: false (클래스 토글)

### 볼트 스위처를 상단에 배치

대상 CSS 변수: `var(--flexcyon-vault-switch-top)`

기본값: false (클래스 토글)

### 볼트 스위처와 액션의 순서 반전

대상 CSS 변수: `var(--flexcyon-vault-reverse)`

기본값: false (클래스 토글)
___

### 툴팁 모서리 둥글기

툴팁 모서리 둥글기 설정하기

#### Small 래디우스

대상 CSS 변수: `var(--radius-s)`

기본값: 2 (px)

#### Medium 래디우스

대상 CSS 변수: `var(--radius-m)`

기본값: 4 (px)

#### Large 래디우스

대상 CSS 변수: `var(--radius-l)`

기본값: 6 (px)

#### Extra large 래디우스

대상 CSS 변수: `var(--radius-xl)`

기본값: 8 (px)

___

### 사이드바 배경

왼쪽 및 오른쪽 사이드바의 배경 이미지 설정하기

허용되는 형식: px, %

#### 사이드바 배경 선택

대상 CSS 클래스: `.flexcyon-sidebar-bg-dots, .flexcyon-sidebar-bg-grid, flexcyon-sidebar-bg-rhombus`
> 아래의 배경 이미지 선언을 덮어쓰며, 왼쪽과 오른쪽 사이드바 모두에 적용됩니다.

기본값: 없음 (클래스 선택)

옵션:

- 격자
- 점선
- 마름모

#### 왼쪽 사이드바 배경 이미지 URL

대상 CSS 변수: `var(--flexcyon-bg-image-sidebar-left-url)`

기본값: url("")
> URL이 작동하려면 이중 따옴표 사이에 URL을 추가하세요. 예: 
`url("https://fake_domain/not_a_real_image.png")`

#### 오른쪽 사이드바 배경 이미지 URL

대상 CSS 변수: `var(--flexcyon-bg-image-sidebar-right-url)`

기본값: url("")
> URL이 작동하려면 이중 따옴표 사이에 URL을 추가하세요. 예: 
`url("https://fake_domain/not_a_real_image.png")`

#### 사이드바 배경 이미지 혼합 모드

대상 CSS 변수: `var(--flexcyon-bg-image-blend-mode)`

기본값: darken

#### 사이드바 배경 이미지 반복

대상 CSS 변수: `var(--flexcyon-bg-image-repeat)`

기본값: no-repeat

#### 사이드바 배경 이미지 흐림 효과

대상 CSS 변수: `var(--flexcyon-bg-image-blur)`

기본값: 0 (px)

#### 사이드바 배경 이미지 밝기

대상 CSS 변수: `var(--flexcyon-bg-image-brightness)`

기본값: unset
> 55%와 같은 백분율 값을 받습니다.

#### 사이드바 배경 이미지 크기

대상 CSS 변수: `var(--flexcyon-bg-image-size)`

기본값: contain

#### 사이드바 배경 이미지 위치

대상 CSS 변수: `var(--flexcyon-bg-image-position)`

기본값: center

___

### 모달 배경

설정 메뉴, 프롬프트 등의 배경 이미지 설정하기

허용되는 형식: px, %

#### 모달 배경 이미지 URL

대상 CSS 변수: `var(--flexcyon-modal-bg-url)`

기본값: url("")
> URL이 작동하려면 이중 따옴표 사이에 URL을 추가하세요. 예: 
`url("https://fake_domain/not_a_real_image.png")`

#### 모달 배경 이미지 혼합 모드

대상 CSS 변수: `var(--flexcyon-modal-image-blend-mode)`

기본값: lighten

#### 모달 배경 이미지 반복

대상 CSS 변수: `var(--flexcyon-modal-image-repeat)`

기본값: no-repeat

#### 모달 배경 이미지 흐림 효과

대상 CSS 변수: `var(--flexcyon-modal-image-blur)`

기본값: 0 (px)

#### 모달 배경 이미지 밝기

대상 CSS 변수: `var(--flexcyon-bg-modal-brightness)`

기본값: unset
> 55%와 같은 백분율 값을 받습니다.

#### 모달 배경 이미지 크기

대상 CSS 변수: `var(--flexcyon-modal-image-size)`

기본값: cover

#### 모달 배경 이미지 위치

대상 CSS 변수: `var(--flexcyon-modal-image-position)`

기본값: center

#### 모달 배경 어두움 강도

대상 CSS 변수: `var(--flexcyon-modal-dark-intensity)`

기본값: 1