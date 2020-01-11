import requests
from bs4 import BeautifulSoup
from requests import get
from requests.auth import HTTPDigestAuth
import json

OUT_FILE_NAME = 'top10_tags.json'

class HhGrabber():
    HOME = "https://pikabu.ru/"
    HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Referer": "https://pikabu.ru/",
        "Content-Type": "application/x-www-form-urlencoded",
        "DNT": "1",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "TE": "Trailers",
    }

    def __init__(self, username, password):
#        pass
        self.session = requests.Session()
        self.session.headers = self.HEADERS
        self.auth(username, password)

    def getPage(self, url):
        return self.session.get(url).text

    def auth(self, username, password):
        get = self.session.get(self.HOME)
#        abc = input("x: ")
        data = {
            "backUrl": "https://pikabu.ru/",
            "action": "Войти",
            "username": username,
            "password": password,
            "_xsrf": 'a'
        }

    def parse_pikabu(self, html):
        soup = BeautifulSoup(html,features="html.parser")
        tag_divs = soup.find_all("div", class_ ="story__tags tags")
        result = []
        for div in tag_divs:
            tags = div.find_all('a', class_="tags__tag")
            i = 0
            for tag in tags:
                i += 1
                current_tag = tag.text
                result.append(current_tag)
        print("Count of posts:", i)
        return result

def out_file(out_dict, out_filename, encoding_table):
#    try:
        with open(out_filename, 'w', encoding=encoding_table) as f:
            json.dump(out_dict, f, ensure_ascii=False)
            print(f"файл {out_filename} создался успешно!")
#    except:
#        print("Ошибка при записи выходного файла JSON")


grabber = HhGrabber("zinchenkovasil", "barsik123456")
lst_tags = []
for i in range(20):
    print("Page: ", i)
    html = grabber.getPage(url="https://pikabu.ru?page="+str(i)) #/account/login?backurl=/")
    lst_tags += grabber.parse_pikabu(html)

print("Count of tags:", len(lst_tags))

dict_tags = {}
for tag in lst_tags:
    if tag in dict_tags:
        dict_tags[tag] += 1
    else:
        dict_tags[tag] = 1

top10_tags = []
for tag in dict_tags:
    max_ = 0
    dict_ = {}
    for key, value in dict_tags.items():
        if value > max_:
            max_ = value
            max_key = key
    dict_[max_key] = max_
    top10_tags.append(dict_)
    dict_tags[max_key] = -1

top10_tags = top10_tags[:10]
print(top10_tags)

out_file(top10_tags, OUT_FILE_NAME, 'UTF-16')