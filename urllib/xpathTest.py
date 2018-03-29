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
         
         <li class="li le-first"><a href="link.html">属性多值</a></li>
         
         <li class="la le-first" name="item"><a href="link.html">多属性</a></li>
     </ul>
 </div>
'''
# 读取text
html = etree.HTML(text)
# 读取文件
# html1=etree.parse('./test.html',etree.HTMLParser())
# 节点内容
result = html.xpath('//li[@class="item-inactive"]/a/text()')
print('节点内容：', result)
#父节点属性值
result1 = html.xpath('//a[@href="link5.html"]/../@class')
print('父节点属性值： ', result1)
#属性值
result2 = html.xpath('//li/a/@href')
print('属性值：', result2)
#属性多值匹配
result3 = html.xpath('//li[contains(@class,"li")]/a/text()')
print('属性多值匹配：', result3)
# 多属性匹配
result4 = html.xpath('//li[contains(@class,"la") and @name="item"]/a/text()')
print('多属性匹配', result4)
# 序号匹配
#####返回第一个节点
result5 = html.xpath('//li[1]/a/text()')
print('第一个节点：', result5)
#####返回第二个节点
result6 = html.xpath('//li[last()]/a/text()')
print('最后一个节点：', result6)
#####返回位置小于3的节点
result7 = html.xpath('//li[position()<3]/a/text()')
print('位置小于3的节点：', result7)
#####返回倒数第二个节点
result8 = html.xpath('//li[last()-1]/a/text()')
print('倒数第二个节点：', result8)
# str=etree.tostring(html)
# print(str.decode('utf-8'))
