from typing import override
from sqlalchemy import String, Text
from sqlalchemy.orm import (
    Mapped,
    mapped_column
)
from .base import Base


class Trait(Base):
    __tablename__: str = "traits"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(20))
    category: Mapped[str] = mapped_column(String(20))
    description: Mapped[Text | None] = mapped_column(Text, nullable=True)

    @override
    def __str__(self) -> str:
        if self.description is None:
            return self.name
        return self.name + " - " + str(self.description)
