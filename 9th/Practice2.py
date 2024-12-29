class Employee:
    def __init__(self,role,department,salary):
        self.role=role
        self.department=department
        self.salary=salary
    def showDetails(self):
        print(self.role)
        print(self.department)
        print(self.salary)

class Engineer(Employee):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        super().__init__("Engineer","Top",30000)
s1=Employee("Manager","Head",20000)
print(s1.showDetails())

s2=Engineer("gandi",21)
print(s2.showDetails())