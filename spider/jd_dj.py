import requests
from lxml import etree

def gethtml(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.content
    except:
        return '爬取失败!'

def findmessage(url):
    html = etree.HTML(url)
    prices = html.xpath('//li[@class="gl-item"]/div/div[3]/strong/i/text()')
    titles = html.xpath('//li[@class="gl-item"]/div/div[4]/a/em/text()[1]')
    hrefs = html.xpath('//li[@class="gl-item"]/div/div[4]/a/@href')
    for price, title, href in zip(prices, titles, hrefs):
        lst = {
            '标题': title,
            '价格': price,
            '链接': 'http:'+href
        }
        print(lst)

def main():
    for i in range(1, 8, 2):
        url = 'https://search.jd.com/Search?keyword=%E7%9B%91%E5%90%AC%E8%80%B3%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E7%9B%91%E5%90%AC%E8%80%B3%E6%9C%BA&page={}&s=1&click=0'.format(i)
        html=gethtml(url)
        findmessage(html)

main()

