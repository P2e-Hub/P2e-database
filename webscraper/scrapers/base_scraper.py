from typing import Generic, TypeVar
from fetchers.base_fetcher import BaseFetcher
from abc import ABC, abstractmethod
from bs4 import BeautifulSoup

T = TypeVar(name="T")


class BaseScraper(ABC, Generic[T]):
    def __init__(self, baseFetcher: BaseFetcher) -> None:
        self.fetcher: BaseFetcher = baseFetcher

    def scrape(self, url: str) -> list[T]:
        html: str = self.fetcher.fetch(url=url)
        soup: BeautifulSoup = BeautifulSoup(markup=html, features='html.parser')
        return self.parse(soup=soup)

    @abstractmethod
    def parse(self, soup: BeautifulSoup) -> list[T]:
        raise NotImplementedError
