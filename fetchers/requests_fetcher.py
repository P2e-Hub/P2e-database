from fetchers.base_fetcher import BaseFetcher
from requests import get


class RequestsFetcher(BaseFetcher):
    def fetch(self, url: str, actions=None) -> str:
        response = get(url, timeout=10)
        response.raise_for_status()
        return response.text
