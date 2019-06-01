from multiprocessing import Process
import time
import os


## 定义自己的子类
class Myprocess(Process):

	def __init__(self,interval):
		#继承父类的方法
		super().__init__()
		self.interval = interval



##定义了这个之后，p.start() 启动后就会自动运行这个代码，对自己的进程类进行定制化修改
	def run(self):
		print('子进程')
		startTime = time.time()
		time.sleep(self.interval)
		stopTime=time.time()
		print("子进程id：%d 父进程id：%d, 执行了%s秒"%(os.getpid(),os.getppid(),stopTime-startTime))
	

'''
进程池：用来存放创建好的进程，动态生成多个进程，pool方法，指定一个最大的进程数，当有新的进程用来执行该请求，如果池中的进程数已经达到指定的最大值
那么请求会等待，知道池中有进程结束，才会创建的新的进程来执行
'''



print("父进程")
startTime =time.time()
childs = []
#同时创建5个子进程，并且同时运行
#进程的创建要消耗资源，创建太多不可取
for i in range(5):
	p = Myprocess(i+1)
	p.start()
	childs.append(p)
	#p.join() #后续代码不会执行
for item in childs:
	item.join() #让父进程不等子进程完，先把子进程放到列表中，同时运行，然后在同时结束。
stopTime = time.time()
print("子进程结束，消耗的时间%s"%(stopTime-startTime))


