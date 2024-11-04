#  how to acheive absrtaction.by using abstraction method.  
from abc import *


class Bank(ABC):
  
  @abstractmethod
  def cal_bal(self):
    pass

# Bank()

 #any class contains extending abc module 
 #and it contains atleast one abstract method,
 # we can't create object.