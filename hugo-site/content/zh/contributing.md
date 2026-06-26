---
title: 贡献
---

## 主题

请在发出 PR 之前创建自己的 Fork
> 在执行此操作之前, 请先提交 Issue

### 开发

主题存储库附带了一些辅助脚本. 重要的包括:

- `npm run dev`: SCSS-CSS 编译器, 假设您已安装 [Sass](https://sass-lang.com/) (Dart 或 Node 版本)
- `npm run lint`: 检查整个 SCSS 代码库. 在源文件中检测到文件写入时重新运行代码检查.
- `npm run lint-once`: 与其同名, 一次性检查整个 SCSS 代码库
- `npm run fix`: 相当于运行 `stylelint --fix` 命令. 仅在保存文件更改后运行此操作.

如果您更喜欢使用 CSS 而不是 SCSS, 请放置您建议的代码更改在 `css/` 文件夹中. 我们将尝试整合它们.

由此以外，您可以在以下网址 [打开问题](https://github.com/bladeacer/flexcyon/issues)
或开始 GitHub 讨论.

请注意, 存储库有自己的 [行为准则](https://github.com/bladeacer/flexcyon/blob/master/code_of_conduct)
和 [贡献指南](https://github.com/bladeacer/flexcyon/blob/master/contributing).

## 翻译

有关更多详细信息以及当前支持的语言集,
请[参阅文档存储库](https://github.com/flexcyon/docs-en).

### 翻译指南

1. 翻译应符合母语人士的阅读习惯.
> 例如：汉, 日, 韩语 (CJK) 在字符间距的约定上差异很大.

2. 允许机器翻译和人工审核.
> 请关注满足准则 1 机器翻译并不总是推断上下文与最地道措辞的最佳方法.

3. 译者应能够流利地使用目标语言进行读写. 我们不需要母语级别的熟练度, 
但您至少应该对这门语言有足够的了解, 以便进行人工审核.
> 我们可以判断您是否纯粹使用机器翻译, 如准则 2 所述.

4. 请将您的翻译拆分为大小合理的独立 Git 提交 (Commit). 这会让代码审
查 (Review) 变得轻松得多. 同时请使用清晰合理的提交信息，以便我们能
够理解每次提交的范围和目的.

5. 在您的 Git Fork 中, 创建一个单独的 Git 分支并根据功能进行适当命
名 (例如 `ko-translation-1.4.0`). 更改也将合并到上游 (Upstream) 仓
库的一个独立功能分支中, 以便随后 cherry-pick 到其他 Git 分支
(如 `master` 或 `staging`).

6. 如果外部参考链接存在对应的多语言 (i18n) 版本, 请进行替换.
> 例如: 中文文档中应使用 `https://developer.mozilla.org/zh-CN/docs/Web/...`, 而不是
英文版的 `en-US` 链接.

7. 英文文档是唯一的权威事实来源 (Canonical source of truth).

8. 宁可不翻译, 也不要提供错误或有误导性的翻译.
> 与准则 7 一样, 如有疑问, 请参阅英文文档或其他已有的语言翻译版本.

9. 避免翻译某些特定的术语或单词, 以免用户感到困惑, 或者该功能主要以其英文名称为人所知.
> 例如: "Bases" (Obsidian 功能), "Omnisearch" (插件名称) 或 "Obsidian" 本身.

10. 尊重并延续现有的代码库规范.

提交 Issue 或拉取请求（Pull Request）时, 遵循相同的开源协作规范.

项目的行为准则（Code of Conduct）和贡献指南（Contributing Guide）基本相同.

### 现有翻译

欢迎提交 Issue 和 PR 来改进现有的翻译.
