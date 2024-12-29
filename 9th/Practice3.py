class Order:
    def __init__(self,item,price):
        self.item=item
        self.price=price
        
    def __gt__(self,order2):
        return self.price>order2.price
order1=Order("Washer",20)
order2=Order("Soap",40)

print(order1>order2)