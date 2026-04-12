from .base_scraper import BaseScraper
from bs4 import BeautifulSoup, Tag
from bs4.element import NavigableString, PageElement
from typing import override
from orm.trait import Trait


class TraitsScraper(BaseScraper[Trait]):
    @override
    def parse(self, soup: BeautifulSoup) -> list[Trait]:
        main: Tag = self.__get_main_element(soup=soup)
        traits_container: Tag = self.__get_traits_container(main=main)
        trait_type_headers: list[Tag] = self.__get_trait_type_headers(traits_containers=traits_container)

        result: list[Trait] = []

        for header in trait_type_headers:
            result.extend(self.__parse_traits_from_header(header=header))

        return result

    def __get_main_element(self, soup: BeautifulSoup) -> Tag:
        main = soup.find(id='main')
        if not isinstance(main, Tag):
            raise ValueError("Element 'main' not found")

        return main

    def __get_traits_container(self, main: Tag) -> Tag:
        traits_container = main.contents[9]
        if not isinstance(traits_container, Tag):
            raise ValueError("Traits block not valid")

        return traits_container

    def __get_trait_type_headers(self, traits_containers: Tag) -> list[Tag]:
        return traits_containers.find_all(name="h2", class_="title")

    def __parse_traits_from_header(self, header: Tag) -> list[Trait]:
        traits: list[Trait] = []
        trait_type: str = header.get_text(strip=True)
        current_type: PageElement | None = header.next_sibling

        while current_type is not None:
            if self.__is_section_break(node=current_type):
                break

            tag = self.__get_valid_trait_tag(node=current_type)
            if tag is None:
                current_type = current_type.next_sibling
                continue

            href = self.__get_link_href(tag=tag)
            if href is None:
                current_type = current_type.next_sibling
                continue

            description = self.__get_trait_description(url=href)
            trait = Trait(
                name=current_type.get_text(strip=True),
                trait_type=trait_type,
                description=description
            )

            print(trait)
            traits.append(trait)

            current_type = current_type.next_sibling

        return traits

    def __is_section_break(self, node: PageElement) -> bool:
        return isinstance(node, Tag) and node.name == 'br'

    def __get_valid_trait_tag(self, node: PageElement) -> Tag | None:
        if isinstance(node, NavigableString) or not isinstance(node, Tag):
            return None

        return node

    def __get_link_href(self, tag: Tag) -> str | None:
        link = tag.find('a')
        if not isinstance(link, Tag):
            return None

        href = link.get(key='href')
        if not isinstance(href, str) or not href:
            return None

        return href

    def __get_trait_description(self, url: str) -> str:
        base_url = "https://2e.aonprd.com"
        html = self.fetcher.fetch(url=f"{base_url}/{url}")
        soup = BeautifulSoup(html, 'html.parser')

        external_link = soup.find(class_="external-link")
        if not isinstance(external_link, Tag):
            return ""

        description_section = external_link.next_sibling

        while not isinstance(description_section, NavigableString) and description_section is not None:
            description_section = description_section.next_sibling

        if description_section is None:
            return ""

        description: str = self.__parse_description_section(description_section=description_section)

        return description

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
