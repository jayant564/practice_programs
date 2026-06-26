# WAP that checks if a Δ is equilateral Δ (all sides equal),
# isosceles Δ (two sides equal), or scalene Δ (no sides equal)

side1 = int(input("Enter first side: "))
side2 = int(input("Enter second side: "))
side3 = int(input("Enter third side: "))

if side1 == side2 == side3:
    print("Equilateral Triangle")
elif side1 == side2 or side2 == side3 or side1 == side3:
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")




# Checks for Valid Triangle

# side1 = int(input("Enter first side: "))
# side2 = int(input("Enter second side: "))
# side3 = int(input("Enter third side: "))

# if side1 + side2 <= side3 or side1 + side3 <= side2 or side2 + side3 <= side1:
#     print("Not a valid triangle")
# elif side1 == side2 == side3:
#     print("Equilateral Triangle")
# elif side1 == side2 or side2 == side3 or side1 == side3:
#     print("Isosceles Triangle")
# else:
#     print("Scalene Triangle")