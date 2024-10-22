import string
import random


chars = []
symbols = []
numbers = []

if input('Do you want to add chars to your password?(y/n): ').lower() == 'y':
    char_len = int(input("How many chars do you want to see in password?: "))
    chars = [random.choice(string.ascii_lowercase) for _ in range(char_len)]

if input('Do you want to add symbols to your password?(y/n): ').lower() == 'y':
    symb_len = int(input("How many symbols do you want to see in password?: "))
    symbols = [random.choice(string.punctuation) for _ in range(symb_len)]

if input('Do you want to add numbers to your password?(y/n): ').lower() == 'y':
    num_len = int(input("How many numbers do you want to see in password?: "))
    numbers = [random.choice(string.digits) for _ in range(num_len)]

print(numbers)
print(symbols)
print(chars)

password = numbers + chars + symbols
print(password)

random.shuffle(password)

password = ''.join(password)

print(password)
