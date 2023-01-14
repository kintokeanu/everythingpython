import random

def roll_dice():

   # dice_drawing = {} ... here we can create a dictionary with dice illustrations, ill add for sure.

   roll = input("Roll the dice? (Y/N): ") 

   while roll.lower() == "Y".lower():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    print("dice rolled: {} and {}".format(dice1,dice2))

    roll = input("Roll again? (Y/N): ")

roll_dice()