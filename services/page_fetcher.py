from requests import get


def fetch_categories_html(url: str, timeout: int = 20) -> str:
    response = get(url=url, timeout=timeout)
    response.raise_for_status()
    return response.text
