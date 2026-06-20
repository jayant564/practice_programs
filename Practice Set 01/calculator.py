# Create a menu-driven calculator:
# 1 Addition
# 2 Subtraction
# 3 Multiplication
# 4 Division
# 5 Modulus
# User enters choice first.
# Then numbers.
# Perform operation.

op = input("Enter operators:\n1 Addition\n2 Subtraction\n3 Multiplication\n4 Division\n5 Modulus\n")
num1 = int(input("Enter number1: "))
num2 = int(input("Enter number2: "))
if op=='1': print(f"{num1} + {num2} = {num1 + num2}")
elif op=='2': print(f"{num1} - {num2} = {num1 - num2}")
elif op=='3': print(f"{num1} * {num2} = {num1 * num2}")
elif op=='4': print(f"{num1} / {num2} = {num1 / num2}")
elif op=='5': print(f"{num1} % {num2} = {num1 % num2}")
