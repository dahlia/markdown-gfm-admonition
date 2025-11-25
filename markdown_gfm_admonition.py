import re
from typing import List, Optional

from markdown.core import Markdown
from markdown.extensions import Extension
from markdown.blockprocessors import BlockProcessor
from markdown.blockparser import BlockParser
from xml.etree.ElementTree import Element, SubElement

__all__ = ["GfmAdmonitionExtension", "GfmAdmonitionProcessor", "makeExtension"]


class GfmAdmonitionExtension(Extension):
    def extendMarkdown(self, md: Markdown) -> None:
        md.registerExtension(self)
        md.parser.blockprocessors.register(
            GfmAdmonitionProcessor(md.parser),
            "gfm_admonition",
            105
        )


class GfmAdmonitionProcessor(BlockProcessor):
    PATTERN = re.compile(r"""
        ^ \s*
        \\? \[ ! ( NOTE | TIP | IMPORTANT | WARNING | CAUTION ) \\? \]
        (?: $ | (?: [ ] [ ] )? \n )
    """, re.VERBOSE | re.IGNORECASE)

    def __init__(self, parser: BlockParser):
        super().__init__(parser)

    def test(self, parent: Element, block: str) -> bool:
        if parent.tag != "blockquote":
            return False
        match = self.PATTERN.match(block)
        return match is not None

    def run(self, parent: Element, blocks: List[str]) -> Optional[bool]:
        if not blocks:
            return False
        match = self.PATTERN.match(blocks[0])
        blocks[0] = blocks[0][match.end():]
        type_ = match.group(1).lower()
        parent.tag = "div"
        parent.set("class", "admonition " + type_)
        title = SubElement(parent, "p")
        title.set("class", "admonition-title")
        title.text = type_.capitalize()
        self.parser.parseBlocks(parent, blocks)
        blocks.clear()
        return True


def makeExtension(**kwargs):
    return GfmAdmonitionExtension(**kwargs)
