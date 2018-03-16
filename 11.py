# def fact(n):
#     return fact2(n,1)
# def fact2(n,result):
#     if n==1:
#         return result
#     return fact2(n-1,n*result)
# r=fact(100)
# print(r)
# def move(n,a,b,c):
#     if n==1:
#         print(a,'--->',c)
#     else:move(n-1,a,c,b),move(1,a,b,c),move(n-1,b,a,c)
# move(3,'A','B','C')
#
# def abc(s):
#     if s=='':
#         return '空值'
#     if s[0] == ' ':
#         return abc(s[1:])
#     elif s[-1] == ' ':
#         return abc(s[:-1])
#     else:
#         return s
# s=abc(' 23232 ')
# s1=('   qewewd    ')
# print(s1)
# print(s)

# from collections import Iterable
#
# print(isinstance('abs',Iterable))
#
# for i,v in enumerate(['wew','sf','dfdf']):
#     print(i,v)

# def findMinAndMax(L):
#     if isinstance(L,list):
#         min = max = L[0]
#         for i,v in enumerate(L):
#             if L[i]>max:
#                 max=L[i]
#             if L[i]<min:
#                 min=L[i]
#         return min,max
# L=[3,7,2,8,1]
# r=findMinAndMax(L)
# print(r)

# import os
# l=[x*x for x in range(1,11) if x%2==0]
# l1=[m+n for m in "ABC" for n in "123"]
# l2=[d for d in os.listdir('.')]
# print(l)
# print(l1)
# print(l2)

# L1 = ['Hello', 'World', 18, 'Apple', None]
# L2=[]
# for x in L1:
#     if isinstance(x,str):
#         x=x.lower()
#     L2.append(x)
# print(L2)
# L3=[s.lower() for s in L1 if isinstance(s,str)]
# print(L3)

# g=(x*x for x in range(10))
# for n in g:
#     print(n)

# def fib(max):
#     n,a,b=0,0,1
#     while n<max:
#         # print(b)
#         yield b
#         a,b=b,a+b
#         n+=1
# for x in fib(6):
#     print(x)

# def triangles():
#     L=[1]
#     while 1:
#         yield L
#         L=[1]+[L[n]+L[n+1] for n in range(len(L)-1)]+[1]
#
# n = 0
# for t in triangles():
#     print(t)
#     n = n + 1
#     if n == 10:
#         break

# def add(x, y, f):
#     return f(x) + f(y)
#
# print(add(-5, 6, abs))

# s='wewe'
# s.upper()
# def normalize(name):
#     name=name[0].upper()+name[1:].lower()
#     return name
# L1 = ['adam', 'LISA', 'barT']
# L2 = list(map(normalize, L1))
# print(L2)

# from functools import reduce
# DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
# def str2int(s):
#     def char2num(s):
#         return DIGITS[s]
#     return reduce(lambda x,y:x*10+y, list(map(char2num, s)))
#
# x=str2int('3432')
# print(x)

# from functools import reduce
# def prod(L):
#     def fn(x,y):
#         return x*y
#     return reduce(fn,L)
# L=[3,5,7,9]
# s=prod(L)
# print(s)


# from functools import reduce
# # DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,'.':'.'}
# def str2float(s):
#     # def fn(x,y):
#     #     return x*10+y
#     # def char2num(s):
#     #     return DIGITS[s]
#     int_part, dec_part = s.split('.')
#     return reduce(lambda x, y: 10 * x + y, map(int, int_part)) + \
#            reduce(lambda x, y: 10 * x + y, map(int, dec_part)) * 10 ** (-len(dec_part))
#
# f=str2float('2242.4534')
# print(f)

# def is_palindrome(n):
#     return str(n)==str(n)[::-1]
# output = list(filter(is_palindrome, range(1, 1000)))
# print(output)

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
# for n in primes():
#     if n<100:
#         print(n)
#     else:
#         break

# L = [('Bob', 75), ('adam', 92), ('Bart', 66), ('Lisa', 88)]
# def by_name(t):
#     return t[0].lower()
# L2=sorted(L,key=by_name)
# print(L2)


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
# print(f3())


# def createCounter():
#     s=[0]
#     def counter():
#         s[0]=s[0]+1
#         return s[0]
#     return counter
# counterA=createCounter()
# print(counterA(),counterA(),counterA())

# def createCounter():
#     s=0
#     def counter():
#         nonlocal s
#         s=s+1
#         return s
#     return counter
# counterB=createCounter()
# print(counterB(),counterB(),counterB())

