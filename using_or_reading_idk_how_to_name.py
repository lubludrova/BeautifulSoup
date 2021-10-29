# В этом коде вы сможете получить нужную для вас ссылку (start: 12:40) (End:1:57)

import re
import json

with open("all_cats.json", "r", encoding="utf-8") as file:
    all_jobs = json.load(file)

print("Введите HELP, для помощи или GO, чтобы начать")
door = input()
if door == "HELP":
    print('Программа помогает найти подходящие вам вакансии. По 4 критериям вы можете найти то, что вам нужно.'
          "Если вам не принципиален какой-либо критерий, то можете перейти к следующему, нажав ENTER")
elif door != "GO":
    print("Вы ввели ерунду, в следующий раз слушайте меня")
    exit(0)

print("Введите один из критериев поиска(Город): Москва, Новоссибирк, Екатеринбург, Санкт-Петербург... ")
city1 = str(input())
if len(city1) > 0:
    city = "'" + city1 + "'"
else: city = "' '"

print("Введите один из критериев поиска(Стиль Работы): Полный рабочий день, Можно удаленно")
style_work1 = input()
if len(style_work1) > 0:
    style_work = "'" + style_work1 + "'"
else: style_work = "' '"

print("Введите один из критериев поиска(Компания):Admitad,TINKOFF, BSL...")
company1 = input()
if len(company1) > 0:
    company = "'" + company1 + "'"
else: company = "' '"

print("Введите один из критериев поиска(Разработка):Python, MySQL, C#...")
work1 = input()
if len(work1) > 0:
    work = "'" + work1 + "'"
else: work = "' '"



for link, vacancy in all_jobs.items():
    s = ""
    for i in vacancy:
        s = s + "'" + i
    s = s + "' '"
    pattern1 = re.compile(city)
    pattern2 = re.compile(style_work)
    pattern3 = re.compile(company)
    pattern4 = re.compile(work)
    result1 = pattern1.findall(s)
    result2 = pattern2.findall(s)
    result3 = pattern3.findall(s)
    result4 = pattern4.findall(s)
    if len(result1) > 0 and len(result2) > 0 and len(result3) > 0 and len(result4) > 0:
        print(*vacancy, "Ссылка: ", link)
