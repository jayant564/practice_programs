# Take three sides of a triangle.
# Check whether a valid triangle can be formed.
# Condition:
# a + b > c
# a + c > b
# b + c > a

a=int(input("Enter side: ")) 
b=int(input("Enter side: ")) 
c=int(input("Enter side: ")) 
if(a+b>c) and (a+c>b) and (b+c>a): 
    print("valid tri") 
else:   print("not valid")