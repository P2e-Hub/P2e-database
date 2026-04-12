from sqlalchemy import String, Text
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column
)


class Base(DeclarativeBase):
    pass


class Trait(Base):
    __tablename__: str = "traits"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(20))
    trait_type: Mapped[str] = mapped_column(String(20))
    description: Mapped[Text] = mapped_column(Text)
