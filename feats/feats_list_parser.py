from bs4 import BeautifulSoup, Tag


def parse_feats_links(list_html: str) -> list[dict]:
    soup = BeautifulSoup(list_html, "html.parser")

    table_div = soup.find(
        "div", class_="div.fill-width:nth-child(2) > div:nth-child(1)"
    )
    table = table_div.table

    for tr in table.select("tbody tr"):
        tds = tr.find_all("td")
        if not tds:
            continue


