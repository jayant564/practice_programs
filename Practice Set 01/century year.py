# Input a year.
# Check whether it is:
# Century Year
# or
# Not Century Year
# Examples:
# 1900
# 2000
# 2100

year = int(input("Enter year: "))
if (year%100==0):
    print("Century year")
else:
    print("not century year")
