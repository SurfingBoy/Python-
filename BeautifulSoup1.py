import urllib.request
import re
from bs4 import BeautifulSoup
def main():
    url='https://baike.baidu.com/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB'
    response=urllib.request.urlopen(url)
    html=response.read()
    soup=BeautifulSoup(html,'html.parser')

    for each in soup.find_all(href=re.compile('item')):
        print(each.text,'->',''.join(['http://baike.baidu.com',each['href']]))
if __name__=='__main__':
    main()