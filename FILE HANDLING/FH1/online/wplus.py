st = 'hello,good morning'

fp=open('stex.txt','w+')
fp.write(st)

data=fp.read()
print(data)


fp.close()