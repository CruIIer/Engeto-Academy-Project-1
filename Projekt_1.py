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
user = input("username: ").lower()
password = input("password: ")
print(separator)

######## KONTROLA VSTUPNÍCH ÚDAJŮ ########
 
if user not in users and password not in passwords:
    print("unregistered user, terminating the program...")
    exit()

if (user == "bob" and password == "123" or
user == "ann" and password == "pass123" or
user == "mike" and password == "password123" or
user == "liz" and password == "pass123"):
    print(f"Welcome to the app, {user}")  
  
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
vybrany_text = vybrany_text.split()
"""MUSÍM PŘEPSAT PROMĚNNOU VYBRANY_TEXT_SLOVA VE FOR CYKLU
DO KTERÉ SE BUDOU UKLÁDAT NOVĚ VYTVOŘENÁ OČIŠTĚNÁ SLOVA
ALE TÍM PÁDEM MUSÍM PŘEPSAT VŠECHNY PROMĚNNÉ DOLE
TAK SI DÁVEJ POZOR, CO PŘESNĚ DĚLÁŠ"""
vybrany_text_slova = []
for slovo in vybrany_text:
    ciste_slovo = slovo.strip(".,:;-!?")
    vybrany_text_slova.append(ciste_slovo)

pocet_slov = len(vybrany_text_slova)
print(f"There are {pocet_slov} words in the selected text.")

######## POČET SLOV ZAČÍNAJÍCÍCH VELKÝM PÍSMENEM ########
slova_zacinajici_velkym = []
for slovo in vybrany_text_slova:
    if slovo.istitle() and not slovo.isnumeric():
        slova_zacinajici_velkym.append(slovo)

print(f"There are {len(slova_zacinajici_velkym)} titlecase words.")

######## POČET SLOV VELKÝMI PÍSMENY ########
slova_malymi = []
for slovo in vybrany_text_slova:
    if slovo.isalpha() and slovo.isupper():
        slova_malymi.append(slovo)
print(f"There are {len(slova_malymi)} uppercase words")

######## POČET SLOV MALÝMI PÍSMENY ########
slova_malymi = []
for slovo in vybrany_text_slova:
    if slovo.isalpha() and slovo.islower():
        slova_malymi.append(slovo)
print(f"There are {len(slova_malymi)} lowercase words")


######## POČET ČÍSEL ########
cisla = []
for cislo in vybrany_text_slova:
    if cislo.isnumeric():
        cisla.append(cislo)
print(f"There are {len(cisla)} numeric strings.")

######## SOUČET VŠECH ČÍSEL ########
cisla_int = []
for cislo in cisla:
    cisla_int.append(int(cislo))
print(f"The sum of all numbers is {sum(cisla_int)}")

######## SLOUPCOVÝ GRAF ########
print(separator)
