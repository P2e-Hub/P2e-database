import re
from bs4 import BeautifulSoup
from bs4.element import Tag


def parse_categories(html: str) -> dict[str, list[str]]:
    soup = BeautifulSoup(html, "html.parser")
    side_menu = soup.find("div", class_="modern-menu-items")
    if side_menu is None:
        return {}

    categories = {}
    categories_tags = side_menu.find_all("div", class_="modern-menu-item")

    for item in categories_tags:
        title = _get_category_title(item)
        links = _get_category_links(item)
        categories[title] = links

    return categories


def _get_category_title(item: Tag) -> str:
    title = item.find("span", class_="modern-menu-item-text")
    text = (title.get_text(strip=True) if title else "")
    return re.sub(r'\s*[^a-zA-Z0-9]+\s*$', '', text)


def _get_category_links(item: Tag) -> list[str]:
    sibling = item.find_next_sibling()
    if sibling is None:
        return []
    link_tags = sibling.find_all("a", href=True)
    return [a["href"] for a in link_tags]
