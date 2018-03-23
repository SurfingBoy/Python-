# -*- coding:utf-8 -*-
# from urllib import request
# from urllib import parse

# with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
#     data=f.read()
#     print('Status:',f.status,f.reason)
#     for k,v in f.getheaders():
#         print('%s:%s'%(k,v))
#     print('Data',data.decode('utf-8'))


# dict1 = {
#     'ip': '183.189.199.197'
# }
# url = 'http://ip.taobao.com/service/getIpInfo.php'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2',
#     # 'Host':'hip.taobao.com'
# }
# data = bytes(parse.urlencode(dict1), encoding='utf-8')
# req = request.Request(url=url, data=data, headers=headers)
# response = request.urlopen(req)
# print(str(response.read(), encoding='utf-8'))

from urllib.request import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, build_opener
from urllib.error import URLError

username = 'username'
passsword = 'password'
url = 'https://jenkins.labradors.work/login?from=%2F'
p = HTTPPasswordMgrWithDefaultRealm()
p.add_password(None, url, username, passsword)
auth_handler = HTTPBasicAuthHandler(p)
opener = build_opener(auth_handler)

try:
    result = opener.open(url)
    html = result.read().decode('utf-8')
    print(html)
except URLError as e:
    print(e.reason)
