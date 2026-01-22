import re
from json import dump
from typing import List
from bs4 import BeautifulSoup
from bs4.element import Tag
from requests import get


def get_categories_json(base_url: str) -> None:
    categories = {}

    response = get(base_url)
    soup = BeautifulSoup(response.text, "html.parser")
    side_menu = soup.find("div", class_="modern-menu-items")
    categories_tags = side_menu.find_all("div", class_="modern-menu-item")

    for item in categories_tags:
        title = get_category_title(item)
        links = get_category_links(item)

        categories[title] = links

    with open("categories.json", "w") as f:
        dump(categories, f, indent=2)


def get_category_title(item: Tag) -> str:
    title = item.find("span", class_="modern-menu-item-text").string
    title = re.sub(r'\s*[^a-zA-Z0-9]+\s*$', '', title)

    return title


def get_category_links(item: Tag) -> List[str]:
    link_tags = item.next_sibling.next_sibling.find_all("a")
    links = []
    for tag in link_tags:
        links.append(tag["href"])

    return links
