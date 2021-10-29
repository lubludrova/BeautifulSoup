import requests

url = ["https://career.habr.com/vacancies?divisions[]=backend&divisions[]=frontend&divisions[]=apps&divisions[]=software&page=2&type=all",
       "https://career.habr.com/vacancies?divisions[]=backend&divisions[]=frontend&divisions[]=apps&divisions[]=software&page=2&type=all",
       "https://career.habr.com/vacancies?divisions[]=backend&divisions[]=frontend&divisions[]=apps&divisions[]=software&page=3&type=all",
       "https://career.habr.com/vacancies?divisions[]=backend&divisions[]=frontend&divisions[]=apps&divisions[]=software&page=4&type=all",
       "https://career.habr.com/vacancies?divisions[]=backend&divisions[]=frontend&divisions[]=apps&divisions[]=software&page=5&type=all"]

headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1"
}

num = 0
for i in url:
    req = requests.get(i, headers=headers)
    src = req.text
    print(src)
    num += 1
    with open(f"index{num}.html", "w", encoding="utf-8") as file:
        file.write(src)
