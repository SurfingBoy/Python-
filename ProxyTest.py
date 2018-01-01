import urllib.request
import random
url='http://www.whatismyip.com.tw'
print('添加代理IP地址(IP:端口号),多个IP地址用英文分号隔开!')
iplist=input('输入IP地址:').split(';')
while True:
    ip=random.choice(iplist)
    proxy_support=urllib.request.ProxyHandler({'http':ip})
    opener=urllib.request.build_opener(proxy_support)
    opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
          'Chrome/63.0.3239.108 Safari/537.36X-Requested-With:XMLHttpRequest')]
    urllib.request.install_opener(opener)# 将代理安装进默认程序
    try:
        print('正在使用%s访问..'%ip)
        response=urllib.request.urlopen(url)
    except :
        print('访问出错')
    else:
        print('访问成功')
    if input('是否继续访问(Y/N)')=='N':
        break
# html=response.read().decode('utf-8')
# print(html)
