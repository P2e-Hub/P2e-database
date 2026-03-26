from ..services.page_fetcher import fetch_categories_html
from .categories_parser import parse_categories


def discover_links(base_url: str):
    html = fetch_categories_html(url=base_url)
    categories = parse_categories(html=html)

    return categories
