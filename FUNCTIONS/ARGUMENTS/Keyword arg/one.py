#  while changing the arguments place .
def calc(a,b):
    print(a-b)

calc(100,200)
calc(200,100)
# -100
# 100



#by using keyword arguments we can get same output
def calC(a,b):
    print(a-b)
calC(a=100,b=200)   #-100

calC(b=200,a=100)   # -100


