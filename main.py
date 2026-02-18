from json import load
from os import path
from selenium import webdriver

base_url = "https://2e.aonprd.com"


async def get_feats(url: str):
    pass


def main():
    options = webdriver.FirefoxOptions()
    options.add_argument("-headless")
    driver = webdriver.Firefox(options=options)

    # if not path.isfile("categories.json"):
    #     get_categories_json(base_url=base_url)

    json_file = open("categories.json")
    categories = load(json_file)

    driver.quit()


if __name__ == "__main__":
    main()
