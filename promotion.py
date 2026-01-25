class Product:
    def __init__ (self, name, price):
        self.name = name
        self.__price = price # No Tax Yet

    #Apply tax

    @property
    def price (self):
        return self.__price
    
    @property
    def price_with_tax(self):
        return self.__price*1.5
    
    @price.setter
    def price(self, value):
        if value > 0:
            self.__price = value
        else:
            raise ValueError("The Price Needs to be Positive!")
        
    @price_with_tax.setter
    def price_with_tax(self, value):
        if value > 0:
            self.__price = value / 1.5
        else:
            raise ValueError("The Price Needs to be Positive!")
        
    def promotion(self):
        return f"PROMOTION: {self.price_with_tax*0.75}!!"
    
    def __str__(self):
        return f"The Price is: {self.price_with_tax}"
    
product = Product("Table", 100)
print(product)
print(product.promotion())

product.price_with_tax = 200 # price_with_tax is important to avoid the error here
print(f"New price: {product}")
print(product.promotion())


