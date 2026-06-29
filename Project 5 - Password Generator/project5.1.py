import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g',
    'h', 'i', 'j', 'k', 'l', 'm', 'n',
    'o', 'p', 'q', 'r', 's', 't', 'u',
    'v', 'w', 'x', 'y', 'z'
]

numbers = [
    '0', '1', '2', '3', '4',
    '5', '6', '7', '8', '9'
]

symbols = [
    '!', '@', '#', '$', '%',
    '^', '&', '*', '(', ')',
    '-', '_', '+', '=', '?'
]

print("Welcome to the PyPassword Generator!")

num_letter = int(input("How many letters do you want in your password? -- \n"))
num_symbol = int(input(f"How many symbols do you want? -- \n"))
num_number = int(input(f"How many numbers do you want? -- \n"))

password_list = []

for char in range(0, num_letter ):
    password_list.append(random.choice(letters))
for char in range(0, num_symbol ):
    password_list.append(random.choice(symbols))
for char in range(0, num_number ):
    password_list.append(random.choice(numbers))

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
    password += char

print(f"Your password is: {password}")