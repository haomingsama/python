import urllib
import urllib.request as urllib2

#urllib has been split up in Python 3. 
#The urllib.urlencode() function is now urllib.parse.urlencode(), 
#and the urllib.urlopen() function is now urllib.request.urlopen().



url = 'http://www.baidu.com/s'

keyword = input('请输入需要查询的字符串')
headers = {'User-Agent': 'Mozilla....'}  #百度不会反爬虫
wd = {'wd': keyword}

wd = urllib.parse.urlencode(wd)

fullurl = url+'?'+wd

request=urllib2.Request(fullurl,headers = headers)

response = urllib2.urlopen(request)

print(response.read())