# def createCounter():
#     def g():
#         s=0
#         while True:
#             s=s+1
#             yield s
#     it=g()
#     def counter():
#         return next(it)
#     return counter
# counterC=createCounter()
# print(counterC(),counterC(),counterC())

# L=list(filter(lambda x:x%2==0,range(1,20)))
# print(L)

# def compute(x,y,op):
#     if op=='+':return x+y
#     elif op=='*':return x*y
#     elif op=='-':return x-y
#     else:return x/y if y else None
#
# def exp(p,iter=0):
#     from itertools import permutations
#     if len(p)==1:return [(p[0],str(p[0]))]
#     operation = ['+','-','*','/']
#     ret = []
#     p = permutations(p) if iter==0 else [p]
#     for array_n in p:
#         #print(array_n)
#         for num in range(1,len(array_n)):
#             ret1 = exp(array_n[:num],iter+1)
#             ret2 = exp(array_n[num:],iter+1)
#             for op in operation:
#                 for va1,expression in ret1:
#                     if va1==None:continue
#                     for va2,expression2 in ret2:
#                         if va2==None:continue
#                         combined_exp = '{}{}' if expression.isalnum() else '({}){}'
#                         combined_exp += '{}' if expression2.isalnum() else '({})'
#                         new_val = compute(va1,va2,op)
#                         ret.append((new_val,combined_exp.format(expression,op,expression2)))
#                         if iter==0 and new_val==24:
#                             return ''.join(e+'\n' for x,e in ret if x==24)
#     return ret
# print(exp([4,7,10,12]))

# import functools
# import time
# def log(func):
#     @functools.wraps(func)
#     def wapper(*args,**kw):
#         print('kaishiqian')
#         t1=time.time()
#         f=func(*args,**kw)
#         t2=time.time()
#         print('%s()运行时间%s'%(func.__name__,(t2-t1)))
#         return f
#     return wapper()
# @log
# def now():
#     time.sleep(0.1)
#     print('wrwerw')

# import time
# import functools
# def log(arg):
#     def inner_log(text='call'):
#         def decorator(func):
#             @functools.wraps(func)
#             def wapper(*arg,**kw):
#                 s1=time.time()
#                 f=func(*arg,**kw)
#                 s2=time.time()
#                 print('%s,%s()运行了%s'%(text,func.__name__,(s2-s1)))
#                 return f
#             return wapper
#         return decorator
#     if callable(arg):
#         return inner_log()(arg)
#     return inner_log(arg)
# @log('execute')
# def now():
#     time.sleep(0.2)
#     print('哈哈哈哈')
# f=now()

# class Student():
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#
#     def get_grade(self):
#         if self.score >= 90:
#             return 'A'
#         elif self.score >= 60:
#             return 'B'
#         else:
#             return 'C'
# lisa = Student('Lisa', 99)
# bart = Student('Bart', 59)
# print(lisa.name, lisa.get_grade())
# print(bart.name, bart.get_grade())

# class Student():
#     def __init__(self,name,gender):
#         self.name=name
#         self.__gender=gender
#     def getGender(self):
#         return self.__gender
#     def setGender(self,gender):
#         if gender=='male' or gender=='female':
#             self.__gender = gender
#         else:
#             raise ValueError('错误:%s'%gender)
# x=Student('hhh','male')
# print(x.getGender())
# x.setGender('female')
# print(x.getGender())
# x.setGender('KKK')
# print(x.getGender())

# class myClass(object):
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def add(self):
#         return self.x+self.y
#     def sub(self):
#         return self.x-self.y
#     def pow(self):
#         return self.x*self.y
#     def div(self):
#         return self.x/self.y
# def run(x,y):
#     my = myClass(x, y)
#     while True:
#         inp = input('method:')
#         if hasattr(my,inp):
#             func=getattr(my,inp)
#             print(func())
#         else:
#             setattr(my,inp,lambda x:x+1)
#             func=getattr(my,inp)
#             print(func(x))
#         if inp=='exit':
#             break
# run(1,5)

# class Student(object):
#     count=0
#     print(id(count))
#     def __init__(self,name):
#         self.name=name
#         Student.count+=1
#
# s1=Student('qw')
# s1.age=12
# print(s1.age)

