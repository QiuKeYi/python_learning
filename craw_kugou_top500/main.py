import requests
import time
from bs4 import BeautifulSoup

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"
}

def get_info(url):
    wb_data = requests.get(url,headers=headers)

    soup = BeautifulSoup(wb_data.text,"lxml")

    ranks = soup.select('span.pc_temp_num')

    titles = soup.select('div.pc_temp_songlist > ul > li > a')

    times = soup.select('div.pc_temp_songlist > ul > li > span.pc_temp_tips_r > span')


    for rank,title,time in zip(ranks,titles,times):
        data = {
            'rank':rank.get_text().strip(),
            'singer':title.get_text().split('-')[0],
            'song':title.get_text().split('-')[1],
            'time':time.get_text().strip()
        }
        print(data)


if __name__ == "__main__":
    urls = [ 'http://www.kugou.com/yy/rank/home/{}-8888.html?from=rank'.format(i) for i in range(1,24)]

    for url in urls:
        get_info(url)
        time.sleep(1.5)