from hangmanWords import *
from random import randint

def hangman():
    words = getwords()
    word = words[randint(0, 2241)]
    print()
    tries = 10
    spaces = []
    wrongLetters = []
    for letter in word:
        spaces.append("_")
    print(spaces)



    while tries > 0:
        guess = input("\nGuess a letter: ")
        if guess == word:
            print("\nYOU WIN!!! GOOD JOB :)\n")
            break
        for index, letter in enumerate(word):
            if guess == letter:
                spaces[index] = guess
                print("\nYou got one right :)\n")
        print(spaces)
        
            

                
                
        if "_" not in spaces:
            print("\nYOU WIN!!! GOOD JOB :)\n")
            break
        if guess not in word:
            tries -= 1
            print("\nOops, you have " + str(tries) + " attempt(s) left.\n")
            wrongLetters.append(guess)
            print("Wrong letters: " + str(wrongLetters) +"\n")
            if tries == 9:
                print('''
    __________
    |     |
    |     
    |     
    |     
    |     
    |_________''')
            if tries == 8:
                print('''
    __________
    |     |
    |     O
    |     
    |     
    |     
    |_________''')
            if tries == 7:
                print('''
    __________
    |     |
    |     O
    |     |
    |     
    |     
    |_________''')
            if tries == 6:
                print('''
    __________
    |     |
    |     O
    |     |-
    |     
    |     
    |_________''')
            if tries == 5:
                print('''
    __________
    |     |
    |     O
    |     |--
    |     
    |     
    |_________''')
            if tries == 4:
                print('''
    __________
    |     |
    |     O
    |    -|--
    |     
    |     
    |_________''')
            if tries == 3:
                print('''
    __________
    |     |
    |     O
    |   --|--
    |     
    |     
    |_________''')
            if tries == 2:
                print('''
    __________
    |     |
    |     O
    |   --|--
    |     |
    |     
    |_________''')
            if tries == 1:
                print('''
    __________
    |     |
    |     O
    |   --|--
    |     |
    |    / 
    |_________''')

    if tries == 0:
        print('''
    __________
    |     |
    |     O
    |   --|--
    |     |
    |    / \\
    |_________''')
        print("\nYou lose :( the correct answer was " + word + ". \n")
        
hangman()