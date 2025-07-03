#Create two variables a=10 and b=3.Perform print: addition(+), subtraction(-), multiplication(x), division(/), modulus(%), exponentiation(), and floor division(//).**
a = 10 
b = 3
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)
print("Floor Divsion:", a // b)
#Compare a and b using comparison operators: ==, !=, >, <, >=, <=. Print the result of each comparison.
a
b
print("Equal:", a == b)
print("Not Equal:", a != b)
print("Greater Than:", a > b)
print("Less Than:", a < b)
print("Greate Than or Equal:", a >= b)
print("Less Than or Equal:", a <= b)
#Create two boolean variables: x=True, y=False. Perform and print results of: x and y, x or y, x not y.
x = True
y = False
print("x and y:", x and y)
print("x or y:", x or y)
print("not x:", not x)
#Create num + 5 and perforn assignment operations: +=, -=, *=, /=, %=, **=, //=. Print the result after each operation.
num = 5
num += 1
print("After += : ", num)
num -= 2
print("After -= :", num)
num *= 3
print("After *= :", num)
num /= 2
print("After /= :", num)
num %= 4
print("After %= :", num)
num **= 2
print("After **= :", num)
num //= 3
print("After //= :", num)
#Create m = 100, n = 100 Check if they are the same object using is and is not, and print the result.
m = 100
n = 100
print("m is n:", m is n)
print("m is not n:", m is not n)
#Create a string text = "Python Programming" Check if "Python" is in text and if "Java" is not in text.
text = "Python Programming"
print("Python" in text)
print("Java" not in text)
#Write a Python program to print all keywords using the keyword module.
import keyword
print("Python keywords:", keyword.kwlist)
#Declare: name = "Ali", age = 20, height = 5.9, Print their values and data types using the type() function.
name = "Ali"
age = 20
height = 5.9
print(name, type(name))
print(age, type(age) )
print(height, type(height))
#Write 5 valid variable names (e.g, user_name, x1, _value, TotalAmount, data123). Also write 3 invalid ones (as comments): 1name, user-name, class. Explain why invalid names are not allowed.
user_name_valid = "Rafia"
x1_valid= 1
_value_valid = 10
TotalAmount_valid = 500
data123_valid = "done"
#1name = "error"
#user_name = "error"
#class = "error"
print(user_name_valid)
print(x1_valid) 
print(_value_valid) 
print(TotalAmount_valid)
print(data123_valid)
#Create special-naming variables: _hidden = 5, __private = 10, MAX_SIZE = 100. Print their values.
_hidden = 5
__private = 10
MAX_SIZE = 100
print(_hidden) 
print(__private) 
print(MAX_SIZE )
#Assign values in one line: x = 1, y = 2, z = 3. Print them.
x, y, z, = 1, 2, 3
print(x, y, z)
#Assign same value 0 to a, b, c in one line. Print them.
a = b = c = 0
print(a, b, c)
#Create temp = 100, print it, delete it using del, then try to print again and observe the error.
temp = 100
print(temp)
del temp
try:
    print(temp) 
except NameError as e:
    print("Error:", e)
#Create a string using triple single quotes: "Helo" Print it.
single_quote_str = '''Hello'''
print(single_quote_str)
#**Create a multi-line string using triple duoble quotes: """This is line one./nThis is line two. """ Print it.**
multi_line = """This is line one./nThis is line two."""
print(multi_line)
#**use type() to check and print the data types of: An integer, A float, A string, A boolean.**
num = 10
print("Value:", num, "Type:", type(num))
a = 3.14
print("Value:", a, "Type:", type(a))
name = "Rafia"
print("Value:", name, "Type:", type(name))
is_active = True
print("Value:", is_active, "Type:", type(is_active)) 
#Create score = 85 Check: score > 50 and score < 100. Print the result.
score = 85
result = score > 50 and score < 100
print(result)
#Create message = "Welcome to Python" Use in and not in to check for word "Python" Print the result.
message = "Welcome to Puython"
print("Python" in message)
print("java" not in message)
#Write a code block using only comments that explains what your program does.
# This program demonstrates:
# - string operation
# - variable assignments
# - type checking 
# - logical & membership operations
#Create data = 123 Use id(data) to print its memory address.
data = 123
print("Memory address of data:", id(data))