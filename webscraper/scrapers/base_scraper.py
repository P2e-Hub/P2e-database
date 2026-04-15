from typing import Generic, TypeVar
from fetchers.base_fetcher import BaseFetcher
from abc import ABC, abstractmethod
from bs4 import BeautifulSoup

T = TypeVar(name="T")


class BaseScraper(ABC, Generic[T]):
    def __init__(self, baseFetcher: BaseFetcher):
        self.fetcher: BaseFetcher = baseFetcher

    def scrape(self, url: str) -> list[T]:
        html = self.fetcher.fetch(url=url)
        soup = BeautifulSoup(html, 'html.parser')
        return self.parse(soup=soup)

    @abstractmethod
    def parse(self, soup: BeautifulSoup) -> list[T]:
        raise NotImplementedError
