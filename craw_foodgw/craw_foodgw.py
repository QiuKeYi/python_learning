# -*- coding:utf-8 -*-
import os
import sys
import requests
from bs4 import BeautifulSoup

MAINPAGE = 'http://www.foodgw.com'

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
}
def craw():
    with open("book.txt","w") as wfile:
        for index in range(1,200,1):
            try:
                res = requests.get(MAINPAGE + "/list/8-{}.html".format(index), headers=headers).content.decode("gbk")
                soup = BeautifulSoup(res,"html.parser")
            except:
                print("Error is coming")
                continue
            booklist = soup.select('#content > div > div.col-md-8 > div > div.panel-body > div > div > div.media-body > h4 > a')
            for book in booklist:
                wfile.write(book.get_text()+" : "+book.get("href")+"\n")
                print(book.get_text()+" : "+book.get("href"))


if __name__ == "__main__":
    craw()