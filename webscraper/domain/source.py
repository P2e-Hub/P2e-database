from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class Source:
    id: int
    name: str
    category: str
    page: int
    version: str
    is_legacy: bool
    created_at: datetime