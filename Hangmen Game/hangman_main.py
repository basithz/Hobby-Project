from hangman_pic import hangman

import random

def guess_word(): #to choose random word to guess
    word=random.choice(words)
    print("Guess the fruit name ?")
    return word

def is_present(letter): # if checking by letter is chosen, to check whether user entered letter present in word or not 
    if letter.lower() in word.lower():
        return letter.lower()
    else:
        False

def fill_blank(letter): #to fill the dash with appropriate letter at correct position
    global d,word
    d=list(d)
    for i,l in enumerate(word):
        if letter == l:
            d[i]=letter
    print("".join(d))

def make_hangman(): #if user entered wrong letter then the hangman will be printed( total 6 chances)
    global chances
    chances += 1
    print(hangman[chances])
        

def check_letter(user_choice): #if the user enter letter by letter to fill the dash
    letter = is_present(user_choice)
    if letter:
        fill_blank(letter)
    else:
        make_hangman()
    

def check_word(user_choice): #if the user enter the whole word, only 1 chance
    if user_choice.lower == word.lower:
        return True
    else:
        return False

words=["banana","watermelon","apple","mango","orange","kiwi","grape"]
word=guess_word()
d=("-"*len(word))
print(d)
print(hangman[0])
chances=0
is_win = False

while chances<=5 and not is_win:
    user_choice=input()
    if len(user_choice)==1:
        check_letter(user_choice)
    else:
        is_win = check_word(user_choice)
        break
    
    if "-" not in d:
        is_win = True


        
if is_win:
    print("you win ")
else:
    print("you lost")
