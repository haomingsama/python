
import gevent
from urllib import request

### 需要让gevent能够自动处理io事件，需要先打补丁

gevent.monkey.patch_all()

def downloader(url):
	print('get %s'%url)
	rep = request.urlopen(url)
	data = reponse.read()
	print('从%s收到%s数据'%(url, len(data))

g1 = gevent.spawn(downloader,"http://www.baidu.com")
g2 = gevent.spawn(downloader,"http://www.sina.com")
g3 = gevent.spawn(downloader,"http://www.bjsxt.com")

g1.join()
g2.join()
g3.join()