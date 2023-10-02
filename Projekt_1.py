"""
projekt_1.py: první projekt do Engeto Online Python Akademie

autor: Aleš Preclík
email: apreclik@centrum.cz
discord: alda_p
"""

user = input("username: ")
password = input("password: ")
reg_uzivatele = ["bob", "ann", "mike", "liz"]
passwords = ["123", "pass123", "password123"]


if user == "bob" and password == "123":
    print("Welcome to the app", user)
elif user == "ann" and password == "pass123":
    print("Welcome to the app", user)
elif user == "mike" and password == "password123":
    print("Welcome to the app", user)
elif user == "liz" and password == "pass123":
    print("Welcome to the app", user)
else:
    print("unregistered user, terminating the program")

print("We have 3 texts to be analyzed.")

vyber = int(input("Enter a number btw. 1 and 3 to select:"))
if vyber < 1 or vyber > 3:
    print("Chosen number is not in the selection")
elif vyber != type(int):
    print("You must select a number")


# ---------------

# 6. pro vybraný text spočítá následující statistiky 
# 7. 

# ---------------

