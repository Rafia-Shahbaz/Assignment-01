#Takes input for 5 items: name, price, quantity (as strings)
#Convert all values using casting to int and float
#Store data in lists and dictionaries
#Add 10% tax, calculate subtotal, total, and average
#dentify high-value items (price > 500) and store in a set, convert to frozenset
#Use functions: calculate_bill(), apply_discount(), print_cart_summary()
#Use loops to display item info with type() checks
#Use random.choice() for a giveaway item
#Use keyword module to verify if item name is a Python keyword
#Use datetime to log purchase time and calendar to show current month
import keyword 
import datetime
import calendar
import random
items = []
high_value_items = set()
grand_total = 0
for i in range(5):
    print(f"\nEnter details for item {i+1}")
    name = input("Item name: ")
    price = float(input("Price: "))
    quantity = int(input("Quantity: "))
    items.append({"name": name, "price": price, "quantity": quantity})
def calculate_bill(item):
    subtotal = item["price"] * item["quantity"]
    tax = subtotal * 0.10
    total = subtotal + tax
    return subtotal, tax, total 
def apply_discount(total):
    if total > 1000:
        return total * 0.90
    return total
def print_cart_summary(items):
    global grand_total
    print("\n--- CART SUMMARY ---") 
    total_all_items = 0
    for item in items:
     subtotal, tax, total = calculate_bill(item)
     discounted_total = apply_discount(total)
     grand_total += discounted_total
     print(f"Item: {item['name']}, Price: {item['price']}, Quantity: {item['quantity']}, Total: {total:.2f} ")
     print(f"Type checks -> Name: {type(item['name'])}, Price:{type(item['price'])}, Quantity: {type(item['quantity'])}")
     print(f"Is item name a Python keyword? {keyword.iskeyword(item['name'])}")
     print("-" * 40)
     if item["price"] > 500:
         high_value_items.add(item["name"])
print_cart_summary(items)
average = grand_total / len(items)
frozen_items = frozenset(high_value_items)
giveaway = random.choice(items) ["name"] 
print(f"Grand Total: {grand_total:.2f}")
print(f"Average Item Total: {average:.2f}")
print(f"Random.Giveaway Item: {giveaway}")
print(f"High-value items (frozen Set): {frozen_items}")
print(f"Purchase time: {datetime.datetime.now()}")
print(f"Current month: {calendar.month_name[datetime.datetime.now().month]}")