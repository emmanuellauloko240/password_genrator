import string
import random

all_characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

def get_password_length():
    while True:
        try:
            password_character_length = int(input("How long do you want your password length: "))
            return password_character_length
        except ValueError:
            print("That's not a valid number! Try again.")
password_character_length = get_password_length()
password_characters = []

for i in range(password_character_length):
    password_characters.append(random.choice(all_characters))
password = "".join(password_characters)
print(password)
            # print(password_characters)
