import asyncio
from json import load
from os import path
from pydoll.browser.chromium import Chrome
from pydoll.browser.tab import Tab
from categories_scraper import get_categories_json

base_url = "https://2e.aonprd.com"


async def get_feats(tab: Tab, url: str):
    await tab.go_to(base_url + url)


async def main():
    async with Chrome() as browser:
        tab = await browser.start()
        if not path.isfile("categories.json"):
            await get_categories_json(tab, base_url=base_url)

        json_file = open("categories.json")
        json = load(json_file)

        await get_feats(tab, json["feats"][0])


if __name__ == "__main__":
    asyncio.run(main())
