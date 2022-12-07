import random

words_to_guess = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'
words = words_to_guess.split()

guesses = ''
turns = 10
secret_letter = random.choice(words)

while turns > 0:
    failed = 0
    for char in secret_letter:
        if char in guesses:
            print(char, end= ' ')
 
        else:
            print('_')
            failed += 1
        
    if failed == 0:
        print('You Won')
        print('The word is: ', secret_letter)
        break
    
    print()
    guess = input('Guess a character please:')
    
    guesses += guess
    
    if guess not in secret_letter:
        turns -= 1
        print('Wrong character')
        
        print('You have', + turns, 'more guesses')
        
        if turns == 0:
            print('You Lost')