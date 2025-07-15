#Take input for 5 students (name, age, city, and 3 subject scores as strings)
#Store data using lists, tuples, and dictionaries
#Use type casting to convert scores to integers
#Calculate total, average (using statistics.mean()), and grade using if-elif-else
#Define functions: calculate_grade(), is_passed(), display_student_info()
#Store results in a set, remove duplicates, and convert to frozenset
#Use datetime to log current report time
#Use math to find square root of total marks
#Use keyword to check if names are Python keywords
#Display data types using type()
#Use os to print current working directory
#Print final results using loops and conditions
import statistics
import datetime
import math
import keyword
import os
students_data = []
unique_reports = set()
for i in range(5):
    print(f"\nEnter data for student {i+1}:")
    name = input("Enter name: ")
    age = input("Enter age: ")
    city = input("Enter city: ")
    sub1 = input("Enter score of subject 1: ")
    sub2 = input("Enter score of subject 2: ")
    sub3 = input("Enter score of subject 3: ")
    scores = (int(sub1), int(sub2), int(sub3))
    student = {"name": name, "age": age, "city": city, "scores": scores}
    students_data.append(student)
def calculate_grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    else:
        return "Fail"
def is_passed(avg):
    return avg >= 40
def display_student_info(student):
    scores = student["scores"]
    total = sum(scores)
    avg = statistics.mean(scores)
    grade = calculate_grade(avg)
    passed = is_passed(avg)
    sqrt_total = math.sqrt(total)
    is_keyword = keyword.iskeyword(student["name"])
    current_time = datetime.datetime.now()
    print("\n--- Student Report ---")
    print(f"Name: {student['name']}")
    print(f"Age: {student['age']}")
    print(f"City: {student['city']}")
    print(f"Scores: {scores}")
    print(f"Total Marks: {total}")
    print(f"Average: {avg:.2f}")
    print(f"Grade: {grade}")
    print(f"Passed: {'Yes' if 'passed' else 'Failed'}")
    print(f"Square root of total: {sqrt_total:.2f}")
    print(f"Is name a Python keword? {is_keyword}")
    print(f"Data types: name({type(student['name'])}), age({type(student['age'])}), scores({type(student['scores'])})")
    print(f"Report generated at: {datetime.datetime.now()}")
    print(f"Current Directory: {os.getcwd()}")
    print("-" * 30)
    unique_reports.add((student["name"], total, grade))
final_frozen = frozenset(unique_reports)
for student in students_data:
    display_student_info(student)
print("\n Final Frozen Report Summary: ")