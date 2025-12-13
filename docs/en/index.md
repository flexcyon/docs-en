---
title: Home
icon: material/home
---

<p align="left">
    <a href="https://www.moritzjung.dev/obsidian-stats/themes/flexcyon-1/">
        <img src="https://img.shields.io/badge/dynamic/json?query=%24%5B%22flexcyon%22%5D.download&url=https%3A%2F%2Freleases.obsidian.md%2Fstats%2Ftheme&style=for-the-badge&label=Downloads&logo=obsidian" referrerpolicy="noreferrer">
    </a>
    <a href="https://github.com/bladeacer/flexcyon/blob/master/LICENSE">
        <img src="https://img.shields.io/github/license/bladeacer/flexcyon?style=for-the-badge" referrerpolicy="noreferrer"> 
    </a>
    <a href="https://github.com/bladeacer/flexcyon/releases/latest">
        <img src="https://img.shields.io/github/v/release/bladeacer/flexcyon?style=for-the-badge&sort=semver" referrerpolicy="noreferrer">
    </a>
</p>

This hosts the English documentation for the
[flexcyon theme](https://github.com/bladeacer/flexcyon).

> Currently, there are some Style Settings options undergoing refactor for
> better performance.
>
> There are legacy options kept for backwards compatibility if you are using
> earlier version of the application

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

## Questions, Issues?

Feel free to talk about it at:

- [this Discord thread](https://discord.com/channels/686053708261228577/1338130333698359357).
- [this Obsidian forum topic](https://forum.obsidian.md/t/flexcyon-a-dark-theme-for-obsidian/99869)

## Contributing

You can create your own fork before making a pull request.
> Before doing this, do open an issue at the repository first.

The repository comes with some scripts. The important ones include:

- `npm run dev`: SCSS to CSS compiler, assumes you have
[Sass](https://sass-lang.com/) (Dart, Node) installed
- `npm run lint`: Lints the entire SCSS codebase. Reruns linting when a file
write is detected in source files
- `npm run lint-once`: As its namesake says, lints the codebase once
- `npm run fix`: Equivalent to running `stylelint --fix`. Run this only after
your file changes are saved.

If you prefer to use CSS instead of SCSS, place your proposed code changes or
snippets in the `css/` folder. The maintainer will try to integrate them.

Alternatively, you can open an issue at
[the repository](https://github.com/bladeacer/flexcyon/issues) or
[start a GitHub discussion](https://github.com/bladeacer/flexcyon/discussions) here.

Do note that this repository has its own [Code of Conduct](https://github.com/bladeacer/flexcyon/blob/master/CODE_OF_CONDUCT.md)
and [Contributing Guide](https://github.com/bladeacer/flexcyon/blob/master/CONTRIBUTING.md).

### About Comments

Comments on this website uses GitHub Discussions in the source
code repository (`bladeacer/flexcyon`) as a back-end.
