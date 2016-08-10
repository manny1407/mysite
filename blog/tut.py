# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests

url = "http://news.tut.by/"

response = requests.get(url)
html = response.content

soup = BeautifulSoup(html, "html.parser")
print(soup.decode('cp1251'))