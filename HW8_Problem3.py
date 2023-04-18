# Maahir Vohra
# CS100 Section 008
# HW 08, March 23, 2023

def enterNewPassword():
    while True:
        password = input("Please enter a password: ")
        if len(password) < 8 or len(password) > 15:
            print("The password must be between 8-15 digits.")
            continue
        if not any(char.isdigit() for char in password):
            print("The password must contain at least one digit.")
            continue
        return password


print(enterNewPassword())
