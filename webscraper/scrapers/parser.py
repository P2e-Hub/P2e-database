from typing import Generic, TypeVar
from fetchers.base_fetcher import BaseFetcher
from abc import ABC, abstractmethod
from bs4 import BeautifulSoup

T = TypeVar(name="T")


class Parser(ABC, Generic[T]):
    @abstractmethod
    def parse(self, html: str) -> list[T]:
        raise NotImplementedError
