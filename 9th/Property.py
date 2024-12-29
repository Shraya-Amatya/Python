class Student:
    def __init__(self,phy ,chem,math):
        self.phy=phy
        self.chem=chem
        self.math=math
        # self.percentage=str((self.phy+self.chem+self.math)/3)+"%"
        
    @property#so even if there are changes it will solve it
    def percentage(self):
        return str((self.phy+self.chem+self.math)/3)+"%"

stu1=Student(100,56,22)
print(stu1.percentage)

stu1.phy=30#changes to the marks as it was wrong
print(stu1.percentage)