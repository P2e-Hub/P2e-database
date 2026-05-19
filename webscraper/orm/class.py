from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from .base import Base


class InitialProficiency(Base):
    __table_args__: str = "initial_proficiency"

    id: Mapped[int] = mapped_column(primary_key=True)
    perception: Mapped[str] = mapped_column(String(1))
    fortitude: Mapped[str] = mapped_column(String(1))
    reflex: Mapped[str] = mapped_column(String(1))
    will: Mapped[str] = mapped_column(String(1))
    unarmed_attacks: Mapped[str] = mapped_column(String(1))
    simple_weapons: Mapped[str] = mapped_column(String(1))
    unarmored_defense: Mapped[str] = mapped_column(String(1))
    light_armor: Mapped[str] = mapped_column(String(1))
    medium_armor: Mapped[str] = mapped_column(String(1))