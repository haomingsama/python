def isPhone(num):
	#判断长度是不是11位

	if len(num) != 11:
		print('长度不符合11位')
		return False
	#判断是不是都是数字

	if not str.isdigit(num):
		print('不是数字')
		return False

	#判断前三位是不是正确的号段
	li = ['138','137','136','186','187','177']
	if num[:3] not in li:
		print('号码不在号段内')
		return False
	return True


num = input(">>")

print(isPhone(num))
