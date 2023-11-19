markdown-gfm-admonition
=======================

[![PyPI][PyPI badge]][PyPI]
[![GitHub Actions status][GitHub Actions status badge]][GitHub Actions status]

This package is an extension of [Python Markdown] that enables
the [admonition syntax of GitHub Flavored Markdown][1].

There are five types of admonitions:

~~~~ markdown
> [!NOTE]  
> Highlights information that users should take into account,
> even when skimming.

> [!TIP]
> Optional information to help a user be more successful.

> [!IMPORTANT]  
> Crucial information necessary for users to succeed.

> [!WARNING]  
> Critical content demanding immediate user attention due to potential risks.

> [!CAUTION]
> Negative potential consequences of an action.
~~~~

It generates the same HTML as [Python Markdown's built-in admonition
extension][2]:

~~~~ html
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>Highlights information that users should take into account,
even when skimming.</p>
</div>
~~~~

[PyPI badge]: https://img.shields.io/pypi/v/markdown-gfm-admonition
[PyPI]: https://pypi.org/project/markdown-gfm-admonition/
[GitHub Actions status badge]: https://github.com/dahlia/markdown-gfm-admonition/actions/workflows/build.yaml/badge.svg
[GitHub Actions status]: https://github.com/dahlia/markdown-gfm-admonition/actions/workflows/build.yaml
[Python Markdown]: https://github.com/Python-Markdown/markdown
[1]: https://github.com/orgs/community/discussions/16925
[2]: https://python-markdown.github.io/extensions/admonition/
