#coconutskinz bot program
import random
from random import randint

#list of random names
names = ["Romy", "Sookie", "Zac", "Aliya", "Carl", "Sohpie", "April", "Mia", "Ethan", "Tanya"]


def welcome():
    '''
    Purpose: To generate a random name from the list and print out
    a welcome message
    Pairameters: None
    Returns: None
    '''
    num = randint(0,9)
    name = (names[num])
    print ("*** Welcome to CoconutSkinz! ***")
    print ("*** My name is", name, "***")
    print ("*** I will be here to help you order the skincare you need! ***")

def main():
    '''
    Purpose: To run all functions
    Pairameters: None
    Returns: None
    '''
    welcome()
    

main()
