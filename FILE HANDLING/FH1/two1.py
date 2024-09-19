fp1 = open('data1.txt','r')
data =fp1.read()

fp2 = open('banglore1.txt','w')
fp2.write(data)

fp3 =open('city1.txt','a')
fp3.write(data)


fp1.closer()
fp2.closer()
fp3.closer()