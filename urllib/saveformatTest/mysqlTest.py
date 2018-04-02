# -*- coding:utf-8 -*-
import pymysql

##连接数据库
# db=pymysql.connect(host='localhost',user='root',password='123456',port=3306)
# cursor=db.cursor()
# cursor.execute('select version()')
# data=cursor.fetchone()
# print('Database version:',data)
# cursor.execute('create database spider default CHARACTER  set utf8')
# db.close()

##创建表
# db=pymysql.connect(host='localhost',user='root',password='123456',port=3306,db='spider')
# cursor=db.cursor()
# sql='create table if not exists student (id VARCHAR (255) Not NULL ,name VARCHAR (255) NOT NULL ,age INT NOT NULL ,PRIMARY KEY (id))'
# cursor.execute(sql)
# db.close()

##插入数据
# id='1001'
# name='daming'
# age=21
# db=pymysql.connect(host='localhost',user='root',password='123456',port=3306,db='spider')
# cursor=db.cursor()
# sql='insert into student(id,name,age) VALUES (%s,%s,%s)'
# try:
#     cursor.execute(sql,(id,name,age))
#     db.commit()
# except :
#     db.rollback()
# db.close()


##插入数据(可扩展)
# db=pymysql.connect(host='localhost',user='root',password='123456',port=3306,db='spider')
# cursor=db.cursor()
# data={
#     'id':'1002',
#     'name':'Bom',
#     'age':24
# }
# table='student'
# keys=','.join(data.keys())
# values=','.join(['%s']*len(data))
# sql='insert into {table}({keys}) VALUES ({values})'.format(table=table,keys=keys,values=values)
# try:
#     if cursor.execute(sql,tuple(data.values())):
#         print('Successful')
#         db.commit()
# except:
#     print('Failed')
#     db.rollback()
# db.close()


##更新(数据存在，则更新;数据不存在，则插入数据)
###### INSERT INTO students(id, name, age) VALUES (%s, %s, %s) ON DUPLICATE KEY UPDATE id = %s, name = %s, age = %s
# db=pymysql.connect(host='localhost',user='root',password='123456',port=3306,db='spider')
# cursor=db.cursor()
# data={
#     'id':'1002',
#     'name':'Bom',
#     'age':12
# }
# table='student'
# keys=','.join(data.keys())
# values=','.join(['%s']*len(data))
# sql='insert into {table}({keys}) VALUES ({values}) ON DUPLICATE KEY UPDATE '.format(table=table,keys=keys,values=values)
# update=','.join(['{key}=%s'.format(key=key) for key in data])
# sql+=update
# try:
#     if cursor.execute(sql,tuple(data.values())*2):
#         print('Successful')
#         db.commit()
# except:
#     print('Failed')
#     db.rollback()
# db.close()


# sql='update student set age=%s where id=%s'
# try:
#     cursor.execute(sql,(12,'1002'))
#     db.commit()
# except:
#     db.rollback()
# db.close()


## 删除数据
# db=pymysql.connect(host='localhost',user='root',password='123456',port=3306,db='spider')
# cursor=db.cursor()
# table='student'
# condition='age>30'
# sql='delete from {table} where {condition}'.format(table=table,condition=condition)
# try:
#     cursor.execute(sql)
#     db.commit()
#     print('Successful')
# except:
#     db.rollback()
#     print('Failed')
# db.close()


##查询数据
db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='spider')
cursor = db.cursor()
sql = 'select *from student where age>10'
try:
    cursor.execute(sql)
    print('Count:', cursor.rowcount)
    row = cursor.fetchone()
    while row:
        print('Row:', row)
        row = cursor.fetchone()
except:
    print('Error')
