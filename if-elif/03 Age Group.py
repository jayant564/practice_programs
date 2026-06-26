# Ask the use to enter their age and determine if they are a 
# child (0-12 years), a teenager (13-19 years), an adult (20-59 years), 
# or a senior citizen (60+ years)

age = int(input("Enter your age: "))

if age < 0:
    print("Invalid Age")
elif age <= 12:
    print("Child")
elif age <= 19:
    print("Teenager")
elif age <= 59:
    print("Adult")
else:
    print("Senior Citizen")