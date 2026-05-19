from datetime import datetime
from sqlalchemy import String, func
from sqlalchemy.orm import Mapped, mapped_column
from .base import Base


class Source(Base):
    __tablename__: str = "sources"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255))
    category: Mapped[str] = mapped_column(String(100))
    page: Mapped[int] = mapped_column()
    version: Mapped[str] = mapped_column(String(20))
    is_legacy: Mapped[bool] = mapped_column()
    created_at: Mapped[datetime] = mapped_column(insert_default=func.now())