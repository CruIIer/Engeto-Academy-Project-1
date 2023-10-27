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

number_texts = (len(TEXTS))
number_texts_list = []
for number in range(number_texts + 1):
    if number == 0:
        continue
    else:
        number_texts_list.append(number)

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
words_capital = []
for word in chosen_text_words:
    if word.istitle() and not word.isnumeric():
        words_capital.append(word)

print(f"There are {len(words_capital)} titlecase words.")

######## POČET SLOV VELKÝMI PÍSMENY ########
words_upper = []
for word in chosen_text_words:
    if word.isalpha() and word.isupper():
        words_upper.append(word)
print(f"There are {len(words_upper)} uppercase words")

######## POČET SLOV MALÝMI PÍSMENY ########
words_lower = []
for word in chosen_text_words:
    if word.isalpha() and word.islower():
        words_lower.append(word)
print(f"There are {len(words_lower)} lowercase words")


######## POČET ČÍSEL ########
words_numbers = []
for number in chosen_text_words:
    if number.isnumeric():
        words_numbers.append(number)
print(f"There are {len(words_numbers)} numbereric strings.")

######## SOUČET VŠECH ČÍSEL ########
words_numbers_sum = []
for number in words_numbers:
    words_numbers_sum.append(int(number))
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

print("LEN | OCCURENCES | NUMBER")
for length in range(1, longest_length + 1):
    words_same_len = words_length.get(length, 0)
    line = "*" * words_same_len
    print(f"{length} | {line} | {words_same_len}")
    

    
