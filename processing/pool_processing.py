from multiprocessing import Pool
import time
import os
'''
进程池：用来存放创建好的进程，动态生成多个进程，pool方法，指定一个最大的进程数，当有新的进程用来执行该请求，如果池中的进程数已经达到指定的最大值
那么请求会等待，知道池中有进程结束，才会创建的新的进程来执行
同步： 等上一个进程执行完了，才执行下一个
异步： 不等待，同时执行
进程池里面创建好的进程不断的去使用，效率会高。
'''
def worker(msg):
	print('子进程pid： %s'%os.getpid())
	startTime = time.time()
	time.sleep(2)
	stopTime = time.time()
	print("子进程msg ： %s ， 花费的时间 %s"%(msg,stopTime-startTime))

# 创建进程池
pool = Pool(3)

for x in range(10):
	#异步请求
	#pool.apply_async(worker,(x,))
	#同步请求
	pool.apply(worker,(x,))
#关闭进程池
pool.close()
#父进程等待进程池结束
pool.join()
print("进程池结束")