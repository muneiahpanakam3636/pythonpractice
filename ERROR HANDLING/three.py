try:
    fp=open("muni.txt",'r')
except:
    open("MUni.txt",'r')
data= fp.read()         
print(data)
print("welcome to banglore")