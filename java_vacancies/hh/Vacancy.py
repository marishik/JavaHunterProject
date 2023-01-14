class Vacancy:
    name = ""
    desc = ""
    skills = []
    company_name = ""
    salary_from = "Не указана"
    salary_to = "Не указана"
    salary_currency = "Не указана"
    region = ""
    date_publication = ""

    def __repr__(self):
        return f'name: {self.name}\ndesc: {self.desc}\nskills: {self.skills}\ncompany: {self.company_name}\nsalary_from: {self.salary_from}\nsalary_to: {self.salary_to}\nsalary_currency: {self.salary_currency}\nregion: {self.region}\ndate_publication: {self.date_publication}'
