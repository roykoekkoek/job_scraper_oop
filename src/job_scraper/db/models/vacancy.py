from typing import Optional
from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from job_scraper.db.engine import Base

class Vacancy(Base):
    __tablename__ = "vacancies"

    id: Mapped[int] = mapped_column(primary_key=True)
    external_id: Mapped[str]
    company: Mapped[str]
    salary_bottom: Mapped[int | None]
    salary_top: Mapped[int | None]
    salary: Mapped[int]
    description: Mapped[int]
    experience_years: Mapped[int | None]
    city: Mapped[int]