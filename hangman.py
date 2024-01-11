import random
import string
from words import words

def getValidWord(words):
    word = random.choice(words)
    while '_' in word or '' in word:
        word = random.choice(words)
    return word.upper()

def hangman(): 
    word = getValidWord(words)
    word_letter = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    
    while len(word_letter)>0:
        print("You have used these letters: ", " ".join(used_letters))
        
        word_list =[letter if letter in used_letters else '_' for letter in word]
        print('current word: ',' '.join(word_list))  

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letter :
                word_letter.remove(user_letter)
    
            elif user_letter in used_letters:
                print("You have already used that character. Please try again.")       
        else:
            print("Invalid character. please try again. ") 
    
hangman()    
userInput = input("Type something: ")    
print(userInput) 