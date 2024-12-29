class Car:
    @staticmethod
    def start():
        print("Car started..")
    
    @staticmethod
    def stop():
        print("Car stopped")

class Toyota(Car):
    def __init__(self,brand):
        self.brand=brand

class Fortuner(Toyota):
    def __init__(self,type):
        self.type=type
car1=Fortuner("petrol")
car1.start()#multi level inheritance