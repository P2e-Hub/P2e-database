from typing import override
from unittest import TestCase
from unittest.mock import Mock
from bs4 import BeautifulSoup
from fetchers.base_fetcher import BaseFetcher
from scrapers.base_scraper import BaseScraper


class FakeScraper(BaseScraper[str]):
    def parse(self, soup: BeautifulSoup) -> list[str]:
        result: list[str] = []

        for element in soup.select(selector=".item"):
            result.append(element.get_text(strip=True))

        return result

class TestBaseScraper(TestCase):
    def test_scrape_sucess(self) -> None:
        fetcher_mock: Mock = Mock(spec=BaseFetcher)
        fetcher_mock.fetch.return_value = """
            <html>
                <body>
                    <span class="item">A</span>
                    <span class="item">B</span>
                </body>
            </html>
        """

        scraper: FakeScraper = FakeScraper(baseFetcher=fetcher_mock)

        url: str = "url de teste"
        result: list[str] = scraper.scrape(url)

        self.assertEqual(result, ["A", "B"])
        fetcher_mock.fetch.assert_called_once_with(url=url)