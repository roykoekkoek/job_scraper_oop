from job_scraper.schemas.vacancies import ABNVacancy

print("Hello world!")

example_abn_vacancy = ABNVacancy(
    id="Dit is een test id",
    salary_bottom=5000,
    salary_top=5900,
    description="Dit is een sample description",
    experience_years=5,
    city="Amsterdam"
)

print(example_abn_vacancy)