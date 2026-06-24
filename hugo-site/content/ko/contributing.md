---
title: 기여하기
---

기여할 때는 먼저 [리포지토리](https://github.com/bladeacer/flexcyon/issues)에 이슈를 열거나
[GitHub 토론](https://github.com/bladeacer/flexcyon/discussions)을 시작하세요.

풀 리퀘스트를 보내기 전에 직접 포크를 생성할 수 있습니다.
> 그 전에 먼저 이 리포지토리에 이슈를 열어주세요.

이 리포지토리는 몇 가지 스크립트를 포함하고 있습니다. 중요한 것들은 다음과 같습니다:

- `npm run dev`: SCSS를 CSS로 컴파일하는 도구, [Sass](https://sass-lang.com/) (Dart, Node)가 설치되어 있음을 가정합니다.
- `npm run lint`: 전체 SCSS 코드베이스를 린트합니다. 소스 파일에 변경이 감지되면 린팅을 다시 실행합니다.
- `npm run lint-once`: 이름 그대로 코드베이스를 한 번 린트합니다.
- `npm run fix`: `stylelint --fix`를 실행하는 것과 동일합니다. 파일 변경 사항이 저장된 후에만 실행하세요.

CSS를 SCSS 대신 사용하길 원한다면, 제안한 코드 변경사항이나 스니펫을 `css/` 폴더에 넣어주세요. 유지보수자가 이를 통합하려고 노력할 것입니다.

이 리포지토리는 자체 [행동 강령](https://github.com/bladeacer/flexcyon/blob/master/code_of_conduct)과 [컨트리뷰션 가이드](https://github.com/bladeacer/flexcyon/blob/master/contributing)를 가지고 있음을 참고해 주세요.