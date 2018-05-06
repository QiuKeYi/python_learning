# -*- coding:utf-8 -*-
from lxml import etree
import requests
import csv

def main():
    fp = open("./doubanbook.csv","wt",encoding='utf-8')
    writer = csv.writer(fp)
    writer.writerow(('name','url','author','publisher','date','price','rate','comment'))

    urls = ['https://book.douban.com/top250?start={}'.format(i) for i in range(0,250,25)]

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
    }

    for url in urls:
        req = requests.get(url,headers=headers)
        selector = etree.HTML(req.text)
        infos = selector.xpath('//tr[@class="item"]')
        for info in infos:
            name =info.xpath('td/div/a/@title')[0]
            url = info.xpath('td/div/a/@href')[0]
            book_infos = info.xpath('td/p/text()')[0]
            author = book_infos.split('/')[0:-3]
            publisher = book_infos.split('/')[-3]
            date = book_infos.split('/')[-2]
            price = book_infos.split('/')[-1]
            rate = info.xpath('td/div/span[2]/text()')[0]
            comments = info.xpath('td/p/span/text()')
            comment = comments[0] if len(comments)!=0 else "空"
            writer.writerow((name,url,author,publisher,date,price,rate,comment))

if __name__ == '__main__':
    main()