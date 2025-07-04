#Write a program that checks if a number is positive or negative. If it is zero, print "Zero."
num = int(input("Enter a number: "))
if num > 0:
    print("Positive number:")
elif num < 0:
    print("Negative number:")
else:
    print("Zero")
#Input a number from the user and print whether it is even or odd.
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even number:")
else:
    print("Odd number:")
# Ask the user to enter their age. If age is 18 or above, print "Eligible to vote." Else, print "Not eligible."
age = int(input("Enter a age: "))
if age >= 18:
    print("Eligible to vote:")
else:
    print("Not eligible:")
#Enter a number and check whether it is divisible by: 3, 5, Both. Print an appropriate message.
num = int(input("Enter a number: "))
if num % 3 == 0 and num % 5 == 0:
    print("Divisible by both 3 and 5:")
elif num % 3 == 0:
    print("Divisible by 3:")
elif num % 5 == 0:
    print("Divisible by 5:")
else:
    print("Not divisible by 3 or 5:")
#**Ask for a student's marks and assign a grade: 90+ "A+",80+ "A",, 70+ "B" Otherwise "Fail".
marks = int(input("Enter your marks: "))
if marks >= 90:
    print("Grade: A+")
elif marks >= 80:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
else:
    print("Grade: Fail")
#**Take a temperature input: Above 40 "Too Hot", Below 10 "Too cold" Otherwise "Moderate weather"**.
temp = float(input("Enter temperature: "))
if temp > 40:
    print("Too Hot:")
elif temp < 10:
    print("Too cold:")
else:
    print("Moderate weather:")
#Ask the user to enter a year. Check whether it is a leap yaer or not.
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year:")
else:
    print("Not a leap year:")
#Input three numbers and print the largest one.
a= int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a >= b and a >= c:
    print("Largest:", a)
elif b >= a and b>= c:
    print("Largest:", b)
else:
    print("Largest:", c)
#Ask the user to enter a password. If password matches "admin123" print "Access granted", Else "Access denied".
password = input("Enter password: ")
if password == "admin123":
    print("Access grainted: ")
else:
    print("Access denied: ")
#**Take an integer input. If number > 0, check if it's less than 100. Print appropriate messages for both checks*.
num = int(input("Enter an integer: "))
if num > 0:
    print("Positive number: ")
if num < 100:
    print("Number is 100 or greater: ")
else:
    print("Number is zero or negative: ")