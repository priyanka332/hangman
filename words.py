import string
import random

def load_words():
    """
    Ye function kaafi jayada words ko load karne mai help karega
    """
    file=open("words.txt","r")
    list=file.read().split()
    return list
def choose_word():
    """
    word_list (list): list of words (strings)
    ye function ek word randomly return karega
    """
    data = load_words()
    secret_word = random.choice(data)
    secret_word = secret_word.lower()

    return secret_word
print(choose_word())


