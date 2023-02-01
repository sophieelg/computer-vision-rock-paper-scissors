# %%
import time
import random
import cv2
from keras.models import load_model
import numpy as np

# %%
model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
options = ['Rock', 'Paper', 'Scissors', 'Nothing']

countdown_time = 20
start_time = time.time()

while True:    
    ret, frame = cap.read()
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    data[0] = normalized_image
    prediction = model.predict(data)
    highest = np.argmax(prediction[0])
    user_choice = options[highest]
    current_time = time.time()
    elapsed_time = current_time - start_time
    remaining_time = countdown_time - elapsed_time
    if remaining_time <= 0:
        print(f'You choose {user_choice}.')         
        break
    cv2.imshow('frame', frame)
    # Press q to close the window
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

def get_computer_choice():
    computer = random.choice(options)
    print(f'The computer chooses {computer}.')
    return computer

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

def play():
    computer_choice = get_computer_choice()
    get_winner(computer_choice, user_choice)

play()
            
# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()

 
# %%
