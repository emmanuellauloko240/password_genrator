# Password Generator

A simple command-line Python program that generates a random, secure password and saves it to a file for safekeeping.

## How to Run

1. Make sure you have Python 3 installed.
2. Clone this repository:
```bash
   git clone https://github.com/emmanuellaenenu/password-generator.git
```
3. Navigate into the project folder:
```bash
   cd password-generator
```
4. Run the program:
```bash
   python3 password_generator.py
```

## Features

- Generates a random password using letters, numbers, and symbols
- Lets the user choose the password length
- Rejects lengths shorter than 4 characters (for basic security)
- Saves every generated password to `password.txt`
- Lets the user generate multiple passwords in one session

## What I Learned

Building this project helped me understand:

- Lists and how to build/append to them
- Loops (`for` and `while`) and how to control them
- Functions, including `return` values
- Handling invalid input with `try`/`except`
- Reading and writing files in Python
- Using `.gitignore` to keep sensitive files out of GitHub