# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)
#
# Remember the rules:
#
# Rock beats scissors
# Scissors beats paper
# Paper beats rock


user1 = input("What's your name?\t")
user2 = input("And your name?\t")

while True:
    user1_answer = input("Hi {} ! Do yo want to choose rock, paper or scissors?".format(user1))
    user2_answer = input("Hi {} ! Do yo want to choose rock, paper or scissors?".format(user2))


    if user1_answer.title() == user2_answer.title():
        print("It's a tie! ")
        if str(input('Do you want to play another game, yes or no?\n')).title() == 'Yes':
            continue
        else:
            print('game over.')
            break
    elif user1_answer.title() == 'Rock':
        if user2_answer.title() == 'Scissors':
            print("Rock wins!")
            if str(input('Do you want to play another game, yes or no?\n')).title() == 'Yes':
                continue
            else:
                print('game over.')
                break
        else:
            print("Paper wins!")
            if str(input('Do you want to play another game, yes or no?\n')).title() == 'Yes':
                continue
            else:
                print('game over.')
                break
    elif user1_answer.title() == 'Scissors':
        if user2_answer.title() == 'Paper':
            print("Scissors win!")
            if str(input('Do you want to play another game, yes or no?\n')).title() == 'Yes':
                continue
            else:
                print('game over.')
                break
        else:
            print("Rock wins!")
            if str(input('Do you want to play another game, yes or no?\n')).title() == 'Yes':
                continue
            else:
                print('game over.')
                break
    elif user1_answer.title() == 'Paper':
        if user2_answer.title() == 'Rock':
            print("Paper wins!")
            if str(input('Do you want to play another game, yes or no?\n')).title() == 'Yes':
                continue
            else:
                print('game over.')
                break
        else:
            print("Scissors win!")
            if str(input('Do you want to play another game, yes or no?\n')).title() == 'Yes':
                continue
            else:
                print('game over.')
                break
    else:
        print("Invalid input! You have not entered rock, paper or scissors, try again.")
