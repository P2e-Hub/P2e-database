from typing import override
from fetchers.base_fetcher import BaseFetcher
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import (
    presence_of_element_located
)
from selenium.webdriver.remote.webdriver import WebDriver
from scrapers.actions import BrowserActions

class SeleniumFetcher(BaseFetcher):
    driver: WebDriver | None = None

    def __init__(self, actions: list[BrowserActions]) -> None:
        self.actions: list[BrowserActions] = actions
        if self.driver is None:
            self.__build_web_driver()

    @override
    def fetch(self, url: str) -> str:
        if self.driver is None:
            return ""

        self.driver.get(url)
        _ = WebDriverWait(self.driver, timeout=10).until(
            method=presence_of_element_located(locator=(By.TAG_NAME, "body"))
        )
        
        for action in self.actions:
            action.run(driver=self.driver)

        return self.driver.page_source

    def __build_web_driver(self) -> None:
        options = webdriver.FirefoxOptions()
        options.add_argument("-headless")
        self.driver = webdriver.Firefox(options=options)
