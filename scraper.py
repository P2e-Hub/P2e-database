import pprint
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from urllib.parse import urljoin, urlparse


def group_lis_and_divs(tags):
    lis = tags.find_all('li', class_="expand")
    groups = []

    for li in lis:
        div = li.find_next_sibling('div')
        group = (li, div)
        groups.append(group)

    return groups


def fill_types_of_content_dict(groups, collection):
    for group in groups:
        title = group[0].find('span', class_="k-item-text").string
        title = re.sub(r'^[^a-zA-z0-9]+|[^a-zA-z0-9]+$', '', title)
        title = re.sub(r'[^a-zA-z0-9\s]', ' ', title)
        title = re.sub(r'\s+', ' ', title)
        title = title.lower().replace(' ', '_')

        a_tags = group[1].find_all('a', class_="k-item-text")

        content = {}
        for a_tag in a_tags:
            name = a_tag.string
            link = a_tag['href']
            content[name] = link

        collection[title] = content


def main():
    driver = webdriver.Firefox()
    url = "https://2e.aonprd.com/"

    driver.get(url)

    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    tags = soup.find('ul', attrs={"id": "menu-list"})

    groups = group_lis_and_divs(tags)
    types_of_content = {}
    fill_types_of_content_dict(groups, types_of_content)
    pprint.pprint(types_of_content)


if __name__ == "__main__":
    main()
