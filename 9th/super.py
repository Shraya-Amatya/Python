class Car:
    def __init__(self,type):
        self.type=type
    @staticmethod
    def start():
        print("Car started..")
    
    @staticmethod
    def stop():
        print("Car stopped")

class Toyota(Car):
    def __init__(self,brand,type):
        super().__init__(type)#Super is used to access method of parent class
        self.brand=brand 
        super().start()

car1=Toyota("prius","petrol")
car1.start()#multi level inheritance