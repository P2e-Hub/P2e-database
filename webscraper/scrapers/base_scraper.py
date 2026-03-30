from fetchers.base_fetcher import BaseFetcher
from fetchers.selenium_fetcher import SeleniumFetcher
from fetchers.requests_fetcher import RequestsFetcher
from abc import ABC, abstractmethod
from bs4 import BeautifulSoup


class BaseScraper(ABC):
    def __init__(self):
        self.fetcher: BaseFetcher

    def scrape(self, url: str) -> list[dict[str, str]]:
        html = ''
        actions = self.get_actions()

        if actions is None:
            self.fetcher = RequestsFetcher()
        else:
            self.fetcher = SeleniumFetcher()

        html = self.fetcher.fetch(url=url, actions=actions)

        return self.parse(BeautifulSoup(html, 'html.parser'))

    def get_actions(self):
        return None

    @abstractmethod
    def parse(self, soup: BeautifulSoup) -> list[dict[str, str]]:
        raise NotImplementedError
