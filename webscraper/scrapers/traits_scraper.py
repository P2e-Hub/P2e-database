from .base_scraper import BaseScraper
from bs4 import BeautifulSoup, Tag
from bs4.element import NavigableString


class TraitsScraper(BaseScraper):
    def parse(self, soup: BeautifulSoup) -> dict:
        result = {"traits": []}

        main = soup.find(id='main')
        if not isinstance(main, Tag):
            return result

        traits = main.contents[9]
        if not isinstance(traits, Tag):
            return result

        traits_types = traits.find_all(name="h2", class_="title")

        for traits_type in traits_types:
            current = traits_type

            while current is not None:
                if isinstance(current, Tag) and current.name == 'br':
                    break

                if isinstance(current, NavigableString):
                    current = current.next_sibling
                    continue

                if not isinstance(current, Tag):
                    current = current.next_sibling
                    continue

                if current.get_text(strip=True) == traits_type.get_text(strip=True):
                    current = current.next_sibling
                    continue

                link = current.find('a')
                if link is None:
                    current = current.next_sibling
                    continue

                href = link.get('href')
                if not href or not isinstance(href, str):
                    current = current.next_sibling
                    continue

                description = self.get_trait_description(href)
                trait = {
                    "name": current.string,
                    "type": traits_type.string,
                    "desc": description
                }

                print(trait)
                result["traits"].append(trait)

                current = current.next_sibling

        return result

    def get_trait_description(self, url: str) -> str:
        base_url = "https://2e.aonprd.com"
        url = f"{base_url}/{url}"
        html = self.fetcher.fetch(url=url)
        soup = BeautifulSoup(html, 'html.parser')

        external_link = soup.find(class_="external-link")
        if not isinstance(external_link, Tag):
            return ""

        description_section = external_link.next_sibling

        while not isinstance(description_section, NavigableString) and description_section is not None:
            description_section = description_section.next_sibling

        if description_section is None:
            return ""

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