# class Screen(object):
#     @property
#     def width(self):
#         return self._width
#     @width.setter
#     def width(self,value):
#         self._width=value
#     @property
#     def height(self):
#         return self._height
#     @height.setter
#     def height(self,value):
#         self._height=value
#     @property
#     def resolution(self):
#         return self._height*self._width
# s=Screen()
# s.width=12
# s.height=5
# print('resolution=',s.resolution)

# ---------------------------多继承以拓扑排序为准，即入度为0，从最左边开始-----------
# class A(object):
#     def foo(self):
#         print('A foo')
#     def bar(self):
#         print('A bar')
#
# class B(object):
#     def foo(self):
#         print('B foo')
#     def bar(self):
#         print('B bar')
#
# class C1(A):
#     pass
#
# class C2(B):
#     def bar(self):
#         print('C2-bar')
#
# class D(C1,C2):
#     pass
#
# if __name__ == '__main__':
#     d=D()
#     print([x.__name__ for x in  D.__mro__])
#     d.foo()
#     d.bar()

# class A(object):
#     def __init__(self):
#         print('    -> Enter A')
#         print('    <- Leave A')
#
# class B(A):
#     def __init(self):
#         print('    -> Enter B')
#         # A.__init__(self)
#         super(B, self).__init__()
#         print('    <- Leave B')
#
# class C(A):
#     def __init__(self):
#         print("    -> Enter C")
#         # A.__init__(self)
#         super(C, self).__init__()
#         print("    <- Leave C")
#
# class D(B, C):
#     def __init__(self):
#         print("    -> Enter D")
#         # B.__init__(self)
#         # C.__init__(self)
#         super(D, self).__init__()
#         print("    <- Leave D")
#
# if __name__ == "__main__":
#     d = D()
#     print("MRO:", [x.__name__ for x in D.__mro__])
#     print(type(D.__mro__))
# ---------------------------多继承以拓扑排序为准，即入度为0，从最左边开始-----------

# class Student(object):
#     def __init__(self,name):
#         self.name=name
#     def __str__(self):
#         return 'Student object (name:%s)'%self.name
#     __repr__=__str__
# print(Student('bomb'))
# s=Student('jack')
# print(s)

# class Fib(object):
#     def __init__(self):
#         self.a,self.b=0,1
#     def __iter__(self):
#         return self
#     def __next__(self):
#         self.a,self.b=self.b,self.a+self.b
#         if self.a>1000:
#             raise StopIteration
#         return self.a
# for n in Fib():
#     print(n)

# class Fib(object):
#     def __getitem__(self, item):
#         if isinstance(item,int):
#             a,b=1,1
#             for x in range(item):
#                 a,b=b,a+b
#             return a
#         if isinstance(item,slice):
#             start=item.start
#             stop=item.stop
#             L=[]
#             a,b=1,1
#             if start is None:
#                 start=0
#             for x in range(stop):
#                 if x>=start:
#                     L.append(a)
#                 a,b=b,a+b
#             return L
# f=Fib()
# print(f[:7])

# --------------------链式调用------------------
# class Chain(object):
#     def __init__(self,path=''):
#         self._path=path
#     def __getattr__(self, item):
#         return Chain('%s/%s'%(self._path,item))
#     __call__=__getattr__
#     def __str__(self):
#         return self._path
# print(Chain().status.user('BOMB').timeline.list)
# --------------------链式调用------------------

# from enum import Enum
# Month=Enum('month',('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
# for name,member in Month.__members__.items():
#     print(name,'==>',member,',',member.value)


# from enum import Enum,unique
# @unique
# class Gender(Enum):
#     male=0
#     female=1
# class Student(object):
#     def __init__(self,name,gender):
#         self.name=name
#         self.gender=gender
# bar=Student('Bart',Gender.male)
# print(bar.gender)

# try:
#     print('try...')
#     r=10/int('3')
#     print('result:',r)
# except BaseException as e:
#     print('except:',e)
# finally:
#     print('finally...')


# from functools import reduce
#
# def str2num(s):
#     return int(s)
#
# def calc(exp):
#     ss = exp.split('+')
#     ns = map(str2num, ss)
#     return reduce(lambda acc, x: acc + x, ns)
#
# def main():
#     r = calc('100 + 200 + 345')
#     print('100 + 200 + 345 =', r)
#     r = calc('99 + 88 + 7.6')
#     print('99 + 88 + 7.6 =', r)
#
# main()

import logging

logging.basicConfig(level=logging.INFO)
n = 0
logging.info('n=%d' % n)
print(10 / n)
print('end')
