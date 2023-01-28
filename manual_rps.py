# %%
import random

# %%

options = ['Rock', 'Paper', 'Scissors']

def get_computer_choice():
    computer_choice = random.choice(options)
    return computer_choice

def get_user_choice():
    while True:
        user_choice = input('Enter Rock, Paper or Scissors')
        if user_choice not in options:
            print('You must enter either Rock, Paper or Scissors exactly.')
        else:
            return user_choice

# %%
