import urllib.request
import urllib.parse
import json
url='http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule' \
    '&smartresult=ugc&sessionFrom=http://www.youdao.com/'
content=input('输入要翻译的内容：')
head={'Referer':'fanyi.youdao.com',
      'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
      'Chrome/63.0.3239.108 Safari/537.36X-Requested-With:XMLHttpRequest'}
data={}
data['i']=content
data['type']='AUTO'
#data['smartresult']='dict'
#data['client']='fanyideskweb'
data['doctype']='json'
data['version']='2.1'
#data['keyfrom']='fanyi.web'
data['action']='FY_BY_CLICKBUTTON'
data['typoResult']='true'
data=urllib.parse.urlencode(data).encode('utf-8')
response=urllib.request.urlopen(url,data,head)
html=response.read().decode('utf-8')
target=json.loads(html)
print('翻译结果：%s'%(target['translateResult'][0][0]['tgt']))


