---
title: Contributing
---

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

Do note that this repository has its own [Code of Conduct](https://github.com/bladeacer/flexcyon/blob/master/code_of_conduct)
and [Contributing Guide](https://github.com/bladeacer/flexcyon/blob/master/contributing).
