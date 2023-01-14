import requests
import json
import time
from datetime import datetime
import re
from java_vacancies.hh.Vacancy import Vacancy


def get_vacancy_json_by_url(url):
    req = requests.get(url)
    data = req.content.decode()
    req.close()

    item = json.loads(data)
    return item


def parse_to_vacancy_model(json_vacancy):
    vacancy = Vacancy()
    vacancy.name = json_vacancy['name']
    vacancy.desc = re.sub(re.compile('<.*?>'), '', str(json_vacancy['description']).replace('<br />', '\n\n  '))
    salary = json_vacancy.get('salary', dict())

    if salary is not None:
        vacancy.salary_from = salary.get('from')
        vacancy.salary_to = salary.get('to')
        vacancy.salary_currency = salary.get('currency')

    vacancy.company_name = json_vacancy['employer']['name']
    vacancy.region = json_vacancy['area']['name']
    vacancy.skills = ', '.join([x['name'] for x in json_vacancy['key_skills']])
    vacancy.date_publication = datetime.strptime(json_vacancy['published_at'], '%Y-%m-%dT%H:%M:%S%z').strftime(
        "%d.%m.%Y %H:%M:%S")

    return vacancy


def get_vacancies_urls(count):
    params = {
        'text': 'Java программист',
        'area': 113,
        'page': 0,
        'per_page': count
    }

    req = requests.get('https://api.hh.ru/vacancies', params)
    data = req.content.decode()
    req.close()

    jsObj = json.loads(data)
    vac_urls = [x['url'] for x in jsObj['items']]

    return vac_urls


def get_vacancies(count):
    vacancies = []
    urls = get_vacancies_urls(count)
    for url in urls:
        vac_json = get_vacancy_json_by_url(url)
        vac_model = parse_to_vacancy_model(vac_json)
        vacancies.append(vac_model)
        time.sleep(0.1)
    vacancies = sorted(vacancies, key=lambda vac: vac.date_publication, reverse=True)
    return vacancies


if __name__ == "__main__":
    print(get_vacancies(3), sep="\n")
