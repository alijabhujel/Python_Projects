# Rock > Scissors, Scissors > paper , paper > rock

import random
while True:
    output = ['rock','paper','scissors']
    player ={}
    while player not in output:
        computer = random.choice(output)
        player = input('rock,paper,scissors:')

        if computer == player:
            print('Computer',computer)
            print('Player',player)
            print('Game Tie')

        elif player == 'rock':
            if computer =='paper':
                print('Computer',computer)
                print('Player',player)
                print('You loose')
            
            elif computer == 'scissors':
                print('Computer',computer)
                print('Player',player)
                print('You win!..:)')

        elif player == 'paper':
            if computer =='rock':
                print('Computer',computer)
                print('Player',player)
                print('You win')
            
            elif computer == 'scissors':
                print('Computer',computer)
                print('Player',player)
                print('You loose!..')

        elif player == 'scissors':
            if computer =='paper':
                print('Computer',computer)
                print('Player',player)
                print('You win!...')
            
            elif computer == 'rock':
                print('Computer',computer)
                print('Player',player)
                print('You loose!..')

play_again = input('Wanna play again y/n'.lower)
if play_again =='n':
    

 print('Thankyou! for playing with us...:)')


        



