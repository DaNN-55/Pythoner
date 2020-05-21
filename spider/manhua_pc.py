import requests
from selenium import webdriver
import os

def makefile(path):
    if os.path.exists(path):
        os.mkdir(path)

def savepic(filename, url):
    content = requests.get(url).content
    with open(filename, 'wb') as f:
        f.write(content)


def findpic(url):

    titles_lst = []
    driver = webdriver.Chrome()
    driver.get(url)
    driver.implicitly_wait(3)

    name = driver.find_element_by_xpath('/html/body/div[2]/h1')
    makefile(str(name))

    titles1 = driver.find_elements_by_class_name('comic_Serial_list')
    for titles2 in titles1:
        link = titles2.find_elements_by_tag_name('a')
        for i in link:
            titles_lst.append(i.get_attribute('href'))

    driver.quit()

    Comis = dict(name=name, urls=titles_lst)
    return Comis


def get_pic(Comis):
    Comis_lst = Comis['urls']
    basedir = Comis['name']

    driver = webdriver.Chrome()
    for title in Comis_lst:
        driver.get(title)
        driver.implicitly_wait(3)

        dirname = driver.find_elements_by_xpath('/html/body/div[3]/div[1]/div[2]/div/a')
        for i in dirname:
            pic_name = i.text
            makefile(pic_name)
            pagenum = len(driver.find_elements_by_tag_name('option'))
            next_page = driver.find_element_by_xpath('//*[@id="AD_j1"]/div/a[4]')
            for hua in range(pagenum):
                pic = driver.find_element_by_id('curPic').get_attribute('src')
                picname = pic_name + '/' + str(hua) + '.png'
                savepic(picname, pic)
                print('当前章节{}下载完毕'.format(picname))

            next_page.click()

    driver.quit()
    print('所有章节下载完毕！')

def main():
    url = str(input('请输入漫画地址：\n'))
    Comis = findpic(url)
    get_pic(Comis)

main()