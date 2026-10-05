import string
import random

all_characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

def get_password_length():
    while True:
        try:
            password_character_length = int(input("How long do you want your password length: "))
            if password_character_length < 4:
                print("Can't be used......")
            else:
                return password_character_length
        except ValueError:
            print("That's not a valid number! Try again.")
def generate_password():
    password_character_length = get_password_length()
    password_characters = []

    for i in range(password_character_length):
        password_characters.append(random.choice(all_characters))
    password = "".join(password_characters)
    print(password)
    with open("password.txt","a") as file:
        file.write(password + "\n")
                
while True:
    generate_password()
    again = input("do you want to generate another password? (y/n):")
    if again != "y":
        break                                  # print(password_characters)