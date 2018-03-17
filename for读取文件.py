myfile = open('1.txt','r')
mylist = []
for var in myfile:
	mylist.append(var)
	print(var)