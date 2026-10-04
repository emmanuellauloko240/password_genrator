import string
import secrets

def get_password_length():
    while True:
        try:
            length = int(input("Enter desired password length: "))
            if length < 4:
                print("Password length should be at least 4.")
            else:
                return length
        except ValueError:
            print("Invalid number! Please enter an integer.")

def get_character_pool():
    pool = ""
    if input("Include lowercase letters? (y/n): ").lower() == 'y':
        pool += string.ascii_lowercase
    if input("Include uppercase letters? (y/n): ").lower() == 'y':
        pool += string.ascii_uppercase
    if input("Include digits? (y/n): ").lower() == 'y':
        pool += string.digits
    if input("Include punctuation? (y/n): ").lower() == 'y':
        pool += string.punctuation
    if not pool:
        pool = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    return pool

def generate_password(length, pool):
    return ''.join(secrets.choice(pool) for _ in range(length))

password_length = get_password_length()
character_pool = get_character_pool()
password = generate_password(password_length, character_pool)

print("\nYour secure password is:", password)


