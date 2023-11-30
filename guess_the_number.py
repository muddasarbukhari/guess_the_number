import random
import math

lower = int(input("Enter the lower value = "))

upper = int(input("Enter the higher value = "))

number = random.randint(lower,upper)

chances = round(math.log(upper - lower + 1, 2))

counter = 0
while counter < chances:
    counter += 1
    
    guess = int(input("Enter the number to guess = "))
    
    if number == guess:
        print(f"You guess it in {counter} try")
        break
    elif number < guess:
        print("You guessed too large")
    elif number > guess:
        print("you guessed too small")
    if counter >= chances:
        print(f"The number is {number}")
        print("Try your luck next time")