from random import choice
from unittest import TestCase, main
from xml.etree.ElementTree import canonicalize

from markdown import Markdown

from markdown_gfm_admonition import GfmAdmonitionExtension


class GfmAdmonitionTestCase(TestCase):
    def setUp(self) -> None:
        ext = choice([
            GfmAdmonitionExtension(),
            "markdown_gfm_admonition:GfmAdmonitionExtension",
            "gfm_admonition",
        ])
        self.md = Markdown(extensions=[ext])

    def assertHtmlEqual(self, expected: str, actual: str):
        self.assertEqual(
            canonicalize(
                f"<body>{expected}</body>",
                with_comments=False,
                strip_text=True,
            ),
            canonicalize(
                f"<body>{actual}</body>",
                with_comments=False,
                strip_text=True,
            ),
        )

    def testNote(self):
        result = self.md.convert(
            "> This is not an admonition block.\n"
            "\n"
            "---\n"
            "\n"
            "> [!NOTE]  \n"
            "> Highlights information that users should take into account,\n"
            "> even when skimming.\n"
        )
        self.assertHtmlEqual(
            "<blockquote><p>This is not an admonition block.</p></blockquote>"
            '<hr></hr><div class="admonition note"><p class="admonition-title">'
            "Note</p><p>Highlights information that users should take into "
            "account,\neven when skimming.</p></div>",
            result
        )

    def testTip(self):
        result = self.md.convert(
            "> [!TIP]\n"
            "> Optional information to help a user be more successful.\n"
            "\n"
            "---\n"
            "> This is not an admonition block.\n"
        )
        self.assertHtmlEqual(
            '<div class="admonition tip"><p class="admonition-title">Tip</p>'
            "<p>Optional information to help a user be more successful.</p>"
            "</div><hr></hr><blockquote><p>This is not an admonition block.</p>"
            "</blockquote>",
            result
        )

    def testImportant(self):
        result = self.md.convert(
            "> [!IMPORTANT]\n"
            ">\n"
            "> Crucial information necessary for users to succeed."
        )
        self.assertHtmlEqual(
            '<div class="admonition important"><p class="admonition-title">'
            "Important</p><p>Crucial information necessary for users to "
            "succeed.</p></div>",
            result
        )

    def testWarning(self):
        result = self.md.convert(
            "> [!WARNING]\n"
            "> \n"
            "> Critical content demanding immediate user attention due to "
            "potential risks.\n"
        )
        self.assertHtmlEqual(
            '<div class="admonition warning"><p class="admonition-title">'
            "Warning</p><p>Critical content demanding immediate user attention "
            "due to potential risks.</p></div>",
            result
        )

    def testCuation(self):
        result = self.md.convert(
            "> [!CAUTION]\n"
            "> \n"
            "> Negative potential consequences of an action."
        )
        self.assertHtmlEqual(
            '<div class="admonition caution"><p class="admonition-title">'
            "Caution</p><p>Negative potential consequences of an action.</p>"
            "</div>",
            result
        )

    def testEscapedBrackets(self):
        result = self.md.convert(
            "> \\[!TIP\\]\n"
            "> Optional information to help a user be more successful.\n"
            "\n"
            "---\n"
            "> This is not an admonition block.\n"
        )
        self.assertHtmlEqual(
            '<div class="admonition tip"><p class="admonition-title">Tip</p>'
            "<p>Optional information to help a user be more successful.</p>"
            "</div><hr></hr><blockquote><p>This is not an admonition block.</p>"
            "</blockquote>",
            result
        )


if __name__ == "__main__":
    main()
