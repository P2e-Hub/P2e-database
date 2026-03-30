from abc import ABC, abstractmethod
from selenium.webdriver.remote.webdriver import WebDriver
from typing import Callable

Actions = Callable[[WebDriver], None] | None


class BaseFetcher(ABC):
    @abstractmethod
    def fetch(self, url: str, actions: Actions = None) -> str:
        raise NotImplementedError
