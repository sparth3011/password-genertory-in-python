# -*- coding: utf-8 -*-
"""password generator.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sscJm1VBBOqSASC0u9fYi2RBwUXjSZx7
"""

import random

def generate_password():
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+{[]}\|;:'\",./?"
    big_alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    small_alphabets = "abcdefghijklmnopqrstuvwxyz"
    numbers = "0123456789"
    special_characters = "!@#$%^&*()-_=+{[]}\|;:'\",./?"

    password = ""
    for i in range(8):
        character = random.choice(characters)
        if i == 0:
            while character not in big_alphabets:
                character = random.choice(characters)
        elif i == 1:
            while character not in small_alphabets:
                character = random.choice(characters)
        elif i == 2:
            while character not in numbers:
                character = random.choice(characters)
        else:
            while character not in special_characters:
                character = random.choice(characters)

        password += character

    return password

def main():
    password = generate_password()
    print(f"Your password is: {password}")

if __name__ == "__main__":
    main()