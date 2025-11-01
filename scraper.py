from pprint import pprint
import re
import asyncio
from pydoll.browser.chromium import Chrome


async def get_category_title(tag):
    return await (await tag.find(class_name="k-item-text")).text


async def get_category_items(tag):
    result = []
    children = await tag.find(class_name="k-item-text", find_all=True)
    for child in children:
        result.append(child.get_attribute('href'))
    return result


async def main():
    async with Chrome() as browser:
        json = {}
        tab = await browser.start()
        await tab.go_to("https://2e.aonprd.com/")
        side_menu = await tab.find(id='menu-list')
        tags = await side_menu.get_children_elements()

        for i in range(0, len(tags), 2):
            category_title = await get_category_title(tags[i])
            category_items = await get_category_items(tags[i + 1])
            json[category_title] = category_items

        pprint(json)


if __name__ == "__main__":
    asyncio.run(main())
