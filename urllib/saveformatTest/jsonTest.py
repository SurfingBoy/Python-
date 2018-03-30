# -*- coding:utf-8 -*-
import json

str = '''
[{
    "name": "炸弹",
    "gender": "male",
    "birthday": "1992-10-18"
}, {
    "name": "Selina",
    "gender": "female",
    "birthday": "1995-10-18"
}]
'''
data = json.loads(str)
print(data)
print(data[1].get('age'))

with open('data.json', 'w', encoding='utf-8') as file:
    file.write(json.dumps(data, indent=2, ensure_ascii=False))  # 缩进2个字符
