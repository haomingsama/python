from multiprocessing import Process
import time
import os


def run_proc(name,num,**kwargs):
	time.sleep(2)
	print("子进程：name :%s, num: %s"%(name,num))
	
	for k,v in kwargs.items():
		print('%s:%s'%(k,v))
	


print('父进程')
p = Process(target = run_proc, name = 'p1', args=("test",10,),kwargs={"a":10,"b":20})
p.start()
p.join(1) #等待一秒钟，会造成子进程不执行，因为子进程等待2秒，父进程只等1秒，然后就终止了

print('子进程的名字：%s,id : %s'%(p.name,p.pid))
p.terminate()
print('子进程已结束')
