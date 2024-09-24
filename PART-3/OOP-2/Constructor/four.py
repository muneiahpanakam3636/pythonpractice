class Account():
    min_bal = 500
    def __init__(self,id,name,amount) :
        self.acc_id = id
        self.acc_name = name
        self.acc_bal = amount
    def deposite_amount(self,amount):
     self.acc_bal= self.acc_bal+amount 
a1= Account(101,"rahul",5000)    
a1.deposite_amount(15)
a1.deposite_amount(20)
a2 = Account(102,"sonia",6000)
a3 = Account(103,"priya",7000)
a3.deposite_amount(50)

print(a1.__dict__)
print(a2.__dict__)
print(a3.__dict__)
print(a3.__dict__)