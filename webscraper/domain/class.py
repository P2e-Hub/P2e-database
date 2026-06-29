from dataclasses import dataclass


@dataclass(frozen=True)
class Class:
    id: int
    name: str
    rarity: str | None
    key_attribuite: str | None
    hit_points: int | None
    tradition: str | None
    perception_proficiency: str | None
    fortitude_proficiency: str | None
    reflex_proficiency: str | None
    will_proficiency: str | None
    description: str | None
    source_id: int | None