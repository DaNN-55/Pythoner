import requests
from lxml import etree

header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36}'}

def gethtml(url):
    try:
        r = requests.get(url, headers=header)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.content
    except:
        return '爬取失败！'

def getimage(url):
    new_html = etree.HTML(url)
    images = new_html.xpath('//ul/li/a/img/@src')
    titles = new_html.xpath('//ul/li/a/img/@alt')
    for image, title in zip(images, titles):
        imagehtml = gethtml('http://www.521609.com' + str(image))
        with open('d://python/meinv/'+str(title)+'.jpg', 'wb') as f:
            f.write(imagehtml)
            f.close()
            print('保存成功！')

def main():
    url = 'http://www.521609.com/daxuemeinv/list8{}.html'
    number = input('请输入想要获取的页数：')
    for i in range(1, int(number)):
        new_url = url.format(str(i))
        html = gethtml(new_url)
        getimage(html)

main()
