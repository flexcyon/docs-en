---
title: 버전 2.x.x
---

## 버전 2.0.x

### 2.0.1: 패치 1

#### 기능
- 비활성 스택 탭의 내용을 흐리게 표시하는 Style Settings 옵션을 새로 추가했습니다. 기본값은 true입니다.
- 비활성 탭 제목은 테마의 디자인 언어에 따라 흐리게 표시되며, 이는 일반 비활성 탭 제목이 흐려지는 방식과도 일관됩니다.

#### 변경
- 1.13 설정 UI의 스타일링을 개선했습니다.
- 설정 검색 컨테이너의 패딩을 조정했습니다.
- `var(--text-on-accent)`가 이제 `var(--color-base-00)`, 나아가 `var(--flexcyon-base-01)`에서 상속됩니다. 덕분에 강조 색상을 배경으로 쓰는 버튼의 대비가 좋아집니다(초록/보라 배경에는 흰 글자보다 검은 글자가 대비가 더 좋습니다).
- Spaced Repetition 플러그인 스타일링을 개선했습니다.

#### 수정
- `var(--slider-track-background)`가 투명 대신 `var(--color-base-25)`를 사용하도록 수정했습니다.
- 중복 코드를 제거하고, Highlightr 플러그인의 realistic 스타일이 테마 기본 하이라이트 테두리 반경에 덮어씌워지지 않도록 했습니다.
- Canvas 블록에서 스타일이 적용된 가로줄 렌더링을 개선했습니다.

### 2.0.0 메타모포시스

#### 기능
- 접근성이 개선되어, 이제 테마 색상의 대비·밝기·채도·색 온도를 조정할 수 있습니다.
- 테마의 색상이 이제 대부분 `oklch` 색 공간을 사용해 더 정확하게 렌더링됩니다.
	- 하드코딩되어 있던 일부 기본 선언을 `oklch` 색상으로 대체했습니다.
- Style Settings
	- "prevent accidental unpin"을 추가했습니다. 핀 아이콘 클릭으로 핀이 해제되는 것을 막습니다. 이 설정을 켠 상태에서 핀을 해제하려면 우클릭 메뉴 또는 Ctrl + W를 사용하세요.
	- "Editor Top Margin"을 추가했습니다.
	- "Callout Horizontal Margin"을 추가했습니다.
	- "Disable Vim Block Cursor Blink"를 추가했습니다.
	- "Hide Keychain item in Style Settings"를 추가했습니다.
	- 스크롤바 너비에 대한 Style Settings 옵션을 추가하고, 기존의 "do not show scrollbar in Settings"를 `flexcyon://Editor > Scrollbar`로 옮겼습니다.
- Banners Reloaded 플러그인 지원을 추가했습니다.
- 이제 테마 자체의 Flexcyon Multi-Column 구현(FMCi)이 생겼습니다.
	- 여기서 키워드란 콜아웃 유형과 콜아웃 메타데이터 양쪽 모두를 뜻합니다.
	- `>[!col]` 또는 `>[!multi-column]` 키워드를 지원합니다. 열 항목이 같은 열에 알맞게 들어가지 않을 때 줄바꿈하도록 `wrap` 콜아웃 키워드와 함께 사용할 수 있습니다. 예: `>[!col|wrap]`
	- `wide-0`부터 `wide-100`까지의 키워드를 지원합니다.
	- [자세한 내용은 문서를 참고하세요](../../styling/callout-metadata/fmci)
- 텍스트 내용에 대문자화를 적용하는 콜아웃 키워드 별칭 `capitalize`를 추가했습니다(이전에는 짧은 형태인 "caps"만 지원했습니다).
- Lemons Search 플러그인 지원을 추가했습니다.
	- 검색 결과 미리보기에 패딩을 추가했습니다.
	- 읽기 좋은 줄 길이를 사용합니다.
- `@Onev`의 노력 덕분에 이제 한국어 문서가 제공됩니다.

