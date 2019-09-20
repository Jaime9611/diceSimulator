# Main script for the dice project
import sys

from dice import Dice

def play():
    pass

print('******************Dice Simulator********************')

print("\nWrite 't' to throw the dices.")
print("Write 'q' to quit from the program.\n")

while True:
    option = input('What would you like to do? ')
    if option == 't' or option == 'q':
        break
    else:
        print('Invalid input. Try again.\n')

if option == 't':
    play()    
if option == 'q':
    sys.exit()