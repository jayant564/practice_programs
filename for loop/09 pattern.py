# WAP print right angled triangle ⊿ pattern

for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()




# If the pattern should print numbers:
for i in range(1, 6):
    for j in range(i):
        print(j + 1, end=" ")
    print()