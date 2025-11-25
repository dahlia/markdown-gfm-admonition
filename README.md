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


Usage
-----

To use this extension, you need to install it first:

~~~~ bash
uv add markdown-gfm-admonition
# or
pip install markdown-gfm-admonition
~~~~

Then, you can use it in your Python code like this:

~~~~ python
from markdown import Markdown
from markdown_gfm_admonition import GfmAdmonitionExtension

md = Markdown(extensions=[GfmAdmonitionExtension()])
html = md.convert("""
> [!NOTE]
> Highlights information that users should take into account,
> even when skimming.
""")
~~~~

> [!TIP]
> Instead of importing `GfmAdmonitionExtension` directly, you can use
> the entry point `"gfm_admonition"` as well to load the extension:
>
> ~~~~ python
> md = Markdown(extensions=["gfm_admonition"])
> ~~~~
