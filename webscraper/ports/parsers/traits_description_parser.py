from typing import override

from bs4 import BeautifulSoup, Tag
from bs4.element import NavigableString, PageElement

from ports.parsers.parser import Parser


class TraitsDescriptionParser(Parser[str]):
    @override
    def parse(self, html: str) -> list[str]:
        soup: BeautifulSoup = BeautifulSoup(html, "html.parser")

        external_link = soup.find(class_="external-link")
        if not isinstance(external_link, Tag):
            return []

        description_section = external_link.next_sibling

        while not isinstance(description_section, NavigableString) and description_section is not None:
            description_section = description_section.next_sibling

        if description_section is None:
            return []

        description: str = self.__parse_description_section(description_section=description_section)

        return [description]

    def __parse_description_section(self, description_section: PageElement | None) -> str:
        parts: list[str] = []

        while description_section is not None:
            if isinstance(description_section, Tag) and description_section.name == 'br':
                break

            if isinstance(description_section, NavigableString):
                parts.append(str(description_section))
            elif isinstance(description_section, Tag):
                parts.append(description_section.get_text(" ", strip=True))

            description_section = description_section.next_sibling

        return "".join(parts).strip()