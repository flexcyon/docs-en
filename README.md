# About
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
    <a href="https://github.com/bladeacer/flexcyon/blob/master/LICENSE">
        <img src="https://img.shields.io/github/license/bladeacer/flexcyon?style=for-the-badge" referrerpolicy="noreferrer"> 
    </a>
    <a href="https://github.com/flexcyon/docs-en">
        <img alt="GitHub deployments" src="https://img.shields.io/github/deployments/flexcyon/docs-en/github-pages?style=for-the-badge&logo=github">
    </a>
</div>

This hosts the English documentation for the
[flexcyon theme](https://github.com/bladeacer/flexcyon). You can [view it here](https://flexcyon.github.io/docs-en/).

For more languages, open a FR/PR.

Current languages supported:

- English
- Chinese
- Korean (PR in progress, based on 1.4.0 English documentation)

## Utilities

There is a [Makefile](./Makefile) which invokes utility Python scripts one can use.
> See the scripts directory for more details

## Translation guidelines

1. Translations should feel natural to native speakers reading it.
> E.g. conventions on character spacing differ widely between Chinese, Japanese
and Korean (CJK).

2. Machine translation with manual human review is allowed.
> Do make the effort especially to fulfil guideline #1, machine translation
> is not always the best at inferring context and phrasing.

3. Split your translation into different commits of sensible size. This
makes it far easier to review. Use sensible commit messages, we should be able
to understand the scope and purpose of each commit.

4. English documentation is the canonical source of truth.

5. No translation at all is better than wrong or misleading translation.

## License
The documentation source and content are both licensed under the MIT License.
