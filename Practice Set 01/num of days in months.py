# Input a month number (1–12).
# Print the number of days.
# Ignore leap years.

mnth = int(input("Enter month number(1-12): "))
if (mnth==2):
    print("28 days")
elif (mnth==1 or 3 or 5 or 7 or 8 or 10 or 12):
    print("31 days") 
elif (mnth==4 or 6 or 9 or 11):
    print("30 days")
else:
    print("try again")