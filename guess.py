import random

words = 'my name is mercede'

def get_random_word(word):
    word = word.split()
    word = random.choice(word)
    return word

secret_word = get_random_word(words)
guesses = ''
turns = 5

def get_guess():
    while True:
        guess = input("\n guess a character:")
        guess = guess.lower()
        return guess
        
def win(fail):
    if fail == 0:
        print('won!')
        print('the secret word is: ', secret_word)
        
def loose(guesses, turns):
    if guesses not in secret_word:
        turns -= 1
        print("\n Wrong")
        print("You have", + turns, 'more guesses')
        
        if turns == 0:
            print("You Loose")
            
while True:    
    while turns>0:
        guesses += get_guess()
        fail =0
        for char in secret_word:
            if char in guesses:
                print(char, end= ' ')
            else:
                print('_')
                fail += 1
        break
    win(fail)
    loose(guesses, turns)