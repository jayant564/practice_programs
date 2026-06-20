# Input electricity units.
# Bill calculation:
# 0-100      -> ₹5/unit
# 101-200    -> ₹7/unit
# 201+       -> ₹10/unit
# Calculate total bill.

eleunt = int(input("Enter electricity units: "))
if (0<=eleunt<101):
    print(f"total bill = {eleunt * 5} INR")
elif (100<eleunt<201):
    print(f"total bill = {eleunt * 7} INR")
else:
    print(f"total bill = {eleunt * 10} INR")
