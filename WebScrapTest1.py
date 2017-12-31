import urllib.request
response=urllib.request.urlopen('http://www.fishc.com')
html=response.read()
html=html.decode('utf-8')
#驱蚊器无群
print(html)