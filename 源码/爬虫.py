#objURL
from urllib.request import *
import re
#url ='http://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1521279665612_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E7%A7%91%E6%AF%94'

url='http://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1521280526612_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E4%B9%94%E4%B8%B9'
html = urlopen(url)#打开一个网页
#html代码
obj = html.read().decode()
#print(obj)
#解码,转换成字符串
print(type(obj))
urls = re.findall('"objURL":"(.*?)"',obj)
#贪婪
#非贪婪
index=0
for url in urls:
	try:
		print('download....%d' %index)
		#if re.serach('.jpg$',url):

		urlretrieve(url,'pic'+str(index)+'.jpg')
		index+=1
	except Exception:
		print('download error....%d' %index)
	else:
		print('download complete....')	

