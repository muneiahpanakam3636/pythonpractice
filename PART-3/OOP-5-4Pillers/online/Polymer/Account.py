from Bank import Bank

class Account(Bank):

    def __init__(self,name,email,address):
        self.acc_name=name
        self.acc_email=email
        self.acc_address=address

        

    def cal_bal(self):
        pass
    def open_Account(self):
        print('account opened')


a1=Account('rahul','rahul@gmail.com','Banglore')    
print(a1.__dict__)