import random

import string
from words import words

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word=random.choice(words)

    return word

def hangman():
    word = get_valid_word(words)
    print(word)
    word_letters = set(word)
    print(word_letters)
    alphabet = set(string.ascii_lowercase)
    used_letters = set()
    
    lives =6 

    while len(word_letters)>0 and lives>0 :
        user_letter=input("Guess a letter: ").lower()
       

        
        if user_letter in alphabet - used_letters:
            print("1")
            used_letters.add(user_letter)
            print(used_letters)
            print(user_letter)
            if user_letter in word_letters:
                print("2")
                word_letters.remove(user_letter)
            else:
                lives=lives-1
                print("Letter is not in the word")

        elif user_letter in used_letters:
            print("You have already used that character. Please Try again")

        else:
            print("Invalid character")
        
        print('You have',lives,'left and you have used these leters ',' '.join(used_letters))
        word_list = [letter if letter in used_letters else '-' for letter in word]        
        print('Current words: ',' '.join(word_list))
    if lives ==0:
        print("You died")
    else:
        print("congratulations you guessed the right word")
    

hangman()



