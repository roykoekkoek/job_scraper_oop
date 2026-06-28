## TODO: Make schemas related to vacancies
from typing import Optional
from pydantic import BaseModel

class ABNVacancy(BaseModel):
    id: str
    salary_bottom: int
    salary_top: int
    description: int
    experience_years: int
    city: str

class Vacancy(BaseModel):
    id: str
    company: str
    salary_bottom: Optional[int]
    salary_top: Optional[int]
    salary: int
    description: str
    experience_years: Optional[int]
    city: str
