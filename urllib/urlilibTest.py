# -*- coding:utf-8 -*-
from urllib import request
from urllib import parse

# with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
#     data=f.read()
#     print('Status:',f.status,f.reason)
#     for k,v in f.getheaders():
#         print('%s:%s'%(k,v))
#     print('Data',data.decode('utf-8'))


# req=request.Request('http://www.douban.com/')
# req.add_header('User-Agent','')

dict1 = {
    'ip': '183.189.199.197'
}
url = 'http://ip.taobao.com/service/getIpInfo.php'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2',
    # 'Host':'hip.taobao.com'
}
data = bytes(parse.urlencode(dict1), encoding='utf-8')
req = request.Request(url=url, data=data, headers=headers)
response = request.urlopen(req)
print(str(response.read(), encoding='utf-8'))
