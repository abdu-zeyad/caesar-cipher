import re
import nltk
from nltk.corpus import words, names

nltk.download('words', quiet=True)
nltk.download('names', quiet=True)

word_list = words.words()
name_list = names.words()


candidates = [
    "a dark and stormy night",
    "n qnex naq fgbezl avtug",
    "j mjat jwm bcxavh wrpqc",
    "call me Ishmael",
    "Billy Pilgrim has become unstuck in time",
    "All happy families are alike; each unhappy family is unhappy in its own way.",
    '"Where\'s Papa going with that ax?" said Fern to her mother as they were setting the table for breakfast.',
    "Off the hizzle fo shizzle",
]

def count_words(text):
    candidate_words = text.split()

    word_count = 0

    for candidate in candidate_words:
        word = re.sub(r'[^A-Za-z]+','', candidate)
        if word.lower() in word_list or word in name_list:
            # print("english word", word)
            word_count += 1
        else:
            pass
            # print('not english word or name', word)

    return word_count

def encrypt(plain_text, shifted):
# # In Python, the ord() function accepts a string of unit length as an argument 
# and returns the Unicode equivalence of the passed argument. 

    encrypted = ""

    for c in plain_text:

        if c.isupper():  

            letter_index = ord(c) - ord('A')
            index_shifted = (letter_index + shifted) % 26 + ord('A')
            new_letter = chr(index_shifted)
            encrypted += new_letter
        elif c.islower(): 

            # print(ord(c))
            letter_index = ord(c) - ord('a')
            index_shifted = (letter_index + shifted) % 26 + ord('a')
            new_letter = chr(index_shifted)
            encrypted += new_letter
        elif c.isdigit():

            new_number = (int(c) + shifted) % 10
            encrypted += str(new_number)
        else:
            encrypted += c
    return encrypted

def decrypt(ciphertext, shifted):

    decrypted = ""
    for c in ciphertext:
        if c.isupper():

            letter_index = ord(c) - ord('A')
            index_shifted_back = (letter_index - shifted) % 26 + ord('A')
            old_letter = chr(index_shifted_back)
            decrypted += old_letter

        elif c.islower():

            letter_index = ord(c) - ord('a')
            index_shifted_back = (letter_index - shifted) % 26 + ord('a')
            old_letter = chr(index_shifted_back)
            decrypted += old_letter
        elif c.isdigit():

            old_number = (int(c) - shifted) % 10
            decrypted += str(old_number)
        else:
            decrypted += c

    return decrypted


x = encrypt('Hello15', 3)
print(x)
y = decrypt(x, 3)
print(y)



# for phrase in candidates:
#     word_count = count_words(phrase)
#     percentage = int(word_count / len(phrase.split()) * 100)
#     if percentage > 50:
#         print(phrase, percentage
