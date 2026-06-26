# WAP asks for the temperature and prints whether it is 
# cold (<15°C), Warm (15-25°C), or Hot (>25°C)

temperature = float(input("Enter temperature: "))

if temperature < 15:
    print("Cold")
elif temperature <= 25:
    print("Warm")
else:
    print("Hot")