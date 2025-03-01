import random
import string

def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):
    char_set = ""
    if use_letters:
        char_set += string.ascii_letters
    if use_numbers:
        char_set += string.digits
    if use_symbols:
        char_set += string.punctuation

    if not char_set:
        raise ValueError("No character types selected for password generation!")

    password = ''.join(random.choice(char_set) for _ in range(length))
    return password

# User input for password length and character types
length = int(input("Enter password length: "))
use_letters = input("Include letters (y/n): ").lower() == 'y'
use_numbers = input("Include numbers (y/n): ").lower() == 'y'
use_symbols = input("Include symbols (y/n): ").lower() == 'y'

password = generate_password(length, use_letters, use_numbers, use_symbols)
print(f"Generated password: {password}")
