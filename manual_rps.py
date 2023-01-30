# %%
import random

# %%


def get_computer_choice():
    options = ['Rock', 'Paper', 'Scissors']
    computer = random.choice(options)
    print(f'The computer chooses {computer}.')
    return computer

def get_user_choice():
    while True:
        user = input('Enter Rock, Paper or Scissors')
        if user not in ['Rock', 'Paper', 'Scissors']:
            print('You must enter either Rock, Paper or Scissors exactly.')
        else:
            print(f'The user chooses {user}.')
            return user

def get_winner(computer_choice, user_choice):
    if computer_choice == user_choice:
        print('It is a tie!')
    elif user_choice == 'Rock':
        if computer_choice == 'Paper':
            print('You lost.')
        else:
            print('You won!')
    elif user_choice == 'Paper':
        if computer_choice == 'Scissors':
            print('You lost.')
        else:
            print('You won!')
    elif user_choice == 'Scissors':
        if computer_choice == 'Rock':
            print('You lost.')
        else:
            print('You won!')

def play():
    computer_choice = get_computer_choice()
    user_choice = get_user_choice()
    get_winner(computer_choice, user_choice)

play()

# %%
