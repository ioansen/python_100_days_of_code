import random
from nltk.corpus import words

def generate_random_word_nltk():
    word_list = words.words()
    return random.choice(word_list)

def ask_for_letter():
    
    return input("Guess a letter: ").lower()


def is_guess_correct(guess, word):

    if guess in word:
        print("Right")
        return 1
    else:
        print('Wrong')
        return 0

def print_guesses_left(number_of_guesses_left):
    print(f'You have {number_of_guesses_left} guesses left')

def print_current_status(number_of_guesses_left, guessed_letters, word):

    for letter in word:
        if letter in guessed_letters:
            print(letter, end="")
        else:
            print('_', end="")
    
    print()
    print_guesses_left(number_of_guesses_left)


def verify_end(number_of_guesses_left, guessed_letters, word):
    if number_of_guesses_left == 0:
        return 0
    
    for letter in word:
        if letter not in guessed_letters:
            return 1
        
    return -1


print("Let's play hangman")

word = generate_random_word_nltk()

number_of_guesses_left = 5
guessed_letters = []

print_current_status(number_of_guesses_left, guessed_letters, word)

while verify_end(number_of_guesses_left, guessed_letters ,word):
    
    current_guess = ask_for_letter()

    if is_guess_correct(current_guess, word):
        guessed_letters.append(current_guess)
    else:
        number_of_guesses_left -= 1

    print_current_status(number_of_guesses_left, guessed_letters, word)
    

if verify_end(number_of_guesses_left, guessed_letters ,word) == 0:
    print("you lost. Cheers")
    print(f'the word was: {word}')
else:
    print("you won. Good for you")