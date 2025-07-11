#Decalre a variable student_id with value 101 (integer) and a variable grades with a list:[85, 90, 92]. Print the value and type of both variables using the type() function.
student_id = 101
grades = [85, 90, 92]
print(f"Value: {student_id}, Type: {type(grades)}")
print(f"Value: {grades}, Type: {type(grades)}")
#Create a variable price with value 19.99(float) and a variable dimensions with a tuple:(5.5,3.2). Print the value and type of both variable.
price = 19.99
dimensions = (5.5, 3.2)
print(f"Value: {price}, Type: {type(price)}")
print(f"Value: {dimensions}, Type: {type(dimensions)}")
#Declare a variable complex_value with a complex number 2+3j, and a variable numbers with range(1,5). print the value and type of both variables.
complex_value = 2 + 3j
numbers = range(1 ,5)
print(f"Value: {complex_value}, Type: {type(complex_value)}")
print(f"value: {list(numbers)}, Type: {type(numbers)}")
#Create a variable is_active with boolean valueTrue, and a variable unique_ids with a set:{1,2,3}. print the value and type of both variables.
is_active = True
unique_ids = {1, 2, 3}
print(f"Value: {is_active}, Type: {type(is_active)}")
print(f"Value: {unique_ids}, Type: {type(unique_ids)}")
#Declare a variable status with a string 'Active' using single quotes, and a variable fixed_colors with a frozenset containing "red" and "blue", Print the value and type of both variables.
status = 'Active'
fixed_colors = frozenset(["red", "blue"])
print(f"Value: {status}, Type: {type(status)}")
print(f"Value: {fixed_colors}, Type: {type(fixed_colors)}")
#Create a variable country with a string "Canada" using double quotes, and a variable cities with a list : ["Toronto", "Vancouver"]. Print the value and type of both variables.
country = "Canada"
cities = ["Toronto" , "Vancouver"]
print(f"Value: {country}, Type: {type(country)}")
print(f"Value: {cities}, Type: {type(cities)}")
#Declare a variable motto with the string 'Keep it simple' using triple single quotes, and a variable coordinates with a tuple: (10,20,30). Print the value and type of both variables.
motto = '''Keep it simple'''
coordinates = (10, 20, 30)
print(f"value: {motto}, Type: {type(motto)}")
print(f"Value: {coordinates}, Type: {type(coordinates)}")
#Create a variable quantity with value 50 (integer), and a variable tags with a sat: {"urgent", "new"}. Print the value and type of both variables.
quantity = 50
tags = {"urgent", "new"}
print(f"Value: {quantity}, Type: {type(quantity)}")
print(f"Value: {tags}, Type: {type(tags)}")
#Declare a variable distance with a float value 42.5, and a variable steps with range(0,10,2). Print the value and type of both variables.
distance = 42.5
steps = (0, 10, 2)
print(f"Value{distance}, Type: {type(distance)}")
print(f"Vlaue: {steps}, Type: {type(steps)}")
#**Create a variable note with a multi-line string using triple double quotes: Meeting at 9 AM Bring notebook and a variable locked_values with frozenset:{100,200,300}. Print the value and type of both variables.**
note = """Meeting at 9 AM Bring notebook"""
locked_value = frozenset({100, 200, 300})
print(f"Value: {note}, Type: {type(note)}")
print(f"Value: {locked_value}, Type: {type(locked_value)}")