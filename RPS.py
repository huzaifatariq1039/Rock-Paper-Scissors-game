# Rocks paper scissors game

import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

print("")
playerchoice = input("Enter a number \n 1 for Rock \n 2 for paper \n 3 for scissors\n")
player = int(playerchoice)

if player < 1 | player > 3:
    sys.exit("You must enter 1,2,3.")

computerchoice = random.choice("123")
computer = int(computerchoice)

print("")

print("You choose" + str(RPS(player)).replace('RPS.', " ") +".")
print("Computer choose" + str(RPS(computer)).replace('RPS.', " ") +".")

print("")

if  player == 1 and computer == 3:
    print("You wins 🎉")
elif  player == 2 and computer == 1:
    print("You wins 🎉")
elif  player == 3 and computer == 2:
    print("You wins 🎉")
elif player == computer:
    print("Tie 😲")
else:
    print("Computer wins 🤖")
print("")