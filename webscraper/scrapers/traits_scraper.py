from .base_scraper import BaseScraper
from bs4 import BeautifulSoup


class TraitsScraper(BaseScraper):
    def parse(self, soup: BeautifulSoup) -> dict:
        result = {"traits": []}
        main = soup.find(id='main')
        traits = main.contents[9]
        traits_types = traits.find_all(name="h2", class_="title")

        for traits_type in traits_types:
            current = traits_type
            while current is not None and current.name != ('br'):
                if current.name is None or (current.string == traits_type.string):
                    current = current.next_sibling
                    continue

                description = self.get_trait_description(current.a['href'])
                trait = {
                    "name": current.string,
                    "type": traits_type.string,
                    "desc": description
                }
                current = current.next_sibling

                result["traits"].append(trait)

                print(trait)

    def get_trait_description(self, url: str) -> str:
        base_url = "https://2e.aonprd.com"
        html = self.fetcher.fetch(url=base_url + '/' + url)
        soup = BeautifulSoup(html, 'html.parser')
        description_section = soup.find(
            class_='external-link').next_sibling.next_sibling
        description = ''

        while description_section.name != 'br':
            if description_section.string is None:
                description += description_section
            else:
                description += description_section.string
            description_section = description_section.next_sibling

        return description
