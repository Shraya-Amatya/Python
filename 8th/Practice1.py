class Student():
    def __init__(self,fullname,marks):
        self.name=fullname
        self.marks=marks
    @staticmethod
    def gand():
        print("Dilasha gandu")
    def avg(self):
        sum=0
        for val in self.marks:
            sum+=val
        print("Your average is:",sum/len(self.marks))
s1=Student("Dilasha",[80,48,85])
print(s1.name,s1.marks)
s1.avg()
s1.gand()
