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

**登录**

发送请求使用OpenerDirector

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
**代理**

    from urllib.error import URLError
    from urllib.request import ProxyHandler,build_opener

    proxy_handler=ProxyHandler({
        'http':'222.208.76.205',
        'http':'115.218.123.177'
    })
    opener=build_opener(proxy_handler)
    try:
        response=opener.open('https://www.baidu.com')
        print(response.read().decode('utf-8'))
    except URLError as e:
        print(e.reason)
***
**Cookies**

    import http.cookiejar,urllib.request

    cookie=http.cookiejar.CookieJar()
    handler=urllib.request.HTTPCookieProcessor(cookie)
    opener=urllib.request.build_opener(handler)
    response=opener.open('https://www.baidu.com')
    for item in cookie:
        print(item.name+'='+item.value)
robotparser
-
* set_url():用来设置robots.txt文件的链接。如果在创建RobotFileParser对象时传入了链
接，那么就不需要再使用这个方法设置了
* read():读取robots.txt文件并进行分析。注意，这个方法执行一个读取和分析操作，如果不
调用这个方法，接下来的判断都会为False，所以一定记得调用这个方法。这个方法不会返回任何
内容，但是执行了读取操作。
* parse():用来解析robots.txt文件，传入的参数是robots.txt某些行的内容，它会按照
robots.txt的语法规则来分析这些内容
* can_fetch():该方法传入两个参数，第一个是User-agent，第二个是要抓取的URL。返回的
内容是该搜索引擎是否可以抓取这个URL，返回结果是True或False。
* mtime():返回的是上次抓取和分析robots.txt的时间，这对于长时间分析和抓取的搜索爬虫
是很有必要的，你可能需要定期检查来抓取最新的robots.txt。
* modified():它同样对长时间分析和抓取的搜索爬虫很有帮助，将当前时间设置为上次抓取和
分析robots.txt的时间。


  [参照：廖雪峰的官方网站](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000)

  [参照掘金文章：Pythonurllib使用(一)](https://juejin.im/entry/5ab441996fb9a028b547cddc?utm_source=gold_browser_extension)      
  [参照掘金文章：【Python3网络爬虫开发实战】3.1.4-分析Robots协议](https://juejin.im/post/5aa9f5996fb9a028d70053a9)
  
  [菜鸟教程](http://www.runoob.com/python/python-files-io.html)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

