# Use math.sqrt() to find the square root of a number
import math
num = 6
square_root = math.sqrt(num)
print("Square root", square_root)
#Find the value of π using math.pi and multiply it by 2
import math
pi = 2 * math.pi
print(pi)
# Use math.pow(x, y) to find 4³
import math
power = math.pow(4,3)
print(power)
#Get the current date and time using datetime.datetime.now()
import datetime
y = datetime.datetime.now()
print("Current date and time:", y)
#Print today's date using datetime.date.today()
import datetime
y = datetime.date.today()
print("Today's date:", y)
# Print the calendar for August 2025 using calendar.month()
import calendar
m = calendar.month(2025,8)
print(m)
# Use calendar.isleap() to check if 2024 is a leap year
import calendar
l = calendar.isleap(2024)
print("Is a leap year? ", l)
#alculate the number of days between two dates
import datetime
date1 = datetime.date(2025, 7, 21)
date2 = datetime.date(2025, 8, 5)
days_difference = date1 - date2
print("Days between", date1, "and", date2, ":", days_difference)
#Create a user-defined function that adds 5 days to the current date
def add_five_days():
    return datetime.date.today() + datetime.timedelta(days=5)
print("Date after adding 5 days: ", add_five_days())
#Format the current date into DD-MM-YYYY using .strftime()
import datetime
formatted_date = datetime.date.today().strftime("%d-%m-%y")
print("Formatted date: ", formatted_date)