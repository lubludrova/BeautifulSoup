from bs4 import BeautifulSoup
import csv
import json


#Создания таблицы для сбора информации
with open(f"data.csv", "w", encoding="UTF-16") as file:
    writer = csv.writer(file)
    writer.writerow(
        (
            "Вакансия",
            "Ссылка",
            "Компания",
            "Доп информация",
            "Скиллы"
        )
    )


all_cats = {}

#Сбор данных вакансия + ссылка
all_vacancies_dict = {}
for i in range(1,6):

    with open(f"index{i}.html", "r", encoding="utf-8") as file:
        src = file.read()

    soup = BeautifulSoup(src, "lxml")

    #Сбор Данных
    all_data = soup.find_all(class_="vacancy-card")
    for item in all_data:
        data = item.find_all(class_="vacancy-card__info")

        vac_title = data[0].find(class_="vacancy-card__title-link")
        title = vac_title.text
        link = "https://career.habr.com/" + vac_title.get("href")

        vac_meta = data[0].find(class_="vacancy-card__meta").find_all(class_="preserve-line")
        meta = []
        for i in range(len(vac_meta)):
            meta.append(vac_meta[i].text)
        # print(meta)

        vac_salary = data[0].find(class_="basic-salary")
        if len(vac_salary.text) > 1:
            salary = vac_salary.text
        else: salary = "Не известно"
        #print(salary)

        vac_skills = data[0].find(class_="vacancy-card__skills").find_all(class_="preserve-line")
        #print(vac_skills)
        skills = []
        for i in range(len(vac_skills)):
            skills.append(vac_skills[i].text)
        #print(skills)

        vac_company = data[0].find(class_="link-comp link-comp--appearance-dark")
        company = vac_company.text
        #print(company)


        all_cats[link] = title,company,*meta,*skills



        #Заполнение таблицы
        with open(f"data.csv", "a", encoding="UTF-16") as file:
            writer = csv.writer(file)
            writer.writerow(
                (
                    title,
                    link,
                    company,
                    meta,
                    skills
                )
            )
#Заполнение json
with open("all_cats.json", "w", encoding="utf-8") as file:
    json.dump(all_cats, file, indent=4, ensure_ascii=False)