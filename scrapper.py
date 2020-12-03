import sqlite3
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import json

conn = None
conn = sqlite3.connect("db/db_scrapper.db")


def sendReq():
    URL = 'https://www.falabella.com/falabella-cl/product/7183917/Bicicleta-M.T.B.-27.5-Alum.-Hero-310-17.5-/7183918'

    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    elements = soup.findAll('script', {'type': 'application/ld+json'})
    finalElements = str(elements)  # transformar soup a str
    x = finalElements.replace('"', '-')
    print(x)
    x2 = x.split('<script class=-next-head- type=-application/ld+json->')
    print(x2[2])


if __name__ == "__main__":
    sendReq()
