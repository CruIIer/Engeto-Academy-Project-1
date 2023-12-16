"""
projekt_1.py: první projekt do Engeto Online Python Akademie

autor: Aleš Preclík
email: apreclik@centrum.cz
discord: alda_p
"""


TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.''', 
]

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
number_texts = (len(TEXTS))
number_texts_list = [number for number in range(1, number_texts + 1)]

print(f"We have {number_texts} texts to be analyzed.")
print(separator)
choose_text = input(f"""\
Enter a number btw.\
 {number_texts_list[0]} and {number_texts_list[-1]} to select: \
""")

if choose_text.isnumeric():
    choose_text = int(choose_text)
    if (choose_text < number_texts_list[0] or
        choose_text > number_texts_list[-1]):
        print("wrong number, terminating the program...")
        exit()
else:
    print("you didn't select a number, terminating the program...")
    exit()

######## STATISTIKY TEXTU ########
print(separator)
chosen_text = TEXTS[choose_text - 1]

######## POČET SLOV ########
chosen_text = chosen_text.split()
chosen_text_words = []
for word in chosen_text:
    clean_word = word.strip(".,:;-!?")
    chosen_text_words.append(clean_word)

number_words = len(chosen_text_words)
print(f"There are {number_words} words in the selected text.")

######## POČET SLOV ZAČÍNAJÍCÍCH VELKÝM PÍSMENEM ########
words_capital = [word for word in chosen_text_words
    if word.istitle() and not word.isnumeric()]
print(f"There are {len(words_capital)} titlecase words.")

######## POČET SLOV VELKÝMI PÍSMENY ########
words_upper = [word for word in chosen_text_words
    if word.isalpha() and word.isupper()]
print(f"There are {len(words_upper)} uppercase words")

######## POČET SLOV MALÝMI PÍSMENY ########
words_lower = [word for word in chosen_text_words
    if word.isalpha() and word.islower()]
print(f"There are {len(words_lower)} lowercase words")

######## POČET ČÍSEL ########
words_numbers = [number for number in chosen_text_words
    if number.isnumeric()]
print(f"There are {len(words_numbers)} numbereric strings.")

######## SOUČET VŠECH ČÍSEL ########
words_numbers_sum = [int(number) for number in words_numbers]
print(f"The sum of all numbers is {sum(words_numbers_sum)}")

######## SLOUPCOVÝ GRAF ########
print(separator)
words_graph = chosen_text_words.copy()
words_length = {}
longest_length = 0
for word in words_graph:
    length = len(word)
    if length not in words_length:
        words_length[length] = 1
    else:
        words_length[length] += 1
    
    if length > longest_length:
        longest_length = length

print("LEN | OCCURENCES", "| NUMBER".rjust(17))
for length in range(1, longest_length + 1):
    words_same_len = words_length.get(length, 0)
    line = "*" * words_same_len
    print(f"{length:3} | {line:19} | {words_same_len}")
    
