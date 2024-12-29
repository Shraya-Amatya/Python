class Person:
    name="anonymous"
    
    def changeName(self,name):
        self.name=name

s1=Person()
s1.changeName("Gand")
print(s1.name)