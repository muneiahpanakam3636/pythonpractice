class Employee:
    company_name = 'TCS'
   
    def __init__(self,id,name,sal) :
        self.eid = id
        self.ename = name
        self.esal = sal

e1 =Employee(101,"Rahul",45000)
print(e1.__dict__)
e2 = Employee(102,"sonia",55000)
print(e2.__dict__)
e3 = Employee(103,"priya",65000)
print(e3.__dict__)


print(Employee.__dict__)

