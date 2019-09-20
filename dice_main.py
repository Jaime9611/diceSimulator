# Main script for the dice project
import sys

from dice import Dice

def play():
    """Function for throw the dices and show the results"""
    number_1 = Dice().throw_dice()
    number_2 = Dice().throw_dice()

    print(f'\t>> You have obtained {number_1} and {number_2}, for a total of {number_1 + number_2}\n')

def info_msg():
    """Print a message with the instructions"""
    print("\nWrite 't' to throw the dices.")
    print("Write 'q' to quit from the program.\n")


print('******************Dice Simulator********************')
info_msg()

# Loop until the user quits.
while True:
    # Loop until a valid input is entered.
    while True:
        option = input('What would you like to do? ')
        if option == 't' or option == 'q':
            break
        else:
            print('Invalid input. Try again.\n')

    # Evaluates the user input
    if option == 't':
        play()
        print('+----------------------------------------------------+')
        info_msg()    
    elif option == 'q':
        print('*****************************************************')
        sys.exit()