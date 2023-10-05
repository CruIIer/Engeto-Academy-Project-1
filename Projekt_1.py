"""
projekt_1.py: první projekt do Engeto Online Python Akademie

autor: Aleš Preclík
email: apreclik@centrum.cz
discord: alda_p
"""

from task_template import TEXTS
######## VYPSÁNÍ PROMĚNNÝCH ########

separator = 40*"-"
users = ["bob", "ann", "mike", "liz"]
passwords = ["123", "pass123", "password123"]
user = input("username: ")
password = input("password: ")
welcome = f"Welcome to the app, {user}"
print(separator)

######## KONTROLA VSTUPNÍCH ÚDAJŮ ########
 
if user not in users and password not in passwords:
    print("unregistered user, terminating the program...")
    exit()

if (user == "bob" and password == "123" or
user == "ann" and password == "pass123" or
user == "mike" and password == "password123" or
user == "liz" and password == "pass123"):
    print(welcome)  
  
else:
    print("unregistered user, terminating the program..")
    exit()

######## VÝBĚR TEXTU K ANALÝZE ########

num_texts = (len(TEXTS))
num_texts_list = []
for cislo in range(num_texts + 1):
    if cislo == 0:
        continue
    else:
        num_texts_list.append(cislo)

print(f"We have {num_texts} texts to be analyzed.")
print(separator)
vyber_textu = input(f"""\
Enter a number btw.\
 {num_texts_list[0]} and {num_texts_list[-1]} to select: \
""")

print(separator)
if vyber_textu.isnumeric():
    vyber_textu = int(vyber_textu)
    if (vyber_textu < num_texts_list[0] or
        vyber_textu > num_texts_list[-1]):
        print("wrong number, terminating the program...")
        exit()
else:
    print("you didn't select a number, terminating the program...")
    exit()

######## STATISTIKY TEXTU ########
print(separator)
vybrany_text = TEXTS[vyber_textu - 1]
######## POČET SLOV ########
"""text = "Hello, world!"
znaky_ke_odstraneni = ",! "
novy_text = text
for znak in znaky_ke_odstraneni:
    novy_text = novy_text.replace(znak, "")
print(novy_text)"""




######## SLOUPCOVÝ GRAF ########
print(separator)
