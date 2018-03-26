# -*- coding:utf-8 -*-
from urllib import request
from urllib import parse
from urllib import error
import socket

# with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
#     data=f.read()
#     print('Status:',f.status,f.reason)
#     for k,v in f.getheaders():
#         print('%s:%s'%(k,v))
#     print('Data',data.decode('utf-8'))


# dict1 = {
#     'ip': '183.189.199.197'
# }
# url1 = 'http://ip.taobao.com/service/getIpInfo.php'
# url='http://httpbin.org/post'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2',
#     'Host':'httpbin.org'
# }
# try:
#     data = bytes(parse.urlencode(dict1), encoding='utf-8')
#     req = request.Request(url=url, data=data, headers=headers,method='POST')
#     #req.add_header(headers)
#     response = request.urlopen(req, timeout=1)
# except error.URLError as e:
#     if isinstance(e.reason,socket.timeout):
#         print('TIME OUT')
# print(str(response.read(), encoding='utf-8'))

# 登录
# from urllib.request import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, build_opener
# from urllib.error import URLError
#
# username = 'username'
# passsword = 'password'
# url = 'https://jenkins.labradors.work/login?from=%2F'
# p = HTTPPasswordMgrWithDefaultRealm()
# p.add_password(None, url, username, passsword)
# auth_handler = HTTPBasicAuthHandler(p)
# opener = build_opener(auth_handler)
#
# try:
#     result = opener.open(url)
#     html = result.read().decode('utf-8')
#     print(html)
# except URLError as e:
#     print(e.reason)

# #代理
# from urllib.error import URLError
# from urllib.request import ProxyHandler,build_opener
#
# proxy_handler=ProxyHandler({
#     'http':'222.208.76.205',
#     'http':'115.218.123.177'
# })
# opener=build_opener(proxy_handler)
# try:
#     response=opener.open('https://www.baidu.com')
#     print(response.read().decode('utf-8'))
# except URLError as e:
#     print(e.reason)

# cookies
# import http.cookiejar, urllib.request
#
# cookie = http.cookiejar.CookieJar()
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open('https://www.baidu.com')
# for item in cookie:
#     print(item.name + '=' + item.value)

# #将cookie保存到文件
# import  http.cookiejar,urllib.request
# filename='cookies.txt'
# #声明MozillaCookieJar对象实例保存cookie,然后保存到文件
# cookie=http.cookiejar.MozillaCookieJar(filename)     #LWPCookieJar(cookies2)
# #创建cookie处理器
# handler=urllib.request.HTTPCookieProcessor(cookie)
# #创建opener
# opener=urllib.request.build_opener(handler)
# response=opener.open('https://www.baidu.com')
# cookie.save(ignore_discard=True,ignore_expires=True)

# #从文件读取cookie
# import http.cookiejar,urllib.request
# #创建MozillaCookieJar对象
# cookie=http.cookiejar.MozillaCookieJar()
# #从文件读取cookie内容到变量
# cookie.load('cookies.txt',ignore_discard=True,ignore_expires=True)
# handler=urllib.request.HTTPCookieProcessor(cookie)
# opener=urllib.request.build_opener(handler)
# response=opener.open('https://www.baidu.com')
# print(response.read().decode('utf-8'))

from urllib.parse import urlparse
from urllib.parse import urlunparse
from urllib.parse import urlsplit
from urllib.parse import urlunsplit
from urllib.parse import urljoin

result = urlparse('http://www.baidu.com/index.html;user?id=5#comment', scheme='https')
print('result=', type(result), result)

data = ['http', 'www.baidu.com', 'index.html', 'user', 'id=6', 'comment']
print('data=', urlunparse(data))

result1 = urlsplit('http://www.baidu.com/index.html;user?id=5#comment')
print('result1=', result1)

data1 = ['http', 'www.baidu.com', 'index.html', 'id=6', 'comment']
print('data1=', urlunsplit(data1))
