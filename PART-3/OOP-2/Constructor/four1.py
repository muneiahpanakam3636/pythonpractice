class Account:
    def __init__(self,id,name,amount):
        self.id = id
        self.name=name
        self.acc_bal =amount
    def depositr_amount(self,amount):
        self.acc_bal = self.acc_bal+amount
a1 =Account(101,"Sonia",5000) 
a1.depositr_amount(55)   
a1.depositr_amount(45)   
a2 =Account(102,"priya",4000)    
a2.depositr_amount(80)
a3 =Account(103,"muni",6000)    
a3.depositr_amount(99)

print(a1.__dict__)
print(a2.__dict__)
print(a3.__dict__)