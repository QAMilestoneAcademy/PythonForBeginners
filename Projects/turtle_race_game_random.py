#Reference-https://realpython.com/beginners-guide-python-turtle/
import random
import turtle
import time
s=turtle.Screen()
s.bgcolor("light yellow")
# Setting Up the Turtles and Homes
# #You now have to create the two turtles that will represent the players. Each turtle will be a different color, corresponding to the different players. Here, player one is green and player two is blue:
player_one = turtle.Turtle()
player_one.color("green")
player_one.shape("turtle")
player_one.penup()
player_one.goto(-200,100)
player_two = player_one.clone()
player_one.color("brown")
player_two.penup()
player_two.goto(-200,100)
time.sleep(1)

# You now need to set up homes for the turtles. These homes will act as the finishing points for each turtle. Each of the turtles’ homes will be represented by a circle. Here, you need to make sure that both homes are equidistant from the starting point:

player_one.goto(300,60)
player_one.pendown()
player_one.speed(2)
player_one.circle(40)
player_one.penup()
player_one.goto(-200,100)
time.sleep(1)
player_two.goto(300,-140)
player_two.pendown()
player_two.circle(40)
player_two.penup()
player_two.goto(-200,-100)
time.sleep(1)

#now create the dice that you’ll be using to play the game.
dice = [1,2,3,4,5,6]
# This list has now become your die. To roll the dice, all you have to do is program your system to randomly select a number from it. The number that is selected will be considered as the output of the die.

# It’s time to develop the code for the rest of the game. You’ll be using loops and conditional statements here, so you need to be careful with the indentations and spaces. To start, take a look at the steps your program will need to take to run the game
# Step 1: You’ll start by telling your program to check if either turtle has reached its home.
# Step 2: If they haven’t, then you’ll tell your program to allow the players to continue trying.
# Step 3: In each loop, you tell your program to roll the die by randomly picking a number from the list.
# Step 4: You then tell it to move the respective turtle accordingly, with the number of steps based on the outcome of this random selection.


for i in range(20):
 if player_one.pos() >= (300,100):
  print("Player One Wins!")
  break
 elif player_two.pos() >= (300,-100):
  print("Player Two Wins!")
  break
 else:
    player_one_turn = turtle.textinput("Player 1: Roll the dice","Press 'Enter' to roll the dice ")
    dice_outcome1 = random.choice(dice)
    print("The result of the die roll is: ")
    print(dice_outcome1)
    print("The number of steps will be: ")
    print(20*dice_outcome1)
    player_one.fd(20*dice_outcome1)

    player_two_turn = turtle.textinput("Player 2 : Press 'Enter' to roll the die "," Press 'Enter' to roll the die")
    dice_outcome2 = random.choice(dice)
    print("The result of the die roll is: ")
    print(dice_outcome2)
    print("The number of steps will be: ")
    print(20*dice_outcome2)
    player_two.fd(20*dice_outcome2)
    time.sleep(1)