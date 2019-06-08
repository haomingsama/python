import urllib2
#这个已经失效了，但是了解工作原理更易于理解爬虫

#发请求到指定的地址里， data决定了是get和post请求， 默认超时限制timeout可以设置比如10秒
#返回会是一个类文件对象（类似文件的对象） 可以进行读写操作
rep = urllib2.urlopen('http://www.baidu.com')

#服务器返回的类文件对象支持python文件对象的操作方法

# read() 方法是读取文件里的全部内容，返回字符串
html = rep.read()

#打印响应内容
print(html)


#urllib2 弊端
# 不支持构造请求，意味着无法模拟浏览器
#其自带的user-agent ： Python-urllib/2.7
#服务器会识别为爬虫
#反反爬虫要重构user-agent

#urllib2.Request(url, data, headers) 构造header
# 通过这个方法，构造一个请求对象
# 通过抓包工具，拿到浏览器的报头

ua_headers = {'User-Agent':""}
request = urllib2.Request('http://www.baid.com/',headers = ua_headers) #参数的顺序要遵循

response = urllib2.urlopen(request)

html = response.read()

print(html)


#response 是服务器响应的类文件，除了支持文件操作的方法外，还支持一下操作
#返回htttp的响应码，成功返回200，4服务器页面出错，5服务器问
print(response.getcode())
#发送具体访问的url，防止重定向问题。
print(response.geturl())
#返回服务器响应的HTTP 报头信息
print(response.info())
#如果想要获取python发送给服务器的请求信息，可以通过抓包工具



