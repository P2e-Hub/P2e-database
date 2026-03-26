from fetchers.base_fetcher import BaseFetcher
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.remote.webdriver import WebDriver


class SeleniumFetcher(BaseFetcher):
    driver: WebDriver | None = None

    def __init__(self):
        if not self.driver:
            options = webdriver.FirefoxOptions()
            options.add_argument("-headless")
            self.driver = webdriver.Firefox(options=options)

    def fetch(self, url: str, actions=None) -> str:
        self.driver.get(url)
        WebDriverWait(self.driver, 10).until(
            presence_of_element_located((By.TAG_NAME, "body"))
        )
        if actions:
            actions(self.driver)

        return self.driver.page_source
