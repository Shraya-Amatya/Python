# print(1+2)
# print("Shraya"+"Amatya")#concatenate
# print([1,2,4]+[2,4,6])#merge


#operating overloading
class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
        
    def showNum (self):
            print(self.real,"i +",self.img,"j")
    def __add__(self,num2):
        newReal=self.real+num2.real
        newImg=self.img+num2.img
        return Complex(newReal,newImg)
num1=Complex(2,10)
print(num1.showNum())

num2=Complex(20,1)
print(num2.showNum())

num3=num1+num2
num3.showNum()