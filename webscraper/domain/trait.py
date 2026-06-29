from dataclasses import dataclass


@dataclass(frozen=True)
class Trait:
    id: int
    name: str | None
    category: str | None
    description: str | None
    source_id: int | None