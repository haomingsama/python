import re
#推荐用ipython一行一行来运行代码，这样结果更清晰。

#匹配一个字符
re.match('h','hello python')

ret = re.match('.', 'hello python')
ret = re.match('no.\d', 'no.1 python')
ret = re.match('[hH]', 'hello python')
path = 'c:\\a\\b\\c'
print(path) ##打印出来只有一个反斜杠


ret = re.match("c:\\",path) # 会出错，因为\在python中有特殊含义
ret = re.match("c:\\\\",path) # 写4个反斜杠，每个都进行转译
ret = re.match(r'c:\\',path) #前面加一个r就可以不用转译符
ret.group()


#匹配多个字符
#手机号的例子
ret = re.match ('\d{11}','13570816336') #输出11位数字
ret.group()

ret = re.match('\d{11}','1233423a33')# 会出错

ret = re.match('[1-9]?[0-9]','7') # 问号跟在后面，表示有一次或者0次
ret = re.match('[1-9]?[0-9]','09') # 会匹配到0，因为表达式第一部分是可有可无的，第二部分正好匹配到第一个0
ret = re.match('[1-9]?[0-9]$','09') # 会匹配到9，$ 符号表示选出以【0-9】结尾的，就是从后面开始匹配，



ret = re.match(r'.*\bver\b','ho ver abc ') #\b 表示匹配单词边界


## search 在字符串中查找，而之前的是从前到后match
ret = re.search(r'\d+', '阅读次数为9999') # +号表示一个或者多个


ret = re.search(r'\d+', '阅读次数为9999, 评论200') # 只会输出9999，200不会出来
ret = re.findall(r'\d+', '阅读次数为9999, 评论200') ## 输出的ret是一个列表

ret = re.sub(r'\d+','9090', '阅读次数为9999, 评论200') #把两个数字都替换成了9090

ret = re.split(r":| ","info:xiaoZhang 33 shangdong") # 根据 ： 或者空格来分割字符串，输出列表


## 贪婪模式和非贪婪模式

ret = re.match('aa(\d+)','aa1234ddddddd')
ret = re.match('aa(\d+?)','aa1234ddddddd')
ret.group(1) #括号起的是分组的作用


