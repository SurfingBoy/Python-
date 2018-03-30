# -*- coding:utf-8 -*-
import csv
import pandas

with open('data.csv', 'w', encoding='utf-8') as file:
    # writer=csv.writer(file)
    # writer.writerow(['id','name','age'])
    # writer.writerow(['1','Bom','14'])
    # writer.writerow(['2','张彪','21'])
    fieldnames = ['id', 'name', 'age']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'id': '1', 'name': 'Bom', 'age': '14'})
    writer.writerow({'id': '2', 'name': '张三', 'age': '21'})

with open('data.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

df = pandas.read_csv('data.csv')
print(df)
