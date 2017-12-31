import urllib.request
response=urllib.request.urlopen('http://placekitten.com/g/400/400')  #获取猫的图片
cat_img=response.read()
with open('400.jpg','wb') as f:
    f.write(cat_img)