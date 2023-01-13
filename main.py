#create a class:
class Item:
    
    #create a method in class to calculate toal price of an item
    def total_price(self, x, y):
        return x * y

# instantiate object from class
item1 = Item()

# Assign attributes:
item1.name = "book"
item1.price = 50
item1.quantity = 20

# Calling methods from instances of a class:
print(item1.total_price(item1.price, item1.quantity))

item2 = Item()

# Assign attributes:
item2.name = "mouse"
item2.price = 800
item2.quantity = 5

print(item2.total_price(item2.price, item2.quantity))
