from multiprocessing import Pool, Manager
import os, time,random

def write(q):
	for item in "ABC":
		print("正在往消息队列写入%s"%item)
		q.put(item)
		time.sleep(random.random())

def reader(q):
	while True:
		if not q.empty():
			item = q.get()
			print("从消息队列读出%s"%item)
			time.sleep(random.random())

		else:
			break


#创建消息队列
q=Manager().Queue()
#创建进程池
pool = Pool(3)
#创建写入过程
pool.apply(write,(q,))
#创建读进程
pool.apply(reader,(q,))

pool.close()
pool.join()

print("所有数据已读完")