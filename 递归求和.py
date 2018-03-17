#递归求和
money = 10000
def cost(money,day=0):
	if money<=0:
		print("没钱了!")
		print("可以花%d天" %day)
		return
	else:
		money=money//2
		day+=1
		cost(money,day)

cost(money)			
money2=200
cost(money2)