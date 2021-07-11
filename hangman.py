import string
from words import choose_word
from images import IMAGES

# End of helper code
# -----------------------------------

name=input("enter name****** ")
def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: ek string word jo ki user ko guess karna hai
    letters_guessed: ek list hai, jisme wo letters hai jo ki user nai abhi tak guess kare hai
    returns: return True kare agar saare letters jo ki user ne guess kiye hai wo secret_word mai hai, warna no
      False otherwise
    '''
    if secret_word == get_guessed_word(secret_word, letters_guessed):
            return True
    return False
# Iss function ko test karne ke liye aap get_guessed_word("kindness", [k, n, d]) call kar sakte hai
def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: ek string word jo ki user ko guess kar raha hai
    letters_guessed: ek list hai, jisme wo letters hai jo ki user nai abhi tak guess kare hai
    returns: ek string return karni hai jisme wo letters ho jo sahi guess huye ho and baki jagah underscore ho.
    eg agar secret_word = "kindness", letters_guessed = [k,n, s]
    to hum return karenge "k_n_n_ss"
    '''
    index = 0
    guessed_word = ""
    while (index < len(secret_word)):
        if secret_word[index] in letters_guessed:
            guessed_word += secret_word[index]
        else:
            guessed_word += "_"
        index += 1
    return guessed_word
def get_available_letters(letters_guessed):
    '''
    letters_guessed: ek list hai, jisme wo letters hai jo ki user nai abhi tak guess kare hai
    returns: string, hame ye return karna hai ki kaun kaun se letters aapne nahi guess kare abhi tak
    eg agar letters_guessed = ['e', 'a'] hai to humme baki charecters return karne hai
    jo ki `bcdfghijklmnopqrstuvwxyz' ye hoga
    '''
    import string
    all_letters = string.ascii_lowercase
    letters_left = ""

    for letter in all_letters:
        if letter not in letters_guessed:
            letters_left += letter
    return letters_left

def if_valid(user):
    if user.isalpha(): #isalpha is used to string handling. if all characters in the string are alphabets this method returns true.
        return True
    if len(user)==1:
        return True
    else:
        return "invalid"

def get_hint(secret_word, letters_guessed):
    '''
    secret_word: ek string word jo ki user ko guess karna hai
    letters_guessed: ek list hai, jisme wo letters hai jo ki user nai abhi tak guess kare hai
    returns: ek character jo abhi tak guess nahi hua hai
    '''

    import random
    letters_not_guessed = []
    index = 0
    while (index < len(secret_word)):
        letter = secret_word[index]
        if letter not in letters_guessed:
            if letter not in letters_not_guessed:
                letters_not_guessed.append(letter)

        index += 1

    return random.choice(letters_not_guessed)

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    Hangman game yeh start karta hai:
    * Game ki shuruaat mei hi, user ko bata dete hai ki
      secret_word mei kitne letters hai
    * Har round mei user se ek letter guess karne ko bolte hai
    * Har guess ke baad user ko feedback do ki woh guess uss
      word mei hai ya nahi
    * Har round ke baad, user ko uska guess kiya hua partial word
      display karo, aur underscore use kar kar woh letters bhi dikhao
      jo user ne abhi tak guess nahi kiye hai
    '''
    print ("Welcome to the game, Hangman!")
    print( "I am thinking of a word that is " + str(len(secret_word)) + " letters long.")
    print("**********"+name+"**********")
    print ("")
    j=0
    while j<1:
        choice=input("Aap abhi kitni difficulty par yeh game khelna chahte ho?\na)\tEasy\nb)\tMedium\nc)\tHard\n\nApni choice a, b, ya c ki terms mei batayein\n")
        if choice=="a":
            remaining_lives=8
            image_selection=[0, 1, 2, 3, 4, 5, 6, 7]
            j+=1
        elif choice=="b":
            remaining_lives=6
            image_selection=[0, 2, 3, 5, 6, 7]
            j+=1
        elif choice=="c":
            remaining_lives=4
            image_selection=[1, 3, 5, 7]
            j+=1
        else:
            continue
    letters_guessed = []
    count=0
    c=0
    # remaining_lives = image_selection
    while (remaining_lives>0):
        available_letters = get_available_letters(letters_guessed)
        print( "Available letters: " + available_letters)
        print("******************************")
        print("******************************")
        guess = input("Please guess a letter / hint: ")
        letter = guess.lower()
        if letter=="hint":
            if count==0:
                print("your hint for this secret word is this --"+ get_hint(secret_word,letters_guessed))
                count+=1
            else:
                print("hint alrady used")
        if letter not in get_available_letters(letters_guessed):
            continue
        if not if_valid(letter):
           continue
        if letter in secret_word:
            letters_guessed.append(letter)
            print ("Good guess: " + get_guessed_word(secret_word, letters_guessed))
            print ("")
            print(letters_guessed)
            if is_word_guessed(secret_word, letters_guessed)== True:
                print (" * * Congratulations, you won! * * ")
                print( "")
                break
        else:
            print ("Oops! That letter is not in my word: " + get_guessed_word(secret_word, letters_guessed))
            print (IMAGES[image_selection[c]])
            c+=1
            remaining_lives -= 1
            print ("Remaining Lives : ", remaining_lives)
            print ("")
            if c==len(image_selection):
                print("out of move plz try again")
                break

    else:
        print ("Sorry, you ran out of guesses. The word was " + str(secret_word) + ".")
    
# Load the list of words into the variable wordlist
# So that it can be accessed from anywhere in the program
secret_word = choose_word()
hangman(secret_word)