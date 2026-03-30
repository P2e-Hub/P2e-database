from fetchers.base_fetcher import BaseFetcher, Actions
from requests import get
from typing import override


class RequestsFetcher(BaseFetcher):
    @override
    def fetch(self, url: str, actions: Actions = None) -> str:
        response = get(url, timeout=10)
        response.raise_for_status()
        return response.text
