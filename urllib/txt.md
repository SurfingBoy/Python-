urllib四个模块
-
* request
* error
* parse
* robotparser
***
    with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
    data=f.read()
    print('Status:',f.status,f.reason)
    for k,v in f.getheaders():
        print('%s:%s'%(k,v))
    print('Data',data.decode('utf-8'))
***
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
***
Handler
-
* HTTPDefaultErrorHandler：处理HTTP错误
* HTTPRedirectHandler：处理重定向
* HTTPCookieProcessor：处理cookie
* ProxyHandler：处理代理
* HTTPPasswordMgr：管理密码
* HTTPBasicAuthHandler：管理认证

发送请求使用OpenerDirector
***
    from urllib.request import HTTPPasswordMgrWithDefaultRealm,HTTPBasicAuthHandler,build_opener
    from urllib.error import URLError

    username='username'
    passsword='password'
    url='https://jenkins.labradors.work/login?from=%2F'
    p=HTTPPasswordMgrWithDefaultRealm()
    p.add_password(None,url,username,passsword)
    auth_handler=HTTPBasicAuthHandler(p)
    opener=build_opener(auth_handler)

    try:
        result=opener.open(url)
        html=result.read().decode('utf-8')
        print(html)
    except URLError as e:
        print(e.reason)
***
  [参照：廖雪峰的官方网站](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000)
  
  [参照掘金文章：Python urllib使用(一)](https://juejin.im/entry/5ab441996fb9a028b547cddc?utm_source=gold_browser_extension)
    
    
    
    
    
    
    

