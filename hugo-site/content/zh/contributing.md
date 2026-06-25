---
title: 贡献
---

## 主题

请在发出 PR 之前创建自己的 Fork
> 在执行此操作之前, 请先打开 GitHub 问题

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

1. 对于母语人士来说, 每一份翻译都应该显得自然.
>例如: 汉语, 日语和韩语（CJK）的字符间距约定差异很大.

2. 允许机器翻译和人工审核.
> 请特别努力满足准则 1, 机器翻译并不总是推断上下文和措辞的最佳方法.

3. 将翻译拆分为大小合理的不同 Git 提交. 这使得审查变得容易得多. 使用合理的 Git 提交消息, 
我们应该能够理解每个提交的范围和目的.

4. 国际化 (i18n) 链接和参考, 其中存在 i18n 等效物
> 例如, 中文文档使用 https://developer.mozilla.org/zh-CN/docs/Web/CSS/Reference/Properties/list-style-type#Values
> 而不是 https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-type#Values

5. 英文文档是真理的标准来源.

6. 没有翻译比错误或误导性的翻译更好.
> 与准则 5 一样, 如有疑问, 请参阅英文文档和其他翻译.

7. 避免翻译某些术语或单词, 以免用户会感到困惑, 或者它指的是英文名称中最为人所知的东西.
> 例如，"Bases"（Obsidian 功能）或 "Omnisearch" (插件名称) 或 "Obsidian"

8. 尊重现有的代码库惯例.

打开问题或拉取请求的相同约定也适用.

行为准则和贡献指南基本相同.