#### 변경
- Style Settings를 전면 개편했습니다. 기존 style settings를 flexcyon 2.0으로 옮기려면 [마이그레이션 도구](../2.0-migration)를 사용하세요.
	- `flexcyon://Editor` 아래의 불투명도 관련 Style settings를 모두 통합해 `flexcyon://Editor > Animations` 아래 전용 섹션으로 옮겼습니다.
	- Style Settings 마이그레이터 스크립트를 작성했습니다. 접근성 관련 style settings의 ID가 예를 들어 `flexcyon`에서 `flexcyon-a11y`로 바뀌었습니다.
	- 다수의 style setting 옵션 이름을 목적에 더 잘 맞게 변경했습니다.
	- "Do not show scrollbar in settings"가 이제 기본적으로 활성화되며, Flex Max Mode에서 활성화되도록 설정되지 않습니다.
	- 사용하지 않던 base grey tab, base grey token, base grey scroll, base grey scroll hover 변수를 제거했습니다.
	- "Relative and normal line numbers on different lines"의 기본값이 이제 true입니다.
	- Pl10k 작업 공간 레이아웃이 더 이상 Flex Max로 설정되지 않으며, "Select Workspace Layout"의 기본값이 이제 Pl10k 작업 공간 레이아웃입니다.
	- dimmed file extensions와 wrap long filenames의 기본값을 true로 바꾸고, 더 이상 Flex Max로 설정되지 않습니다.

- ASCII 아이콘을 개선했습니다. 기존 UI를 보완하는 아이콘 세트입니다. 영감을 준 OMG의 Floodlight에게 감사드립니다.
- 글꼴 크기, 줄 높이 등에 스케일 체계를 적용했습니다. 테마가 더 일관되고 짜임새 있게 보일 것입니다.
- ASCII 및 Clip Path 체크박스가 가능한 한(또는 필요하다고 판단되는 경우) 대체 체크박스 참조 세트에 더 잘 부합하도록 했습니다.
	- ASCII 체크박스가 이제 기본적으로 활성화되고, clip path 체크박스는 기본적으로 비활성화됩니다.
	- 호환성 향상을 위해 일부 아이콘 정의를 다시 매핑했습니다. 체크박스가 제대로 렌더링되지 않는다면 업데이트된 아이콘 세트를 참고하세요.
	- ASCII/Clip Path 체크박스는 대소문자를 구분한다는 점에 유의하세요.
	- 새 아이콘이 몇 가지 추가되었습니다.
	- 큰따옴표와 작은따옴표 ASCII 체크박스는 더 이상 유니코드를 사용하지 않습니다. 렌더링된 따옴표에 약간의 "필기체" 느낌이 있는지는 글꼴 패밀리에 따라 달라집니다.
- 라이트 및 다크 테마 색상을 개선해 대비와 가독성을 높였습니다.
- 이제 콜아웃 유형 대신 콜아웃 메타데이터에 Obsidian 기본 콜아웃 유형을 지정할 수 있습니다. 예를 들어 `>[!tip|a]`와 `>[!a|tip]`은 동일하게 보입니다.
	- Question 콜아웃이 이제 오렌지 대신 초록입니다(테마의 색상을 상속합니다).
	- Important 콜아웃이 이제 시안 대신 보라입니다(테마의 색상을 상속합니다). 기본 아이콘도 `lucide-fire` 대신 `lucide-star`를 사용합니다.
	- Error 콜아웃의 기본 아이콘이 `luicde-zap` 대신 `lucide-circle-alert`를 사용합니다.
	- 콜아웃 아이콘 정렬을 제목 텍스트에 더 잘 맞도록 약간 조정했습니다.
- 그 밖에 테마의 소소한 QOL 개선이 있습니다.

#### 수정
- Mermaid, Canvas 스타일링 수정
- 배너 스니펫 라이브 프리뷰 수정
- pl10k 상태바 수정
- dimmed file extensions와 Novel Word Count 플러그인의 호환성 수정. OMG Discord 서버의 `@psolkaiyn`에게 감사드립니다.
- ASCII 아트 렌더링과 방향을 수정했습니다. 필요하다면 사용 중인 ASCII 아트를 업데이트하세요.
- "Background for add before empty state title"의 `linear-gradient` 로직이 이제 올바른 방향을 사용합니다.
- 성능 개선과 코드베이스 일부 정리를 시도했습니다.
- Revert to Pre 1.11 UI를 수정했습니다.
