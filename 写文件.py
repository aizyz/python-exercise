from time import sleep
myfile = open ('2.txt','a')
myfile.write('www')
myfile.flush()
#close
sleep(10)

myfile.close()



