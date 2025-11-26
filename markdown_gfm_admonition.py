import re
from typing import List, Optional
from xml.etree.ElementTree import Element, SubElement

from markdown.blockparser import BlockParser
from markdown.blockprocessors import BlockProcessor
from markdown.core import Markdown
from markdown.extensions import Extension

__all__ = ["GfmAdmonitionExtension", "GfmAdmonitionProcessor", "makeExtension"]


class GfmAdmonitionExtension(Extension):
    def extendMarkdown(self, md: Markdown) -> None:
        md.registerExtension(self)
        md.parser.blockprocessors.register(
            GfmAdmonitionProcessor(md.parser), "gfm_admonition", 105
        )


class GfmAdmonitionProcessor(BlockProcessor):
    PATTERN = re.compile(
        r"""
        ^ \s*
        \\? \[ ! ( NOTE | TIP | IMPORTANT | WARNING | CAUTION ) \\? \]
        [ ]? (.*)
        (?: [ ]+ (.*) )?
        (?: $ | (?: [ ] [ ] )? \n )
    """,
        re.VERBOSE | re.IGNORECASE,
    )

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
        blocks[0] = blocks[0][match.end() :]
        type_ = match.group(1).lower()
        override_title = match.group(2)
        parent.tag = "div"
        parent.set("class", "admonition " + type_)
        title = SubElement(parent, "p")
        title.set("class", "admonition-title")
        title.text = override_title if override_title else type_.capitalize()
        title.text = override_title if override_title else type_.capitalize()
        self.parser.parseBlocks(parent, blocks)
        blocks.clear()
        return True


def makeExtension(**kwargs):
    return GfmAdmonitionExtension(**kwargs)
