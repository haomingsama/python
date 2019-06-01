import os 
import time
num=100
pid = os.fork() 
#在程序当中创建进程，执行一次代码， 返回两次。父进程返回一次，子进程返回一次。
# 子进程永远返回0，父进程返回子进程pid
# 一个父进程可以fork出很多子进程，所以，父进程要记下每个子进程的id，而子进程只需要调用getppid（）可以拿到父进程的id
# 父进程，子进程执行顺序没有规律，完全取决于操作系统的调度算法
# 进程是有独立的内存空间，父进程和子进程不能共享全局变量，子进程对全局变量的操作，不会影响全局变量在父进程中的值

if pid < 0:
	print("fork()调用失败")

elif pid == 0:
	time.sleep(2) #如果休眠过久，会导致父进程等太久不存在，再去找父进程就找不着了。系统可能会给一个更上层的父进程
	num +=1
	print("子进程，pid:%s， 父进程id :%s"%(os.getpid(),os.getppid()))
	print('num:%s'%num)
else :
	time.sleep(3)
	print("父进程， pid : %s, 子进程id : %s"%(os.getpid(), pid))
	print('num:%s'%num)

