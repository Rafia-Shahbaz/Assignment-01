#Create a variable greeting and store a message. Print it.
greeting = "Hello Python!"
print(greeting)
#Change the value of greeting and print the new message.
greeting = "Hello World!"
print(greeting)
#Create first_name and last-name, then print full name using f-string.
first_name = "Rafia"
last_name = "Shahbaz"
print(f"{first_name} {last_name}")
#Print a famous quote with author' s name using f-string.
quote = "Stay hungry, Stay foolish."
author = "Steve Jobs"
print(f"{quote}: {author}")
#Store a name with extra spaces, strip them, and print clean output.
name = "      Rafia      "
name_strip = name.strip()
print(name_strip)
#Take a number, add 5, multiply by 2, subtract 3, and print the result.
num = 12
result = ((num + 5) * 2 - 3)
print(result)
#Creat a abd b; print their sum, difference, product, and quotient.
a = 4
b = 2
print("Sum:", a + b)
print("Difference:", a - b)
print("Product:", a * b)
print("Quotient:", a / b)
#Final square and cube of a number using ** operator.
num = 16
print("Square:", num ** 2)
print("Cube:", num ** 3)
#Add three floating-point numbers and print the total.
a = 12.3
b = 14.6
c = 15.6
total = (a + b + c)
print(total)
#Assign x,,y,z in one line and print them.
x , y , z = 2, 3, 6
print(x, y, z)
#Create a list of 5 favorite fruits and print each one separately.
fav_fruits = ["Apple", "Banana", "Cherry", "Grapes", "Pineapple"]
for fruit in fav_fruits:
    print(fruit)
#Appened a new fruit and insert one at the beginning.
fruits_name = ["Apple", "Banana", "Cherry", "Grapes", "Pineapple"]
fruits_name.append("Kiwi")
fruits_name.insert(1, "Mango")
print(fruits_name)
#Modify the 2nd item in the list and print the updated list.
item_list = ["Pencil", "Cup", "Bread", "Sugar", "Milk"]
item_list[2] = "Mango"
print(item_list)
#Delete items using del, pop(), and remove.
a = ["Black peper", "Chili", "Powder", "Cup"]
del a [1]
print(a)
a.pop(2)
print(a)
a.remove("Powder")
print(a)
#Use sort() and sorted() to sort the list. show before and after.
a = [ 1,3,4,6,5,2,7,8,9]
print("Before sort:", a)
a.sort()
print("After sort:", a)
b = [1,3,2,4,6,5,7,9,8,]
print("Before sorted:", b)
c = sorted(b)
print("After sorted:", b)
#Create a list of dream travel destinations: Sort alphabetically, Reverse the order, count total destinations,
d = ["Paris", "Madina", "Spain", "Turkey", "UK"]
sorted(d)
print("Sorted Alphabetically:", x)
d.reverse()
print("Reverse order:", d)
print("Total destinations:", len(d))
#Start with an empty guest list: Append 3 guest, Insert 1 at the beginning,  Remove one using pop(), Print final list.
guest_list = []
guest_list.append("Noor")
guest_list.append("Zahra")
guest_list.append("Ali")
guest_list.insert(2, "Fariha")
guest_list.pop(1)
print(guest_list)
#Assecc the last 3 elements of a list without negative indexing.
a = [2,3,4,7,6,8,5]
print(a[3:6])
#From a list of numbers, print only even numbers.
numbers = [1,2,3,4,5,6,7,8,9,]
print("Even number:")
for num in numbers:
    if num % 2 == 0:
      print(num)
#Print squares of the first 10 natural numbers in a list.
square = []
for i in range(1, 11):
   square.append(i * 4)
print("Square of the first 10 natural numbers:", square)