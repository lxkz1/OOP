import random


class Restaurant:
    class Menuitem:
        def __init__(self, dish_name, dish_price):
            self.dish_name = dish_name
            self.dish_price = dish_price
    class Order:
        def __init__(self, table_number):
            self.table_number = table_number
            self.dishes_ordered = []
    def __init__(self, restaurant_name , tax_rate):
        self.restaurant_name = restaurant_name
        self.tax_rate = tax_rate
        self.menu = {}
        self.orders = {}

    def add_dish_to_menu(self,dis_name,dish_price):
        if dis_name in self.menu:
            return f"{dis_name} is already in the menu of the {self.restaurant_name} Restaurant"
        else:
            menuitem  = self.Menuitem(dis_name,dish_price=dish_price )
            self.menu[dis_name] = menuitem
            return f"Successfully added {dis_name} in the menu of the {self.restaurant_name} Restaurant"

    def show_menu(self):
        for item in self.menu:
            print(f"Item: {item},Item price: {self.menu[item].dish_price}$")

    def open_order_for_table(self, table_number):
        if table_number in self.orders:
            order = self.orders[table_number]
            if len(order.dishes_ordered) == 0:
                return f"Please Enter the dishes you want to order: "
            else:
                return f"You have already ordered"
        else:
            answer = input(f"Do you wish for me to open a table number for you?").strip().lower()
            if "yes" in answer:
                while True:
                    number = random.randint(1, 100)
                    if number in self.orders:
                        continue
                    else:
                        break
                self.order = self.Order(number)
                self.orders[number] = self.order
                print(f"Okay Your Table number will be {number}")
            else:
                print(f"Okay have a nice day!")



    def add_dish_to_table(self, dish_name , table_number):
        if table_number in self.orders:
            if dish_name not in self.menu:
                return f"The {dish_name} dish is not currently available on the menu"
            else:
                order = self.orders[table_number]
                order.dishes_ordered.append(self.menu[dish_name])
                return f"Successfully added {dish_name} to the order"
        else:
            return f"table number does not exist in the {self.restaurant_name} Restaurant"


    def tables_bill(self, table_number):
        dish_price_total = 0
        if table_number in self.orders:
            for dish in self.orders[table_number].dishes_ordered:
                print(f"{dish.dish_name} , {dish.dish_price}")
            for dish in self.orders[table_number].dishes_ordered:
                dish_price_total += dish.dish_price
            amount_of_tax = dish_price_total * self.tax_rate
            total = dish_price_total + amount_of_tax
            print(f"total : {total}$")
        else:
         print(f"{table_number} is not a table")



krusty_krab = Restaurant("Krusty Krab", 0.1)
print(krusty_krab.add_dish_to_menu("Krabby Patty", 3.5))
print(krusty_krab.add_dish_to_menu("Kelp Shake", 2))
print(krusty_krab.add_dish_to_menu("Coral Bits", 1.5))
print(krusty_krab.add_dish_to_menu("Krabby Patty", 4))
krusty_krab.show_menu()
krusty_krab.open_order_for_table(0)
table = list(krusty_krab.orders)[-1]
print(krusty_krab.open_order_for_table(table))
print(krusty_krab.add_dish_to_table("Krabby Patty", table))
print(krusty_krab.add_dish_to_table("Kelp Shake", table))
print(krusty_krab.add_dish_to_table("Krabby Patty", table))
print(krusty_krab.add_dish_to_table("Pizza", table))
print(krusty_krab.add_dish_to_table("Kelp Shake", 999))
print(krusty_krab.open_order_for_table(table))
krusty_krab.tables_bill(table)
krusty_krab.tables_bill(999)
krusty_krab.open_order_for_table(0)
print(len(krusty_krab.orders))
