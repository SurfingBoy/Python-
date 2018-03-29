# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
<div class="panel-body">
        <ul class="list" id="list-1">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
"""
soup = BeautifulSoup(html, 'lxml')
# print(soup.prettify())
# #节点名称
# print('节点名称：',soup.title.name)
# #节点内容
# print('节点内容：',soup.title.string)
# #节点属性
# print('节点属性：',soup.p.attrs)
# #节点属性值
# print('节点属性值：',soup.p.attrs['name'])
# print('节点属性值：',soup.p['class'])

# print(soup.p.children)
# for i,child in enumerate(soup.p.children):
#     print(i,child)

# print(soup.p.descendants)
# for i,child in enumerate(soup.p.descendants):
#     print(i,child)

# 父节点
# print(soup.a.parent)
# 下一个兄弟节点
# print(soup.a.next_sibling)
# 上一个兄弟节点
# print(soup.a.previous_sibling)

# 根据节点名查找节点
# for ul in soup.find_all(name='ul'):
#     for li in ul.find_all(name='li'):
#         print(li.string)

# 节点属性查找
# for ul in soup.find_all(id='list'):  # class_
#     for li in ul.find_all(name='li'):
#         print(li.string)
