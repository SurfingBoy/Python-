# -*- coding:utf-8 -*-
# import time,threading
# def loop():
#     print('thread %s is running..'%threading.current_thread().name)
#     n=0
#     while n<5:
#         n+=1
#         print('thread %s => %s'%(threading.current_thread().name,n))
#         time.sleep(1)
#     print('thread %s ended'%threading.current_thread().name)
# if __name__ == '__main__':
#     print('thread %s is running..'%threading.current_thread().name)
#     t=threading.Thread(target=loop,name='LoopThread')
#     t.start()
#     t.join()
#     print('thread %s ended'%threading.current_thread().name)

# -------------------加锁------------------------
# import threading
# balance=0
# lock=threading.Lock()
# def chang_it(n):
#     global balance
#     balance=balance+n
#     balance=balance-n
# def run_thread(n):
#     for i in range(10000):
#         lock.acquire()
#         try:
#             chang_it(n)
#         finally:
#             lock.release()
# if __name__ == '__main__':
#     t1=threading.Thread(target=run_thread,args=(5,))
#     t2=threading.Thread(target=run_thread,args=(8,))
#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()
#     print(balance)


# ------------------ThreadLocal---------------
import threading

# 创建全局ThreadLocal对象
local_school = threading.local()


def process_student():
    # 获取当前线程关联的student
    std = local_school.student
    print('Hello %s(in %s)' % (std, threading.current_thread().name))


def process_thread(name):
    # 绑定threadLocal的student
    local_school.student = name
    process_student()


t1 = threading.Thread(target=process_thread, args=('daming',), name='Thread_A')
t2 = threading.Thread(target=process_thread, args=('zhangsan',), name='Thread_B')
t1.start()
t2.start()
t1.join()
t2.join()
