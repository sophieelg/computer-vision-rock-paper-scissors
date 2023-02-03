# %%
import time
import random
import cv2
from keras.models import load_model
import numpy as np

# %%

model = load_model('keras_model.h5')
options = ['Rock', 'Paper', 'Scissors', 'Nothing']

class RockPaperScissors:
    def __init__(self, model):
        self.model = model
        self.countdown_time = 5
        self.computer_choice = random.choice(options)
        self.computer_wins = 0
        self.user_wins = 0
    
    def get_prediction(self):
        cap = cv2.VideoCapture(0)
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        user_win_amount = "User wins: " + str(self.user_wins)
        computer_win_amount = "Computer wins: " + str(self.computer_wins)
        time_now = time.time()
        while time.time() < time_now + self.countdown_time:    
            ret, frame = cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            data[0] = normalized_image
            prediction = model.predict(data)
            cv2.putText(frame, options[np.argmax(prediction)], (0, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 3)
            cv2.putText(frame, user_win_amount, (0, 100), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 3)
            cv2.putText(frame, computer_win_amount, (0, 150), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 3)
            cv2.putText(frame, str(int((time_now + self.countdown_time - time.time()))), (0, 200), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 3)
            cv2.imshow('frame', frame)
            # Press q to close the window
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        # After the loop release the cap object
        cap.release()
        # Destroy all the windows
        cv2.destroyAllWindows()

        highest = np.argmax(prediction[0])
        user_choice = options[highest]
        if user_choice == 'Rock':
            print('You choose Rock.')
            self.get_winner(user_choice)
        elif user_choice == 'Paper':
            print('You choose Paper.')
            self.get_winner(user_choice)
        elif user_choice == 'Scissors': 
            print('You choose Scissors.')
            self.get_winner(user_choice)
        else:
            print('You choose nothing.')
        return (user_choice)

    def get_computer_choice(self):
        self.computer_choice = random.choice(options)
        print(f'The computer chooses {self.computer_choice}.')
        return (self.computer_choice)

    def get_winner(self, user_choice):
        if self.computer_choice == user_choice:
            print('It is a tie!')
        elif user_choice == 'Rock':
            if self.computer_choice == 'Paper':
                print('You lost')
                self.computer_wins += 1
                print(f'Computer has won {self.computer_wins}.')
            else:
                print('You won!')
                self.user_wins += 1
                print(f'You have won {self.user_wins}.')
        elif user_choice == 'Paper':
            if self.computer_choice == 'Scissors':
                print('You lost')
                self.computer_wins += 1
                print(f'Computer has won {self.computer_wins}.')
            else:
                print('You won!')
                self.user_wins += 1
                print(f'You have won {self.user_wins}.')
        elif user_choice == 'Scissors':
            if self.computer_choice == 'Rock':
                print('You lost')
                self.computer_wins += 1
                print(f'Computer has won {self.computer_wins}.')
            else:
                print('You won!')
                self.user_wins += 1
                print(f'You have won {self.user_wins}.')

    def countdown(self):
        cap = cv2.VideoCapture(0)
        start_time = time.time()
        while time.time() < start_time + self.countdown_time:
            ret, frame = cap.read()         
            cv2.putText(frame, "Please choose between Rock, Paper or Scissors.", (50, 100), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 3)
            cv2.imshow("frame", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

def play_game(model):
    game = RockPaperScissors(model)
    game.countdown()
    while True:
        if game.computer_wins == 3:
            print('You lost! The computer won 3 times.')
            restart = input('Press R to restart the game. Press Q to quit.')
            if restart.lower() == "r":
                game.computer_wins = 0
                game.user_wins = 0
                game.get_computer_choice()
                game.get_prediction()
            else:
                break
        elif game.user_wins == 3:
            print('You won! You beat the computer 3 times.')
            restart = input('Press R to restart the game. Press Q to quit.')
            if restart.lower() == "r":
                game.computer_wins = 0
                game.user_wins = 0
                game.get_computer_choice()
                game.get_prediction()
            else:
                break
        else:
            game.get_computer_choice()
            game.get_prediction()
            

play_game(model)
# %%
