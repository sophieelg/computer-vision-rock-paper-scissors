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

# %%
