class Product :
    def __init__ (self,name,price,deal_price,rating):
        self.name = name 
        self.price = price 
        self.deal_price = deal_price 
        self.rating = rating 
        self.amount_save = self.price - self.deal_price
    @property
    def get_product_details(self):
        print(self)
        print('name :{}'.format(self.name))
        print('price :{}'.format(self.price))
        print('deal_price :{}'.format(self.deal_price))
        print('rating :{}'.format(self.rating))
        print('amount_you_save :{}'.format(self.amount_save)) 
class ElectronicItem(Product):
    # def add_warrenty(self , warrenty):
    #     self.warrenty = warrenty 
    
    # def get_elect_product_details(self):
    #     self.get_product_details
    #     print("warrnty_in_months : {}".format(self.warrenty))
    def __init__(self,name,price,deal_price,rating,warrenty):
        super().__init__(name,price,deal_price,rating)
        self.warrenty = warrenty 
    def get_product_details(self):
        super().get_product_details 
        print("warrnty_in_months : {}".format(self.warrenty))



obj1 = Product('shoes',1500,1200,4.5) 
print(obj1.amount_save)
print(obj1)
obj1.get_product_details
# obj2= ElectronicItem("HP vPRO", 80000 ,65000,4.5) 
# obj2.add_warrenty(24)
# print(obj2)
# obj2.get_elect_product_details()
obj2= ElectronicItem("HP vPRO", 80000 ,65000,4.5,24) 
print(obj2)
obj2.get_product_details()
