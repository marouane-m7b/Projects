import math

def palindrome(word:str):
    word = word.upper()
    flip_word = word[::-1]
    return word == flip_word

my_word = input('word :')
print(palindrome(my_word))