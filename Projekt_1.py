"""
projekt_1.py: první projekt do Engeto Online Python Akademie

autor: Aleš Preclík
email: apreclik@centrum.cz
discord: alda_p
"""

######## VYPSÁNÍ PROMĚNNÝCH ########

separator = print(40*"-")
user = input("username: ")
password = input("password: ")
users = ["bob", "ann", "mike", "liz"]
passwords = ["123", "pass123", "password123"]
welcome = f"Welcome to the app {user}"

######## KONTROLA VSTUPNÍCH ÚDAJŮ ########

separator

if user in users and password in passwords:
    if user == "bob" and password == "123":
        print(welcome)
    elif user == "ann" and password == "pass123":
        print(welcome)
    elif user == "mike" and password == "password123":
        print(welcome)
    elif user == "liz" and password == "pass123":
        print(welcome)
    else:
        print("unregistered user, terminating the program")
        exit()
else:
    print("unregistered user, terminating the program..")
    exit()

######## VÝBĚR TEXTU K ANALÝZE ########

print("/nWe have 3 texts to be analyzed.")
separator
vyber_textu = int(input("Enter a number btw. 1 and 3 to select:"))
separator
if vyber < 1 or vyber > 3:
    print("Chosen number is not in the selection")
elif vyber != type(int):
    print("You must select a number")

######## STATISTIKY TEXTU ########
separator




######## SLOUPCOVÝ GRAF ########
separator
