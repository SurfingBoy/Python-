# def f1(a,b,c=0,*arg,**kw):
#     print('a=',a,'b=',b,'c=',c,'arg=',arg,'kw=',kw)
# f1(3,4,1,ad=13,qe=12)
# #
# def f1(*num):
#     s=1
#     for x in num:
#         s=s*x
#     print(s)
# f1(2,3,4,5)

# L=list(range(100))
# s=L[0:-2]
# print(L)

#----------列表--------------#
# def findMinAndMax(l):
#     x=[]
#     if l == x:
#         print((None,None))
#         return
#     else:
#         max=min=l[0]
#         # for i in range(len(l)):
#         #     if l[i]>max:
#         #         max=l[i]
#         #     if l[i]<min:
#         #         min=l[i]
#         for s in l:
#             if s>max:
#                 max=s
#             if s<min:
#                 min=s
#         print ((min,max))
# findMinAndMax([3,1,4,6,8,6])
#----------列表--------------#

#---------列表生成式-------------#
# L1 = ['Hello', 'World', 18, 'Apple', None]
# L2=[s.lower() for s in L1 if isinstance(s,str)==1]
# print(L2)
#---------列表生成式-------------#

#---------生成器generator-------------#
# g=(x*x for x in range(10))
# for n in g:
#     print(n)
#---------生成器generator-------------#


#---------杨辉三角-------------#
# def triangles():
#     L = [1]
#     while True:
#         yield L
#         L.append(0)
#         L = [L[i - 1] + L[i] for i in range(len(L))]
# n = 0
# results = []
# for t in triangles():
#     print(t)
#     results.append(t)
#     n = n + 1
#     if n == 3:
#         break
#---------杨辉三角-------------#

#-------------高阶函数---------#
# def add(x, y, f):
#     return f(x) + f(y)
#
# print(add(-5, 6, abs))
#-------------高阶函数---------#


#-------------map---------#
# def normalize(s):
#     s1=s[0:1].upper()
#     s2=s[1:].lower()
#     return s1+s2
# L1 = ['adam', 'LISA', 'barT']
# L2 = list(map(normalize, L1))
# print(L2)
#-------------map---------#


#-------------filter筛选素数---------#
# def _odd_iter():
#     n=1
#     while True:
#         n=n+2
#         yield n
# def _not_divisible(n):
#     return lambda x:x%n>0
# def primes():
#     yield 2
#     it=_odd_iter()
#     while True:
#         n=next(it)
#         yield n
#         it=filter(_not_divisible(n),it)
# l=[]
# for n in primes():
#     if n<100:
#         l.append(n)
#     else:
#         break
# print(l)
#-------------filter筛选素数---------#


#-------------filter筛选回数---------#
    #-------方法一--------------#
# def is_palindrome(n):
#     return str(n)==str(n)[::-1]
    #-------方法一--------------#
    #-------方法二--------------#
# def is_palindrome(n):
#     s,m=n,0
#     while s:
#         m=m*10+s%10
#         s=s//10
#     return (m==n)
#     #-------方法二--------------#
# l=list(filter(is_palindrome,range(1,200)))
# print(l)
#-------------filter筛选回数---------#

#-------------sorted高阶应用---------#
# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# def by_name(t):
#     s=t[0]
#     return s
# def by_score(t):
#     s=t[1]
#     return s
# L1=sorted(L,key=by_name)
# L2=sorted(L,key=by_score,reverse=True)
# print(L1)
# print(L2)
#-------------sorted高阶应用---------#


#-------------高阶函数》返回函数---------#

#####--------例子一------########
# def lazy_sum(*arg):
#     def sum():
#         ax=0
#         for n in arg:
#             ax=ax+n
#         return ax
#     return sum
# f=lazy_sum(3,7,2,6,8,9)
# print(f())
#####--------例子一------########

