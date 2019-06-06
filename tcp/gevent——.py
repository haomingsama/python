import gevent

def fun(num):
	for i in range(num):
		print('%s%s'%(gevent.getcurrent(), str(i)))
		#模拟一个耗时的任务
		gevent.sleep(2)
g1 = gevent.spawn(fun,5)
g2 = gevent.spawn(fun,4)
g3 = gevent.spawn(fun,3)


# 这是依次执行，正常的协程师交互执行
# 因为没有耗时的计算任务，需要让他模拟耗时的任务

g1.join()
g2.join()
g3.join()