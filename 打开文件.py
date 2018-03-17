#读写
myfile = open('1.txt','r')
#绝对路径:根目录
#相对路径::从某个路径开始
mystr=myfile.read(3)
print(mystr)
myfile.seek(0,2)
mystr1=myfile.read(7)
print(mystr1)
myfile.read
