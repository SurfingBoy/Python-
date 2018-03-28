# -*- coding:utf-8 -*-
import re
import requests
import json
import time
from requests.exceptions import RequestException


def get_one_page(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return '请求失败'
    except RequestException:
        return None


def parse_one_page(html):
    pattern = re.compile(
        '<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a.*?>(\w+)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>.*?integer">(.*?)</i>.*?fraction">(\d*)</i>.*?</dd>',
        re.S)
    results = re.findall(pattern, html)
    for result in results:
        yield {
            '序号': result[0],
            '图片': result[1],
            '影片': result[2],
            '演员': result[3].strip()[3:],
            '上映时间': result[4].strip()[5:],
            '评分': result[5] + result[6]
        }


def write_to_file(text):
    with open('result.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(text, ensure_ascii=False) + '\n')


def main(num):
    url = 'http://maoyan.com/board/4?offset=' + str(num)
    html = get_one_page(url)
    for text in parse_one_page(html):
        print(text)
        write_to_file(text)


if __name__ == '__main__':
    for i in range(10):
        main(num=i * 10)
        time.sleep(1.5)
