# Project 1  'Guessing the number

import random
guess =0                                   # intializa
correct_guess = random.randint(5,15)
guess_count =0                            # track how many takes to guess the correct guess

while(guess!=correct_guess):
    if guess<0:
        # print('please enter the guess greater than 0..')
        guess = int(input('Enter the correct guess greater than 0:'))
    elif guess>correct_guess:
        # print('please enter the guess between 5 and 15...')
        guess = int(input('Enter the guess between 5 and 15 :'))
    else:
            guess = int(input('Enter the guess:'))
    guess_count+=1

print(f'Congrats you guess the correct number { guess } in { guess_count } times..')
