from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait


class FeatsListFetcher:
    def __init__(self, driver: WebDriver, base_url: str, timeout: int = 20):
        self.driver = driver
        self.base_url = base_url
        self.wait = WebDriverWait(driver=driver, timeout=timeout)

    def get_list_html(self, feats_relative_url: str) -> None:
        self.driver.get(self.base_url + feats_relative_url)

    def click_show_all(self) -> None:
        pass
