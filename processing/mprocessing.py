from multiprocessing import Process
import os


def run_proc(name):
	print('子进程代码运行，子进程id： %s， 父进程id: %s,name:%s'%(os.getpid(),os.getppid(),name))




print('父进程代码')
##创建子进程˜
p = Process(target = run_proc, args=("test",))
# 开始执行子进程
p.start()
# 父进程等待子进程结束后再继续往下运行，通常用于进程间的同步
p.join()
print("子进程已结束")