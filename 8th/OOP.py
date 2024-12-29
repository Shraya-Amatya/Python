class Student():
    college_name="Nagarjuna College"# remains the same in memory only stored 1 time
    name="Error 404" #class attribute
    #parameterized constructor
    def __init__(self,fullname,marks):
        self.name=fullname #object attr>class attr
        self.marks=marks


s1=Student("Dilasha",99)
print(s1.name,s1.marks)

s2=Student("Shraya",91)
print(s2.name,s2.marks)
print(Student.college_name)
# class Car:
#     color="red"
#     brand="Mercedes"

# car1=Car()
# print(car1.color,car1.brand)