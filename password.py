import secrets
import string

def generate_password(length, min_uppercase=1, min_lowercase=1, min_digits=1, min_special=1):
    
    if length < min_uppercase + min_lowercase + min_digits + min_special:
        raise ValueError("Password length is too short for the given character requirements.")
    
   
    uppercase_chars = string.ascii_uppercase
    lowercase_chars = string.ascii_lowercase
    digit_chars = string.digits
    special_chars = string.punctuation

    password = []

    
    for _ in range(min_uppercase):
        password.append(secrets.choice(uppercase_chars))

    for _ in range(min_lowercase):
        password.append(secrets.choice(lowercase_chars))

    for _ in range(min_digits):
        password.append(secrets.choice(digit_chars))

    for _ in range(min_special):
        password.append(secrets.choice(special_chars))

    
    remaining_length = length - len(password)
    all_chars = uppercase_chars + lowercase_chars + digit_chars + special_chars

    for _ in range(remaining_length):
        password.append(secrets.choice(all_chars))

    secrets.SystemRandom().shuffle(password)

    return ''.join(password)


password_length = int(input("Enter the desired length of the password: "))
min_uppercase = int(input("Enter the minimum number of uppercase letters: "))
min_lowercase = int(input("Enter the minimum number of lowercase letters: "))
min_digits = int(input("Enter the minimum number of digits: "))
min_special = int(input("Enter the minimum number of special characters: "))

try:
    
    generated_password = generate_password(password_length, min_uppercase, min_lowercase, min_digits, min_special)
    print(f"Generated password: {generated_password}")
except ValueError as ve:
    print(ve)