---
title: Lucide 아이콘
---

커스텀 콜아웃 / 콜아웃 메타데이터: "`<lucide-icon-value>`"

사용법:

```md
> [!info|lucide-git-fork] 콜아웃 아이콘이 lucide git 포크 아이콘으로 교체됩니다.
> 콜아웃 내용은 정상적으로 렌더링됩니다.
```

## 참고
Lucide 아이콘 설정을 사용할 때는 전체 콜아웃 메타데이터 또는 커스텀 콜아웃 섹션 모두 lucide 아이콘 값과 일치해야 하며, 그렇지 않으면 아이콘이 렌더링되지 않습니다.

- 예: `>[!lucide-git-fork|title-orange bg-blue]` 대신 `>[!bg-blue|lucide-git-fork title-orange]` 또는 `>[!lucide-git-fork title-orange|bg-blue]`

요약하면, 동일한 콜아웃 유형 내에서 또는 메타데이터 내에서 Lucide 아이콘 콜아웃 유형을 사용할 수 없습니다.

이 기능은 **최소 Obsidian 버전 1.9.12 이상**을 필요로 합니다.