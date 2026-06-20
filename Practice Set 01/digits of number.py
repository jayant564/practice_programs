# Input a number.
# Check whether it is a 2-digit, 3-digit, or 4-digit number.
# Use abs()

num = int(input("Enter num: "))
if(11<=abs(num)<100):
    print("2-digit")
elif(99<abs(num)<1000):
    print("3-digit")
elif(999<abs(num)<=9999):
    print("4-digit")
else:   print("try again")
