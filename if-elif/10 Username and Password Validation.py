# create program that asks for a username and password
# If the username is "admin" and the password is "password123", print "Login successful"; otherwise, print "Invalid credentials"

username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "password123":
    print("Login successful")
else:
    print("Invalid credentials")