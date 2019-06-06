from greenlet import greenlet
import time


def fun1():
	while True:
		print("...fun1...")
		gr2.switch()  ## 1.执行到这一步切换到fun2
		time.sleep(1) ## 3. 从fun2 切换过来的

def fun2():
	while True:
		print("...fun2...")
		gr1.switch() ## 2.执行到这一步切换到fun1 继续上一次的代码停止处执行
		time.sleep(1) ## 4. 从fun1切换过来的


gr1 = greenlet(fun1)
gr2 = greenlet(fun2)

gr1.switch()

### 