# %%
import random

# %%

def get_computer_choice():
    options = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(options)
    return computer_choice

def get_user_choice():
    while True:
        user_choice = input('Enter Rock, Paper or Scissors')
        if user_choice not in ['Rock', 'Paper', 'Scissors']:
            print('You must enter either Rock, Paper or Scissors exactly.')
        else:
            return user_choice

def get_winner(computer_choice, user_choice):
    if computer_choice == user_choice:
        print('It is a tie!')
    elif user_choice == 'Rock':
        if computer_choice == 'Paper':
            print('You lost')
        else:
            print('You won!')
    elif user_choice == 'Paper':
        if computer_choice == 'Scissors':
            print('You lost')
        else:
            print('You won!')
    elif user_choice == 'Scissors':
        if computer_choice == 'Rock':
            print('You lost')
        else:
            print('You won!')

# %%
