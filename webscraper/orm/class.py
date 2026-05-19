from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column
from .base import Base


class Classes(Base):
    __table_args__: str = "class"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    rarity: Mapped[str] = mapped_column(String(20))
    key_attribute: Mapped[str] = mapped_column(String(100))
    hit_points: Mapped[int] = mapped_column()
    tradition: Mapped[str] = mapped_column(String(50))
    perception_proficiency: Mapped[str] = mapped_column(String(20))
    fortitude_proficiency: Mapped[str] = mapped_column(String(20))
    reflex_proficiency: Mapped[str] = mapped_column(String(20))
    will_proficiency: Mapped[str] = mapped_column(String(20))
    description: Mapped[str] = mapped_column(Text)
    source_id: Mapped[int] = mapped_column(ForeignKey("sources.id"))