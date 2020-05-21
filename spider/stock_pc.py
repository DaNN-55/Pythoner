import requests
import re
from bs4 import BeautifulSoup


def getHtmlText(url, code='utf-8'):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = code
        return r.text
    except:
        return '爬取失败！！'

def getstocklist(lst, stockurl):
    html = getHtmlText(stockurl, 'GB2312')
    soup = BeautifulSoup(html, 'html.parser')
    a = soup.find_all('a')
    for i in a:
        try:
            href = i.attrs['href']
            lst.append(re.findall(r'[s][hz]\d{6}', href)[0])
        except:
            continue

def getstockinfo(lst, stockurl, fpath):
    count = 0
    for stock in lst:
        url = stockurl + stock +'.html'
        html = getHtmlText(url)
        try:
            if html == '':
                continue
            infoDict = {}
            soup = BeautifulSoup(html, 'html.parser')
            stockinfo = soup.find('div', attrs={'class': 'stock_bets'})

            name = stockinfo.find_all(attrs={'class': 'bets_name'})[0]
            infoDict.update({'股票名称': name.text.split()[0]})

            keylsit = stockinfo.find_all('dt')
            valuelist = stockinfo.find_all('dd')
            for i in range(len(keylsit)):
                key = keylsit[i].text
                val = valuelist[i].text
                infoDict[key] = val

            with open(fpath, 'a', encoding='utf-8') as f:
                f.write(str(infoDict) + '\n')
                count += 1
                print('\r当前速度：{:.2f}%'.format(count*100/len(lst), end=''))
        except:
            count += 1
            print('\r当前速度：{:.2f}%'.format(count*100/len(lst), end=''))
            continue
    return ''
def main():
    stock_list_url = 'http://quote.eastmoney.com/stocklist.html'
    stock_info_url = 'https://gupiao.baidu.com/stock'
    out_file = 'D://stocklist.text'
    slist = []
    getstocklist(slist, stock_list_url)
    getstockinfo(slist, stock_info_url, out_file)

main()
