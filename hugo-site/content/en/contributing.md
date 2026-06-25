---
title: Contributing
---

## Theme

When contributing do open an issue at
[the repository](https://github.com/bladeacer/flexcyon/issues) or
[start a GitHub discussion](https://github.com/bladeacer/flexcyon/discussions) first.

You can create your own fork before making a pull request.
> Before doing this, do open an issue at this repository first.

### Development

The theme repository comes with some scripts. The important ones include:

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

---

## Translations

See the [documentation repository](https://github.com/flexcyon/docs-en) for more details, as well as the current set of languages supported.

### Translation guidelines

1. Translations should feel natural to native speakers reading it.
> E.g. conventions on character spacing differ widely between Chinese, Japanese
and Korean (CJK).

2. Machine translation with manual human review is allowed.
> Do make the effort especially to fulfil guideline #1, machine translation
> is not always the best at inferring context and phrasing.

3. Translators should be able to read and write fluently in the language they are translating to.
We do not need native speaker levels of proficiency but you should at least know
the language enough to manually review it.
> We can tell if you are purely using machine translation, re guideline #2.

4. Split your translation into different commits of sensible size. This
makes it far easier to review. Use sensible commit messages, we should be able
to understand the scope and purpose of each commit.

5. In your Git fork, create a separate Git branch named appropriately based on feature
(e.g. ko-translation-1.4.0). Changes will be merged into a separate feature branch
upstream as well, for cherry-picking to other Git branches like master or staging.

6. i18n links and references where i18n equivalents exist
> E.g. using https://developer.mozilla.org/zh-CN/docs/Web/CSS/Reference/Properties/list-style-type#Values
> instead of https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-type#Values
> for Chinese documentation.

7. English documentation is the canonical source of truth.

8. No translation at all is better than wrong or misleading translation.
> As with guideline #7, refer to the English documentation and other translations when in doubt.

9. Avoid translating certain terminology or words, where the user gets confused
or it refers to something mostly known in its English name.
> E.g. "Bases" (the Obsidian feature) or "Omnisearch" (the plugin name) or "Obsidian"

10. Respect existing codebase conventions.

The same conventions for opening issues or pull requests apply as well.
Code of Conduct and Contributing Guide is largely the same.
