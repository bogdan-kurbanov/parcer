import requests
from bs4 import BeautifulSoup
from time import sleep
from lxml import html

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                         " AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}


def get_url():
    for count in range(0,121,20):

        url = f"http://www.spisszkol.eu/typ/?wojewodztwo=dolnoslaskie&powiat=wroclawski&start={count}"

        responce = requests.get(url, headers=headers,)
        responce.encoding = "utf8"
        soup = BeautifulSoup(responce.text, "lxml")
        data = soup.find_all("div", class_="doc_entry")


        for i in data:
            card_url = i.find("a").get("href")
            yield card_url

def array():
    for list_card in get_url():
        responce = requests.get(list_card, headers=headers)
        responce.encoding = "utf8"
        sleep(3)
        soup = BeautifulSoup(responce.text, "lxml")
        parsed = html.fromstring(responce.text)
        emails = [e.attrib['title'] for e in parsed.xpath('//a[contains(@href, "email") and @title]')]
        s = " ".join(emails)
        data = soup.find("div", class_="page_body")
        name = data.find("p", class_="map_title red").text
        adres = data.find("p", itemprop="address").text
        try:
            telefon = data.find("span", itemprop="telephone").text
        except Exception as e:
            print(e)
            telefon = None
        yield name, adres, telefon,s


