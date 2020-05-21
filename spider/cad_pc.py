# 本人毕业设计时所用

import requests
from lxml import etree

def gethtmltext(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return '爬取失败！！'

def etreehtml(url):
    html = etree.HTML(url)
    titles = html.xpath('//div[@class="modelName"]/a')
    hrefs = html.xpath('//div[@class="modelName"]/a/@href')
    print(len(titles))
    for title, href in zip(titles, hrefs):
        lst = {
            '标题': title.text,
            '链接': href
        }
        print(lst)

def main():
    url = 'http://my.mfcad.com/Tuzhi/Sou/index/keyword/{}/p/{}'
    keyword = input('请输入你要搜索的关键词：')
    for i in range(1, 8):
        new_url = url.format(str(keyword), str(i))
        html = gethtmltext(new_url)
        etreehtml(html)

main()
