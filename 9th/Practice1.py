class Circle:
    def __init__(self,radius):
        self.radius=radius
        
    def Area(self):
        Area=(3.14*self.radius**2)
        return Area
    def Peri(self):
        Peri=(2*3.14*self.radius)
        return Peri
c1=Circle(21)
print(c1.Area())
print(c1.Peri())