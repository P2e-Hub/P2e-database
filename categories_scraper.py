import re
from json import dump
from pydoll.browser.tab import Tab


async def get_category_title(tag):
    title = await (await tag.find(class_name="k-item-text")).text
    title = re.sub(r'\s*[^a-zA-Z0-9]+\s*$', '', title)
    title = title.lower()

    return title


async def get_category_items(tag):
    result = []
    children = await tag.find(class_name="k-item-text", find_all=True)
    for child in children:
        result.append(child.get_attribute('href'))
    return result


async def get_categories_json(tab: Tab, base_url: str):
    categories = {}
    await tab.go_to(base_url)
    side_menu = await tab.find(id='menu-list')
    tags = await side_menu.get_children_elements()

    for i in range(0, len(tags), 2):
        category_title = await get_category_title(tags[i])
        category_items = await get_category_items(tags[i + 1])
        categories[category_title] = category_items

    with open("categories.json", "w") as f:
        dump(categories, f, indent=2)
