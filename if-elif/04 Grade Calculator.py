# WAP that asks for a score (0-100) and prints the corresponding grade
# 90-100: A
# 80-89: B
# 70-79: C
# 60-69: D
# Below 60: F


score = int(input("Enter your score: "))

if score < 0 or score > 100:
    print("Invalid Score")
elif score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")