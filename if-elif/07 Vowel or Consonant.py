# Ask user to input character and check if it is a vowel or consonant

ch = input("Enter a character: ")

if ch.lower() in "aeiou":
    print("Vowel")
else:
    print("Consonant")