from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class Source:
    id: int
    name: str
    category: str | None
    page: int | None
    version: str | None
    is_legacy: bool
    created_at: datetime | None