from fetchers.base_fetcher import BaseFetcher
from requests import get
from typing import override


class RequestsFetcher(BaseFetcher):
    @override
    def fetch(self, url: str) -> str:
        response = get(url)
        response.raise_for_status()
        return response.text
