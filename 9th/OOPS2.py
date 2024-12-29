class Student:
    def __init__(self,name):
        self.name=name
    
s1=Student("Dilasha")
del s1.name#Deletes the object

class Account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no=acc_no
        self.__acc_pass=acc_pass #__double underscore makes things private so u cannot prin tor sth

acc1=Account("12345","abcde")
print(acc1.acc_no)
print(acc1.__acc_pass)
