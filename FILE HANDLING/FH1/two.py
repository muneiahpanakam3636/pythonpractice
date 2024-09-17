fp1 =  open('data.txt','r')
data = fp1.read()


fp2 = open('banglore.txt','w')   #--> file is not avilable it is going to create to new file
fp2.write(data)
# print("new file created!")

fp3 = open('city.txt','a')
fp3.write(data)




fp1.close()
fp2.close()
fp3.close()
