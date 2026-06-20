# Input three sides.
# Determine:
# Equilateral
# Isosceles
# Scalene

a = int(input("Enter sides: "))
b = int(input("Enter sides: "))
c = int(input("Enter sides: "))
if (a==b==c):
    print("equi tri")
elif (a==b!=c) or (a==c!=b) or (b==c!=a):
    print("isosceles tri")
else:
    print("scalene tri")
