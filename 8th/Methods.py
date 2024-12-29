#Functions inside class is called Methods
class Student():
    #parameterized constructor
    def __init__(self,fullname,marks):
        self.name=fullname #object attr>class attr
        self.marks=marks
    def welcome(self):
            print("Welcome student,",self.name)
            
    def get_marks(self):
            print("your marks is :",self.marks)


s1=Student("Dilasha",100)
s1.welcome()
print(s1.get_marks())