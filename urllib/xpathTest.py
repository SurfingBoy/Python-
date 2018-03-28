# -*- coding:utf-8 -*-
from lxml import etree

text = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a>
         
         <li class="li li-first"><a href="link.html">six item</a></li>
     </ul>
 </div>
'''
# 读取text
html = etree.HTML(text)
# 读取文件
# html1=etree.parse('./test.html',etree.HTMLParser())
result = html.xpath('//li[@class="item-inactive"]/a/text()')
print('节点内容：', result)
result1 = html.xpath('//a[@href="link5.html"]/../@class')
print('父节点属性值： ', result1)
result2 = html.xpath('//li/a/@href')
print('属性值：', result2)
result3 = html.xpath('//li[contains(@class,"li")]/a/text()')
print('属性多值匹配：', result3)
# str=etree.tostring(html)
# print(str.decode('utf-8'))
