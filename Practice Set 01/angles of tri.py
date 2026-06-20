# Input three angles.
# Check whether they can form a triangle.
# Hint: Sum must be 180

agl1 = int(input("Enter angle: "))
agl2 = int(input("Enter angle: "))
agl3 = int(input("Enter angle: "))
if (agl1==agl2==agl3!=180) and (agl1 + agl2 + agl3)==180:
    print("triangle")
else:   print("not triangle")
