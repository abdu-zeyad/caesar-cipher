import re
import nltk
from nltk.corpus import words, names
nltk.download('words', quiet=True)
nltk.download('names', quiet=True)
word_list = words.words()
name_list = names.words()


def encrypt(plain_text, shifted):


    encrypted = ""
    # # In Python, the ord() function accepts a string of unit length as an argument 
    # and returns the Unicode equivalence of the passed argument. 
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


def crack(ciphertext):
    for i in range(26):
        word_decrypted =  decrypt(ciphertext,i)
        word = re.sub(r'[^A-Za-z]+','', word_decrypted)
        if word.lower() in word_list or word in name_list:
            print(word_decrypted)

encrypted_word = encrypt('Hello!3', 7)
decrypted_word= decrypt(encrypted_word, 7)
decrypted_word_without_thekey = crack(encrypted_word)






