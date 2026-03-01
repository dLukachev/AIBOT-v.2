from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, DateTime, func

class Base(DeclarativeBase, AsyncAttrs):
    pass

class Users(Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    tid: Mapped[int] = mapped_column(Integer, unique=True, nullable=False)
    name: Mapped[str] = mapped_column(String, nullable=True)
    limit_per_day: Mapped[int] = mapped_column(Integer, default=5)
    limit_per_month: Mapped[int] = mapped_column(Integer, default=20)
    limit_usage_per_day: Mapped[int] = mapped_column(Integer, default=0)
    limit_usage_per_month: Mapped[int] = mapped_column(Integer, default=0)