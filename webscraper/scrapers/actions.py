from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import override
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BrowserActions(ABC):
    @abstractmethod
    def run(self, driver: WebDriver) -> None:
        raise NotImplementedError


@dataclass
class Click(BrowserActions):
    by: str
    value: str

    @override
    def run(self, driver: WebDriver) -> None:
        element: WebElement = WebDriverWait(driver=driver, timeout=10).until(
            method=EC.element_to_be_clickable(mark=(self.by, self.value))
        )
        element.click()

@dataclass
class WaitForElement(BrowserActions):
    by: str
    value: str

    @override
    def run(self, driver: WebDriver) -> None:
        _ = WebDriverWait(driver=driver, timeout=10).until(
            method=EC.presence_of_element_located(locator=(self.by, self.value))
        )