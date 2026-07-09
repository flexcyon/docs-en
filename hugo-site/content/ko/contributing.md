---
title: 기여하기
---

## 테마

기여할 때는 먼저 [리포지토리](https://github.com/bladeacer/flexcyon/issues)에 이슈를 열거나
[GitHub 토론](https://github.com/bladeacer/flexcyon/discussions)을 시작하세요.

풀 리퀘스트를 보내기 전에 직접 포크를 생성할 수 있습니다.
> 그 전에 먼저 이 리포지토리에 이슈를 열어주세요.

### 개발

이 리포지토리는 몇 가지 스크립트를 포함하고 있습니다. 중요한 것들은 다음과 같습니다:

- `npm run dev`: SCSS를 CSS로 컴파일하는 도구, [Sass](https://sass-lang.com/) (Dart, Node)가 설치되어 있음을 가정합니다.
- `npm run lint`: 전체 SCSS 코드베이스를 린트합니다. 소스 파일에 변경이 감지되면 린팅을 다시 실행합니다.
- `npm run lint-once`: 이름 그대로 코드베이스를 한 번 린트합니다.
- `npm run fix`: `stylelint --fix`를 실행하는 것과 동일합니다. 파일 변경 사항이 저장된 후에만 실행하세요.

CSS를 SCSS 대신 사용하길 원한다면, 제안한 코드 변경사항이나 스니펫을 `css/` 폴더에 넣어주세요. 유지보수자가 이를 통합하려고 노력할 것입니다.

이 리포지토리는 자체 [행동 강령](https://github.com/bladeacer/flexcyon/blob/master/code_of_conduct)과 [컨트리뷰션 가이드](https://github.com/bladeacer/flexcyon/blob/master/contributing)를 가지고 있음을 참고해 주세요.

---

## 번역

자세한 내용과 현재 지원되는 언어 목록은
[문서 리포지토리](https://github.com/flexcyon/docs-en)를 참고하세요.

### 번역 가이드라인

1. 번역문은 원어민이 읽었을 때 자연스럽게 느껴져야 합니다.
> 예를 들어 글자 간격에 대한 관례는 중국어, 일본어, 한국어(CJK) 사이에서도 크게 다릅니다.

2. 사람이 직접 검수하는 것을 전제로 기계 번역을 사용해도 됩니다.
> 특히 가이드라인 #1을 충족하도록 공을 들여주세요. 기계 번역이 맥락과 표현을
> 항상 잘 파악하는 것은 아닙니다.

3. 번역자는 번역 대상 언어를 유창하게 읽고 쓸 수 있어야 합니다.
원어민 수준의 능숙함까지는 필요 없지만, 최소한 직접 검수할 수 있을 만큼은 그 언어를
알아야 합니다.
> 가이드라인 #2와 관련해, 순수하게 기계 번역만 사용했는지는 알아볼 수 있습니다.

4. 번역을 적절한 크기의 여러 커밋으로 나누세요. 그러면 리뷰하기가 훨씬 쉬워집니다.
적절한 커밋 메시지를 사용하세요. 각 커밋의 범위와 목적을 이해할 수 있어야 합니다.

5. Git 포크에서 기능에 맞게 적절히 이름 붙인 별도의 Git 브랜치를 만드세요
(예: ko-translation-1.4.0). 변경 사항은 업스트림에서도 별도의 기능 브랜치로 병합되어,
master나 staging 같은 다른 Git 브랜치로 cherry-pick할 수 있게 합니다.

6. i18n 대응물이 존재하는 링크와 참조는 i18n 버전을 사용하세요.
> 예를 들어 한국어 문서에서는
> https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-type#Values
> 대신 https://developer.mozilla.org/ko/docs/Web/CSS/Reference/Properties/list-style-type#Values
> 를 사용합니다.

7. 영어 문서가 정본(canonical source of truth)입니다.

8. 잘못되거나 오해를 부르는 번역보다는 아예 번역하지 않는 편이 낫습니다.
> 가이드라인 #7과 마찬가지로, 확신이 서지 않을 때는 영어 문서와 다른 번역을 참고하세요.

9. 사용자가 혼란스러워하거나 주로 영어 이름으로 알려져 있는 용어나 단어는 번역을 피하세요.
> 예: "Bases"(Obsidian 기능), "Omnisearch"(플러그인 이름), "Obsidian"

10. 기존 코드베이스의 관례를 존중하세요.

이슈나 풀 리퀘스트를 여는 관례도 동일하게 적용됩니다.
행동 강령과 컨트리뷰션 가이드도 대체로 같습니다.

### 기존 번역

기존 번역을 개선하기 위한 이슈와 PR을 환영합니다.
