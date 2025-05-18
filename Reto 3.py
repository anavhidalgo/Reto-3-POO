class MenuItem:
    def __init__(self, name, price):
        self.name = name 
        self.price = price
    
    def total_price(self):
        return self.price 
    
class Beverage(MenuItem):
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.size = size
    
class Apetizer(MenuItem):
    def __init__(self, name, price, shared):
        super().__init__(name, price)
        self.shared = shared
    
class MainCourse(MenuItem):
    def __init__(self, name, price, vegetarian):
        super().__init__(name, price)
        self.vegetarian = vegetarian

class Order:
    def __init__(self):
        self.items =[]

    def add_item(self, item):
        self.items.append(item)
    
    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item.total_price()
        return total
    
    def apply_discount(self):
        total = self.calculate_total()
        if len(self.items) > 6:
            return total * 0.8 # 20% de discount
        return total
    
menu = [
    Beverage("Coke", 1.50, "Medium"),
    Beverage("Water", 1.00, "Large"),
    Beverage("Juice", 2.00, "Small"),
    Apetizer("Nachos", 5.00, True), # shared
    Apetizer("Wings", 6.00, True), # shared
    Apetizer("Fries", 3.00, False), # not shared
    MainCourse("Pasta", 12.00, True), # vegetarian
    MainCourse("Burger", 10.00, False), # not vegetarian
    MainCourse("Steak", 15.00, False), # not vegetarian
    MainCourse("Salad", 8.00, True), # vegetarian
    
]

order = Order()
order.add_item(menu[0]) # Coke
order.add_item(menu[2]) # Juice
order.add_item(menu[3]) # Nachos
order.add_item(menu[5]) # Fries
order.add_item(menu[6]) # Pasta
order.add_item(menu[8]) # Steak
order.add_item(menu[9]) # Salad

print("Total before discount: $", order.calculate_total())
print("Total after discount: $", order.apply_discount())