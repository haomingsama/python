import urllib
import urllib.parse
import urllib.request as urllib2

def loadPage(url,filename):

	'''
	作用：根据url发送请求，获取服务器响应文件
	url： 需要爬去的url地址
	filename: 处理的文件名
	'''
	print('正在下载' + filename)
	headers = {'User-Agent': ''}
	request = urllib2.Request(url,headers= headers)
	return urllib2.urlopen(request).read()

def writePage(html,filename):
	'''
	作用： 将html内容写入到本地
	html： 服务器响应文件内容

	'''
	print('正在保存'+filename)
	with open(filename, 'wb') as f:
		f.write(html)
	print('文件写入成功')


def tiebaSpider(url, beginPage,endPage):
	'''
	作用：贴吧爬虫调度器，负责组合处理每个页面的url
	url：贴吧url的前部分
	beginPage:起始页
	endPage:结束页
	'''
	for page in range(beginPage,endPage+1):
		pn = (page -1)*50
		filename = '第' + str(page) + "页.html"
		fullurl = url + '&pn='+str(pn)
		html = loadPage(fullurl,filename)
		writePage(html,filename)
		print("谢谢使用")





if __name__ == '__main__':
	kw = input ('请输入贴吧名字：')

	beginPage = int(input ("请输入起始页："))
	endPage = int(input("请输入结束也："))

	url = 'http://tieba.baidu.com/f?'
	key= urllib.parse.urlencode({"kw":kw})
	fullurl = url +key
	tiebaSpider(fullurl, beginPage,endPage)
