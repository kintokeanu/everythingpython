import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0

    while guess != random_number:
        guess = int(input(f"Enter a number between 1 and {x}: "))

        if guess < random_number:
            print("Sorry guess again too low")
        elif guess > random_number:
            print("Sorry guess again too high")
    
    print(f"Yes!! you guessed {random_number} correctly")


    
def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f" Is the {guess} to high(H), too low (L) or correct (c)").lower()
        if feedback == "h":
            high = guess -1
        elif feedback == 'l':
            low = guess+ 1
    print(f"Yes!! you guessed the number {guess} correctly")


computer_guess(10)

    
    
