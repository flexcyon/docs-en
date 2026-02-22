---
title: Foreword
icon: material/home
---

<p align="left" style="scale: 1.1;margin-left:5%;">
    <a href="https://www.moritzjung.dev/obsidian-stats/themes/flexcyon-1/">
        <img src="https://img.shields.io/badge/dynamic/json?query=%24%5B%22flexcyon%22%5D.download&url=https%3A%2F%2Freleases.obsidian.md%2Fstats%2Ftheme&style=for-the-badge&label=下载数&logo=obsidian" referrerpolicy="noreferrer" alt="下载数">
    </a>
    <a href="https://github.com/bladeacer/flexcyon/blob/master/LICENSE">
        <img src="https://img.shields.io/github/license/bladeacer/flexcyon?label=许可证&style=for-the-badge" referrerpolicy="noreferrer" alt="许可证">
    </a>
    <a href="https://github.com/bladeacer/flexcyon/releases/latest">
        <img src="https://img.shields.io/github/v/release/bladeacer/flexcyon?label=最低版本&style=for-the-badge&sort=semver" referrerpolicy="noreferrer" alt="最低版本">
    </a>
    <a href="https://matrix.to/#/#flexcyon-space:matrix.org">
        <img alt="Matrix" src="https://img.shields.io/matrix/flexcyon-space%3Amatrix.org?style=for-the-badge&logo=matrix&label=Matrix%20Space">
    </a>
</p>

这里存放着 [Flexcyon 主题](https://github.com/bladeacer/flexcyon) 的中文文档。

**请注意, 英文文档是原始版本。**

**若两者之间存在差异, 应以英文文档为正确版本。**

## 快速链接

以下是您可能正在寻找的一些链接


### 关于主题

- [自述](./README/index.md)

- [许可证](./README/license.md)

- [路线图](./README/roadmap.md)

- [鸣谢](./credits/index.md)

- [更改日志](./changelogs/index.md)

### 样式

- [样式设置](./Styling/Style-Settings/index.md)

___

## 有关于主题的问题?

请随时通过这些渠道与我们联系.

- [Discord](https://discord.com/channels/686053708261228577/1338130333698359357).
- [Obsidian 论坛主题](https://forum.obsidian.md/t/flexcyon-a-dark-theme-for-obsidian/99869)

## 贡献

请在发出 PR 之前创建自己的 Fork
> 在执行此操作之前, 请先打开 GitHub 问题

此存储库附带了一些辅助脚本。重要的包括:


- `npm run dev`: SCSS-CSS 编译器, 假设您已安装 [Sass](https://sass-lang.com/) (Dart 或 Node 版本)
- `npm run lint`: 检查整个SCSS代码库. 在源文件中检测到文件写入时重新运行代码检查.
- `npm run lint-once`: 与其同名, 一次性检查整个SCSS代码库
- `npm run fix`: 相当于运行 `stylelint --fix` 命令. 仅在保存文件更改后运行此操作.

如果您更喜欢使用 CSS 而不是 SCSS, 请放置您建议的代码更改在 `css/` 文件夹中。我们将尝试整合它们。

Alternatively, you can open an issue at
[the repository](https://github.com/bladeacer/flexcyon/issues) or
[start a GitHub discussion](https://github.com/bladeacer/flexcyon/discussions) here.

由此以外，您可以在以下网址[打开问题](https://github.com/bladeacer/flexcyon/issues)
或开始 GitHub 讨论.

请注意, 存储库有自己的[行为准则](https://github.com/bladeacer/flexcyon/blob/master/CODE_OF_CONDUCT.md)
和[贡献指南](https://github.com/bladeacer/flexcyon/blob/master/CONTRIBUTING.md)

### 关于评论

本网站的评论使用源代码库中的 GitHub 讨论作为后端。
