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

# Cookies
# ------------------------------
# r=requests.get('https://www.baidu.com')
# print(r.cookies)
# for key,value in r.cookies.items():
#     print(key+'='+value)

# cookies = ''
# jar = requests.cookies.RequestsCookieJar()
# headers = {
#     'Host': 'www.zhihu.com',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
# }
# for cookie in cookies.split(';'):
#     key, value = cookie.split('=', 1)
#     jar.set(key, value)
# r = requests.get('http://www.zhihu.com', cookies=jar, headers=headers)
# print(r.text)
# ------------------------------

# 会话Session
# s=requests.Session()
# s.get('http://httpbin.org/cookies/set/number/Session123')
# r=s.get('http://httpbin.org/cookies')
# print(r.text)

# SSL
# from requests.packages import urllib3
# urllib3.disable_warnings()   #忽略警告
# response=requests.get('https://www.12306.cn',verify=False) #忽略证书
# response.encoding='utf-8'
# print(response.text)

# 代理
# proxies={
#     'http':'http://192.168.0.1'
# }
# r=requests.get('http://www.baidu.com',proxies=proxies)


# 身份认证
# from requests.auth import HTTPBasicAuth
# r=requests.get('http://localhost:8080',auth=HTTPBasicAuth('username','password')) #HTTPBasicAuth可以省略
# print(r.status_code)


# Prepared Request
# from requests import Request,Session
# url='http://httpbin.org/post'
# data={
#     'name':'germey'
# }
# headers={
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
# }
# s=Session()
# req=Request('POST',url,data=data,headers=headers)
# prepare=s.prepare_request(req)
# response=s.send(prepare)
# print(response.text)
