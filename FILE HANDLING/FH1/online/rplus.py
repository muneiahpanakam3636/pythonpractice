fp=open('data.txt','r+')
data=fp.read()
fp.write('hello,good evening')

# print(data)

fp.close()