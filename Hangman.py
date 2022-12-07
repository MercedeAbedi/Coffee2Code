import random

HANGMAN_PICS = ['''
            +---+
                |
                |
                |
               ===''', '''
            +---+
            0   |
                |
                |
               ===''', '''
               +---+
            0   |
            |   |
                |
               ===''', '''
               +---+
            0   |
           /|   |
                |
               ===''', '''
                +---+
            0   |
           /|\  |
                |
               ===''', '''
                +---+
            0   |
           /|\  |
           /    |
               ===''', '''
               +---+
            0   |
           /|\  |
           / \  |
                ===''']

words_to_guess = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'
words = words_to_guess.split()


def getRandomWords(word_list):
    word_index = random.randint(0, len(word_list) - 1)
    return word_list[word_index]


def displayBoard(missed_letters, correct_letters, secret_words):
    print(HANGMAN_PICS[len(missed_letters)])
    print()
    print('Missed letters:', end=' ')

    for letter in missed_letters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secret_words)

    for i in range(len(secret_words)):
        if secret_words[i] in correct_letters:
            blanks = blanks[:i] + secret_words[i] + blanks[i+1:]

    for letter in blanks:
        print(letter, end=' ')
    print()


def getGuess(already_guessed):
    while True:
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        print('Guess a letter please. ')
        guess = input().lower()
        if len(guess) != 1:
            print('Enter just one letter')
        elif guess in already_guessed:
            print('Choose another letter. This one has been repeated ')
        elif guess not in alphabet:
            print('Choose a LETTER please! ')
        else:
            return guess


def playAgain():
    print('Would you like to play one more time? ')
    return input().lower().startswith('y')


name = input('What is your name? ')
print('Welcome to Hangman Game ',name)
missed_letters = ''
correct_letters = ''
secret_words = getRandomWords(words)
game_is_done = False


while True:
    displayBoard(missed_letters, correct_letters, secret_words)

    guess = getGuess(missed_letters + correct_letters)

    if guess in secret_words:
        correct_letters = correct_letters + guess
        found_all_letters = True
        for i in range(len(secret_words)):
            if secret_words[i] not in correct_letters:
                found_all_letters = False
                break
            if found_all_letters:
                print('You WON!')
                print('The secret word is: ' + secret_words)
                gameIsDone = True
    else:
        missed_letters = missed_letters + guess


        if len(missed_letters) == len(HANGMAN_PICS) - 1:
             displayBoard(missed_letters, correct_letters, secret_words)
             print('You have run out of guesses!\nAfter ' + str(len(missed_letters)) + ' missed guesses and ' + str(len(correct_letters)) + ' correct guesses, the word was "' + secret_words + '"')
             gameIsDone = True

             
    if game_is_done:
        if playAgain():
            missed_letters = ''
            correct_letters = ''
            secret_words = getRandomWords(words)
        else:
            break