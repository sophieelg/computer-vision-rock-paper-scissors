# %%
import time
import random
import cv2
from keras.models import load_model
import numpy as np

# %%

class RockPaperScissors:
    def __init__(self):
        self.model = load_model('keras_model.h5')
        self.cap = cv2.VideoCapture(0)
        self.data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        self.countdown_time = 10
        self.start_time = time.time()
        self.computer_wins = 0
        self.user_wins = 0
        self.options = ['Rock', 'Paper', 'Scissors', 'Nothing']
    
    def get_prediction(self):
        while True:    
            ret, frame = self.cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            self.data[0] = normalized_image
            prediction = self.model.predict(self.data)
            highest = np.argmax(prediction[0])
            user_choice = self.options[highest]
            current_time = time.time()
            elapsed_time = current_time - self.start_time
            remaining_time = self.countdown_time - elapsed_time
            if remaining_time <= 0:
                print(f'You choose {user_choice}.')
                return user_choice         
            cv2.imshow('frame', frame)
            # Press q to close the window
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        # After the loop release the cap object
        self.cap.release()
        # Destroy all the windows
        cv2.destroyAllWindows()

    def get_computer_choice(self):
        computer = random.choice(self.options)
        print(f'The computer chooses {computer}.')
        return computer

    def get_winner(self, computer_choice, user_choice):
        if computer_choice == user_choice:
            print('It is a tie!')
        elif user_choice == 'Rock':
            if computer_choice == 'Paper':
                print('You lost')
                self.computer_wins += 1
                print(f'Computer has won {self.computer_wins}.')
            else:
                print('You won!')
                self.user_wins += 1
                print(f'You have won {self.user_wins}.')
        elif user_choice == 'Paper':
            if computer_choice == 'Scissors':
                print('You lost')
                self.computer_wins += 1
                print(f'Computer has won {self.computer_wins}.')
            else:
                print('You won!')
                self.user_wins += 1
                print(f'You have won {self.user_wins}.')
        elif user_choice == 'Scissors':
            if computer_choice == 'Rock':
                print('You lost')
                self.computer_wins += 1
                print(f'Computer has won {self.computer_wins}.')
            else:
                print('You won!')
                self.user_wins += 1
                print(f'You have won {self.user_wins}.')

def play_game():
    game = RockPaperScissors()
    computer_choice = game.get_computer_choice()
    user_choice = game.get_prediction()
    while True:
        if game.computer_wins == 3:
            print('You lost! The computer won 3 times.')
            break
        elif game.user_wins == 3:
            print('You won! You beat the computer 3 times.')
            break
        else:
            game.get_prediction()
            game.get_winner(computer_choice, user_choice)

play_game()
# %%
