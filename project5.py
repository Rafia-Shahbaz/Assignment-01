#Takes input: name, age, height, skills (list), hobbies (set), and profile summary (multi-line string)
#Convert data using casting where needed
#Use math to calculate BMI, datetime for birth year, os for current directory

#Store all info in a dictionary and display with a loop
#Check if any skills are Python keywords
#Create functions: calculate_bmi(), profile_summary(), display_info()
#Convert skills to frozenset and hobbies to list
#Use conditions to classify user as Beginner, Intermediate, or Expert
#Use calendar.month() to show joining month
import math
import os
from datetime import datetime
import calendar
import keyword
def calculate_bmi(weight, height):
    height_m = height / 100
    bmi = weight / (height_m ** 2)
    return round(bmi, 2)
def profile_summary(summary):
    print("\n Profile Summary: ")
    print(summary)
def display_info(user_profile):
    print("\n User Profile Information: ")
    for key, value in user_profile.items():
        print(f"{key.capitalize()}: {value}")
name = input("Enter yuor name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height in cm: "))
weight = float(input("Enter your weight in kg: "))
skills_input = input("Enter your skills (comma seperated): ")
skills = [skill.strip() for skill in skills_input.split(',')]
hobbies_input = input("Enter your hobbies (comma separated): ")
hobbies = set(hobby.strip() for hobby in hobbies_input.split(','))
print("Enter your profile summary (type'END' on a new line to finish): ")
summary_lines = []
while True:
    line = input()
    if line.strip().upper() == "END":
        break
    summary_lines.append(line)
summary = "\n".join(summary_lines)
bmi = calculate_bmi(weight, height)
birth_year = datetime.now().year - age
skills_frozen = frozenset(skills)
hobbies_list = list(hobbies)
joining_month = datetime.now().month
joining_month_name = calendar.month_name[joining_month] 
current_directory = os.getcwd()
if len(skills) <= 2:
    level = "Beginner"
elif 3 <= len(skills) <= 5:
    level = "Intermediate"
else:
    level = "Expert"
keyword_skills = [skill for skill in skills if keyword.iskeyword(skill)]
user_profile = {"name": name, "age": age, "height(cm)": height, "weight(kg)": weight, "BMI": bmi, "birth_year": birth_year, "skills": skills_frozen, "hobbies": hobbies_list, "level": level, "keywords_in_skills": keyword_skills, "joining_month": joining_month_name, "profile_summary": summary, "current_directory": current_directory}
display_info(user_profile)
profile_summary(summary)