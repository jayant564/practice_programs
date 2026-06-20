# Input purchase amount.
# Discount:
# 5000+  -> 20%
# 2000+  -> 10%
# Else   -> No discount
# Print final amount.

amnt = int(input("Enter amount: "))
dscnt = 0
if (amnt>=5000):
    dscnt = (amnt * 0.2)
    print(f"Final amount = {amnt - dscnt}")
elif (2000<=amnt<5000):
    dscnt = (amnt * 0.1)
    print(f"Final amount = {amnt - dscnt}")
else:
    print(f"No discount.\nFinal amount = amnt")