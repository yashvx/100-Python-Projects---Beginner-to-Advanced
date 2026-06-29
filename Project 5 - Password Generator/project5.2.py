import random
import string

length = int(input("Enter Length: "))

characters = string.ascii_letters + string.digits + string.punctuation
password = ""

for i in range(length):
    password += random.choice(characters)

print(f"Your password is: {password}")