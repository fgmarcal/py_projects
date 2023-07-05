import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

random_password = []
password = ""
if nr_letters < len(letters) and nr_symbols < len(symbols) and nr_numbers < len(numbers):
    for letter in range(nr_letters):    
        random_letter = random.randint(0, (len(letters) - 1))
        pass_letter = letters[random_letter]
        random_password += pass_letter

    for symbol in range(nr_symbols):
        random_symbol = random.randint(0, (len(symbols) - 1))
        pass_symbol = symbols[random_symbol]
        random_password += pass_symbol

    for number in range(nr_numbers):
        random_number = random.randint(0, (len(numbers) - 1))
        pass_number = numbers[random_number]
        random_password += pass_number

    random.shuffle(random_password)
    for char in random_password:
        password += char
        
    print(password)

else:
    print("Invalid selection!")
