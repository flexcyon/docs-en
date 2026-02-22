---
title: Home
icon: material/home
---

<div align="center">
    <a href="https://flexcyon.github.io/docs-en/">
        <img alt="English Documentation" src="https://img.shields.io/badge/english-docs-blue?style=for-the-badge">
    </a>
    <a href="https://flexcyon.github.io/docs-en/">
        <img alt="中文文档" src="https://img.shields.io/badge/%E4%B8%AD%E6%96%87-%E6%96%87%E6%A1%A3-purple?style=for-the-badge">
    </a>
    <a href="https://matrix.to/#/#flexcyon-space:matrix.org">
        <img alt="Matrix Space" src="https://img.shields.io/matrix/flexcyon-space%3Amatrix.org?style=for-the-badge&logo=matrix&label=Matrix%20Space">
    </a>
</div>

<div align="center">
    <a href="https://www.moritzjung.dev/obsidian-stats/themes/flexcyon">
    <a href="https://www.moritzjung.dev/obsidian-stats/themes/flexcyon">
        <img src="https://img.shields.io/badge/dynamic/json?query=%24%5B%22flexcyon%22%5D.download&url=https%3A%2F%2Freleases.obsidian.md%2Fstats%2Ftheme&style=for-the-badge&label=Downloads&logo=obsidian" referrerpolicy="noreferrer">
    </a>
    <a href="https://github.com/bladeacer/flexcyon/releases/latest">
        <img src="https://img.shields.io/github/v/release/bladeacer/flexcyon?style=for-the-badge&sort=semver&logo=semantic-release" referrerpolicy="noreferrer">
    </a>
    <img alt="Min App Version" src="https://img.shields.io/github/manifest-json/minAppVersion/bladeacer/flexcyon?style=for-the-badge&logo=semver">
</div>

<div align="center">
    <a href="https://github.com/bladeacer/flexcyon/blob/master/LICENSE">
        <img src="https://img.shields.io/github/license/bladeacer/flexcyon?style=for-the-badge" referrerpolicy="noreferrer"> 
    </a>
    <a href="https://github.com/flexcyon/docs-en">
        <img alt="GitHub deployments" src="https://img.shields.io/github/deployments/flexcyon/docs-en/github-pages?style=for-the-badge&logo=github">
    </a>
</div>

This hosts the English documentation for the
[flexcyon theme](https://github.com/bladeacer/flexcyon).

## Quick Links

Here are some links you may be looking for.

### Misc

- [README](./README/index.md)

- [License](./README/license.md)

- [Roadmap](./README/roadmap.md)

- [Credits](./credits/index.md)

- [Changelogs](./changelogs/index.md)

### Styling

- [Style Settings](./Styling/Style-Settings/index.md)

___

#### Questions, Issues?

Feel free to talk about it at:

- [this Matrix Space](https://matrix.to/#/#flexcyon-space:matrix.org)
- [this Obsidian forum topic](https://forum.obsidian.md/t/flexcyon-a-dark-theme-for-obsidian/99869)
- [this Discord thread](https://discord.com/channels/686053708261228577/1338130333698359357)
- [start a GitHub discussion](https://github.com/bladeacer/flexcyon/discussions)

Methods of communication are listed in order of preference.

## Contributing

When contributing do open an issue at
[the repository](https://github.com/bladeacer/flexcyon/issues) or
[start a GitHub discussion](https://github.com/bladeacer/flexcyon/discussions) first.

You can create your own fork before making a pull request.
> Before doing this, do open an issue at this repository first.

This repository comes with some scripts. The important ones include:

- `npm run dev`: SCSS to CSS compiler, assumes you have
[Sass](https://sass-lang.com/) (Dart, Node) installed
- `npm run lint`: Lints the entire SCSS codebase. Reruns linting when a file
write is detected in source files
- `npm run lint-once`: As its namesake says, lints the codebase once
- `npm run fix`: Equivalent to running `stylelint --fix`. Run this only after
your file changes are saved.

If you prefer to use CSS instead of SCSS, place your proposed code changes or
snippets in the `css/` folder. The maintainer will try to integrate them.

Do note that this repository has its own [Code of Conduct](https://github.com/bladeacer/flexcyon/blob/master/CODE_OF_CONDUCT.md)
and [Contributing Guide](https://github.com/bladeacer/flexcyon/blob/master/CONTRIBUTING.md).

### About Comments

Comments on this website uses GitHub Discussions in the source
code repository (`bladeacer/flexcyon`) as a back-end.
