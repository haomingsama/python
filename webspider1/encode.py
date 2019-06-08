import urllib

url = 'http://www.baidu.com/s?'

# urllib的urleccode()接受的参数是一个字典
wd = {'wd':'传智播客'}

m = urllib.urlencode(wd)

print(urllib.unquote(m))