#####--------例子二------########
# def count():
#     def f(j):
#         def g():
#             return j*j
#         return g
#     fs=[]
#     for i in range(1,4):
#         fs.append(f(i))
#     return fs
# f1,f2,f3=count()
# print(f1(),f2(),f3())
#####--------例子二------########
# def count():
#     fs = []
#     for i in range(1, 4):
#         def f():
#              return i*i
#         fs.append(f)
#     return fs
#
# f1, f2, f3 = count()
# print(f1(),f2(),f3())
#####--------测试------########
# def createCounter():
#     def counter(i):
#         def c():
#             return i
#         return c
#     j=1
#     while True:
#         j=j+1
#         counter(j)
#     return x
# f1,f2,f3=createCounter()
# print(f1,f2,f3)
#####--------测试------########
#-------------高阶函数》返回函数---------#

##-------------装饰器(decorator)------------#
# import functools
# def log(text1,text2): #---自定义log
#     def decorate(func):
#         @functools.wraps(func)  #----将原始函数的__name__等属性复制到wapper()函数中
#         def wapper(*args,**kw):
#             print('%s  call '%text1)
#             out=func(*args,**kw)
#             print('%s  call '%text2)
#             return out
#         return wapper
#     return decorate
# @log('begin','end')
# def now(time):
#     print(time)
# print(now('2016'))
# print(now.__name__)
#--------------------运行时间-------------------
# import time
# import functools
# def metric(func):
#     @functools.wraps(func)
#     def wapper(*arg,**kw):
#         start=time.time()
#         f=func(*arg,**kw)
#         end=time.time()
#         print('%s()运行了%fs'%(func.__name__,(end-start)))
#         return f
#     return wapper
# @metric
# def fast(x,y):
#     time.sleep(0.012)
#     return x+y
# @metric
# def fast2(x,y,z):
#     time.sleep(0.012)
#     return x*y*z
# print(fast(3,5))
# print('fast.__name__=',fast.__name__)
# print('\n')
# print(fast2(5,9,3))
# print('fast2.__name__=',fast2.__name__)
#--------------------运行时间-------------------
##-------------装饰器(decorator)------------#

##-------------偏函数------------#
# import functools
# int2=functools.partial(int,base=2)
# print(int2('110011'))
##-------------偏函数------------#


#--------------面向对象---------#
# class Student(object):
#     def __init__(self,name,gender):
#         self.__name=name
#         self.__gender=gender
#     def getName(self):
#         return self.__name
#     def getGender(self):
#         return self.__gender
#     def setName(self,name):
#         self.__name=name
#     def setGender(self,gender):
#         self.__gender=gender
# bart=Student('Bart','male')
# bart.setGender('female')
# print(bart.getName(),bart.getGender())
# print(dir(Student))
#-----------------------
# class Student():
#     count=0
#     def __init__(self,name):
#         Student.count+=1
#         self.x=name
# bar1=Student('Bart')
# print(Student.count)
#-----------------------
#--------------面向对象---------#

#-------------面向对象高级编程----------
#--------[__iter__方法]------------
# class Fib(object):
#     def __init__(self):
#         self.a,self.b=0,1
#     def __iter__(self):
#         return self   #实例本身就是迭代对象
#     def __next__(self):
#         self.a,self.b=self.b,self.a+self.b
#         if self.a>100:
#             raise StopIteration()
#         return self.a
# for n in Fib():
#     print(n)
#--------[__getitem__方法]--------
# class Fib(object):
#     def __getitem__(self, n):
#         if isinstance(n,int): #n是索引
#             a,b=1,1
#             for x in range(n):
#                 a,b=b,a+b
#             return a
#         if isinstance(n,slice): #n是切片
#             start=n.start
#             stop=n.stop
#             if start is None:
#                 start=0
#             a,b=1,1
#             L=[]
#             for x in range(stop):
#                 if x>=start:
#                     L.append(a)
#                 a,b=b,a+b
#             return L
# f=Fib()
# print(f[6])
#-------------面向对象高级编程----------
# from functools import reduce
#
# def str2num(s):
#     return float(s)
#
# def calc(exp):
#     ss = exp.split('+')
#     ns = map(str2num, ss)
#     return reduce(lambda n, x: x+n, ns)
#
# def main():
#     r = calc('100 + 200 + 345')
#     print('100 + 200 + 345 =', r)
#     r = calc('99 + 88 + 7.6')
#     print('99 + 88 + 7.6 =', r)
#
# main()

