import requests
from bs4 import BeautifulSoup

def gethtmltext(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return '失败！！'

def souptext(url):
    soup = BeautifulSoup(url, 'html.parser')
    message = soup.find_all('div', {'class': 'hd'})
    print(type(message))
    for i in message:
        href = i.find('a').get('href')
        name = i.find('span', {'class': 'title'})
        lst = {
            '作品': name.get_text(),
            '链接': href
        }
        print(lst)

def main():
    #https: // movie.douban.com / top250?start = 50 & filter =
    url = 'https://movie.douban.com/top250'
    for i in range(0, 10):
        url1 = url + '?start={}'.format(i*25)
        html = gethtmltext(url1)
        souptext(html)

main()


