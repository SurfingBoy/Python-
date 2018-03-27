# -*- coding:utf-8 -*-
import requests
import re

# data={
#     'name':'Bom',
#     'age':'13'
# }
# r=requests.get('http://httpbin.org/get',params=data)
# r1=requests.post('http://httpbin.org/post')
# print(r.json())
# print(r.text)

# 添加headers
# headers={
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
# }
# r=requests.get('https://www.zhihu.com/explore',headers=headers)
# pattern=re.compile('explore-feed.*?question_link.*?>(.*?)</a>',re.S)
# titles=re.findall(pattern,r.text)
# print(titles)

# 保存图片
# r=requests.get('https://github.com/fluidicon.png')
# with open('fluidicon.png','wb') as f:
#     f.write(r.content)

# 上传文件
# files={'file':open('fluidicon.png','rb')}
# r=requests.post('http://httpbin.org/post',files=files)
# print(r.text)

# cookies
# r=requests.get('https://www.baidu.com')
# print(r.cookies)
# for key,value in r.cookies.items():
#     print(key+'='+value)

cookies = ''
jar = requests.cookies.RequestsCookieJar()
headers = {
    'Host': 'www.zhihu.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
}
for cookie in cookies.split(';'):
    key, value = cookie.split('=', 1)
    jar.set(key, value)
r = requests.get('http://www.zhihu.com', cookies=jar, headers=headers)
print(r.text)
