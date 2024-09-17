def calC(a,b,c):
    print(a+b+c)
calC(10,20,30)    
calC(10,20)  #TypeError: calC() missing 1 required positional argument: 'c'
calC(1,2)  #TypeError: calC() missing 1 required positional argument: 'c'