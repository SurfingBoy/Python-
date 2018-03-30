# -*- coding:utf-8 -*-
import requests
from pyquery import PyQuery as py

headers = {

    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'

}
url = 'http://www.zhihu.com/explore'
html = requests.get(url, headers=headers).text
doc = py(html)
items = doc('.explore-tab .feed-item').items()
for item in items:
    question = item.find('h2').text()
    author = item.find('.author-link-line').text()
    time = item.find('.visible-expanded').text()
    content = py(item.find('.content').html()).text()
    with open('explore.txt', 'a', encoding='utf-8') as file:
        file.write('\n'.join(['话题：' + question, '作者：' + author, '发布日期：' + time[3:], '回答：' + content]))
        file.write('\n\n' + '*' * 120 + '\n\n')
