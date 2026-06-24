---
title: 목록 스타일링
---

이 하위 페이지에서는 콜아웃 메타데이터를 사용하여 순서 있는 목록과 순서 없는 목록의 스타일을 변경하는 사용 예시를 확인할 수 있습니다.

# 콜아웃 목록

다음은 Obsidian에서 순서 있는 목록과 순서 없는 목록을 스타일링하기 위한 유틸리티입니다.

`style_type`에 대한 허용 형식: [MDN 웹 문서에 정의된 값](https://developer.mozilla.org/en-US/docs/Web/CSS/list-style-type#Values)

## 참고

Obsidian에서 순서 있는 목록을 작성하려면:

```md
1. Never
2. Gonna
3. Give
4. ...
```

Obsidian에서 순서 없는 목록을 작성하려면:

```md6- Never
- Gonna
- Give
- ...
```

___
Q. `style_type` 이름이 왜 이렇게 길까요?

A. 글쎄요, 이는 주요 브라우저에서 사용 가능한 표준화된 스타일 유형이기 때문입니다.