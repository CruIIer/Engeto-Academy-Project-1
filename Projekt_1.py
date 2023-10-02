"""
projekt_1.py: první projekt do Engeto Online Python Akademie

autor: Aleš Preclík
email: apreclik@centrum.cz
discord: alda_p
"""

from task_template import TEXTS
######## VYPSÁNÍ PROMĚNNÝCH ########

separator = print(40*"-")
user = input("username: ")
password = input("password: ")
users = ["bob", "ann", "mike", "liz"]
passwords = ["123", "pass123", "password123"]
welcome = f"Welcome to the app {user}"

######## KONTROLA VSTUPNÍCH ÚDAJŮ ########
 
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
separator

######## VÝBĚR TEXTU K ANALÝZE ########

num_texts = (len(TEXTS))
num_texts_list = []
for cislo in range(num_texts + 1):
    if cislo == 0:
        continue
    else:
        num_texts_list.append(cislo)

print(f"We have {num_texts} texts to be analyzed.")
separator
vyber_textu = int(input(f"Enter a number btw. {num_texts_list[0]} and {num_texts_list[-1]} to select:"))
separator
if vyber_textu < num_texts_list[0] or vyber_textu > num_texts_list[-1]:
    print("Chosen text is not in selection")
elif vyber != type(int):
    print("You must select a number")

######## STATISTIKY TEXTU ########
separator


######## SLOUPCOVÝ GRAF ########
separator