#------------------file操作-------------------
# with open('README.md','r',encoding='utf-8',errors='ignore') as f:
#     print(f.read())


# fpath = r'C:\Windows\system.ini'
# with open(fpath, 'r') as f:
#     for line in f.readlines():
#         print(line)
#------------------file操作-------------------

#--------------BytesIo和StringIo--------------------
# from io import StringIO
# from io import BytesIO
# f=BytesIO()
# f.write('在中国'.encode('gbk'))
# print(f.write('在中国'.encode('gbk')))
# print(f.getvalue())

# f=StringIO()
# f.write('Hello')
# f.write(' ')
# f.write('world')
# print(f.getvalue())
#--------------BytesIo和StringIo--------------------

#----------------------json---------------------
# import json
# # d={'name':'小明','age':18}
# # d1=dict(name='liming',age=18)
# # j=json.dumps(d)
# # print(j)
#
# class Student(object):
#     def __init__(self,name,age,score):
#         self.n=name
#         self.a=age
#         self.s=score
# def student2dict(std):
#     return {
#         'name':std.n,
#         'age':std.a,
#         'score':std.s
#     }
# s=Student('张三',18,90)
# # print(json.dumps(s,default=student2dict))
# print(json.dumps(s,default=lambda obj:obj.__dict__,ensure_ascii=False))
#----------------------json---------------------

#----------------------进程----------------------
#-----------multiprocessing-----------
# from multiprocessing import Process
# import os
# def run_proc(name):
#     print('Run child process %s(%s)...'%(name,os.getpid()))
# if __name__ == '__main__':
#     print('Parent process %s'%os.getpid())
#     p=Process(target=run_proc,args=('test',))
#     print('Child process will start')
#     p.start()
#     p.join()
#     print('Child process end')
#-----------multiprocessing-----------

#--------------Pool---------------
# from multiprocessing import Pool
# import os,time,random
# def long_time_task(name):
#     print('Run task %s(%s)'%(name,os.getpid()))
#     start=time.time()
#     time.sleep(random.random()*10)
#     end=time.time()
#     print('Task %s run %0.2f seconds'%(name,(end-start)))
# if __name__ == '__main__':
#     print('Parent process %s'%os.getpid())
#     p=Pool()
#     for i in range(5):
#         p.apply_async(long_time_task,args=(i,))
#     print('Waiting for all subprocesses done...')
#     p.close()
#     p.join()
#     print('all subprocesses done')
#--------------Pool---------------

#---------------进程间通信----------------
# from multiprocessing import Process,Queue
# import os,time,random
#
# def write(q):
#     print("process to write: %s"%os.getpid())
#     for value in ['A','B','C']:
#         print('Put %s to queue..'%value)
#         q.put(value)
#         time.sleep(random.random())
# def read(q):
#     print('Process to read:%s'%os.getpid())
#     while True:
#         value=q.get(True)
#         print('Get %s from queue'%value)
# if __name__ == '__main__':
#     q=Queue()
#     pw=Process(target=write,args=(q,))
#     pr=Process(target=read,args=(q,))
#     pw.start()
#     pr.start()
#     #等待pw进程结束
#     pw.join()
#     #pr进程里是死循环，无法等待其结束，只能强行终止
#     pr.terminate()
#---------------进程间通信----------------
#----------------------进程----------------------