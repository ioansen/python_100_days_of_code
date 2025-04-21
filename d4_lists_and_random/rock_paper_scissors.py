import random

def input_is_valid(user_input):
    if user_input not in range(4):
        print("invalid option, bye bye")
        return False

    return True

def print_final_score():
    print(f'Game over')
    print_current_score()

    if u_score == c_score:
        print("Draw!")
    elif u_score < c_score:
        print("You lost, my friend! Good luck with the rest of your life!")
    else:
        print("You won")

def print_current_score():
    print(f'Current score: {u_score} vs {c_score}')

def play_game(user_choice, computer_choice):
    global c_score, u_score
    if users_choice == computers_choice:
        print("Draw!")
    elif computers_choice > users_choice or (computers_choice == 0 and users_choice == 2):
        print("You lose")
        c_score += 1
    else:
        print("You win")
        u_score += 1

    print_current_score()

def get_user_choice():
    return int(input("Choose: "))

def get_computer_choice():
    return random.randint(0,2)


rock = "Rock"
paper = "Paper"
scissors = "Scissors"

options = [rock, paper, scissors]

u_score = 0
c_score = 0

print("Yo, my friend, my brother, lets play rock, paper, scissors, please choose: Type 0 for Rock, 1, for paper, 2 for scissors, 3 to end the game")

users_choice = get_user_choice()

while input_is_valid(users_choice) and users_choice != 3:

    computers_choice = get_computer_choice()

    print(options[users_choice], "vs",  options[computers_choice])

    play_game(users_choice, computers_choice)

    users_choice = get_user_choice()


print_final_score()