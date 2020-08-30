#!/bin/python3
#source - https://projects-static.raspberrypi.org/projects/rock-paper-scissors/84609e0e7de7bd1b635252153d8272da9cc17d81/en/resources/rock-paper-scissors-finished-rock-paper-scissors.py
# Rock crushes scissors. Scissors cut paper. Paper covers rock.
# You and the computer will battle it out in one of the world's most well known schoolyard games.May the best  win.
from random import randint

while True:
    player = input('rock (r), paper (p) or scissors (s)?.Print ')

    if (player == 'r'):
        print('O', end=' ')

    elif (player == 'p'):
        print('___', end=' ')

    elif (player == 's'):
        print('>8', end=' ')


    else:
        print('??')

    print('vs', end=' ')

    chosen = randint(1, 3)

    if (chosen == 1):
        computer = 'r'
        print('O')

    elif (chosen == 2):
        computer = 'p'
        print('___')

    else:
        computer = 's'
        print('>8')

    if (player == computer):
        print('DRAW!')

    elif (player == 'r' and computer == 's'):
        print('Player wins!')

    elif (player == 'r' and computer == 'p'):
        print('Computer wins!')

    elif (player == 'p' and computer == 'r'):
        print('Player wins!')

    elif (player == 'p' and computer == 's'):
        print('Computer wins!')

    elif (player == 's' and computer == 'p'):
        print('Player wins!')

    elif (player == 's' and computer == 'r'):
        print('Computer wins!')

    else:
        print('Huh?')