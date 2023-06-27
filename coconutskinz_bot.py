#pizza bot program
#bugs - phone number input allows letters 
#     - name input allows numbers 

import random
from random import randint

#list of random names
names = ["Romy", "Sookie", "Zac", "Aliya", "Carl", "Sohpie", "April", "Mia", "Ethan", "Tanya"]
#list of skincare names
skincare_names = ['COCONUTSKINZ Acne Pimple Patch', 'COCONUTSKINZ Snail 96 Mucin Power essence',
                'CORSX Low pH Good Morning Gel Cleanser','AHA BHA PHA 30 Days Mircacle Toner', 'KLAIRS Freshly Juiced Vitamin Drop',
                'ROUND LAB 1025 Dokdo Toner','THE FACE SHOP Rice Water Bright Light Cleansing Oil','INNISFREE Bija Trouble Facial Foam','COCONUTSKINZ Rabbit Embo Cotton Pads', 'IM FROM Honey Mask', 
                'MIZON Good Bye Blemish Pink Spot','COCONUTSKINZ Anti-Pore Blackhead Clear Kit']
#list of skincare prices
skincare_prices = [6.00, 27.00, 16.00, 48.00, 40.00, 22.00, 20.00, 15.00, 5.00, 54.00, 
                21.00, 5.00]
#customer details dictionary
customer_details ={}

#validates inputs to check if they are blank
def not_blank(question):
    valid = False
    while not valid:
        response = input(question)
        if response !="":
            return response.title()
        else: 
            print("This cannot be blank")

#welcome message with random name 
def welcome():
    '''
    Purpose: To generate a random name from the list and print out
    a welcome message
    Pairameters: None
    Returns: None
    '''
    num = randint(0,9)
    name = (names[num])

    #logo
    print("""

                                                     .-') _             .-') _     .-')   .-. .-')               .-') _    .-') _  
                                                    ( OO ) )           (  OO) )   ( OO ). \  ( OO )             ( OO ) )  (  OO) ) 
   .-----.  .-'),-----.    .-----.  .-'),-----. ,--./ ,--,' ,--. ,--.  /     '._ (_)---\_),--. ,--.  ,-.-') ,--./ ,--,' ,(_)----.  
  '  .--./ ( OO'  .-.  '  '  .--./ ( OO'  .-.  '|   \ |  |\ |  | |  |  |'--...__)/    _ | |  .'   /  |  |OO)|   \ |  |\ |       |  
  |  |('-. /   |  | |  |  |  |('-. /   |  | |  ||    \|  | )|  | | .-')'--.  .--'\  :` `. |      /,  |  |  \|    \|  | )'--.   /   
 /_) |OO  )\_) |  |\|  | /_) |OO  )\_) |  |\|  ||  .     |/ |  |_|( OO )  |  |    '..`''.)|     ' _) |  |(_/|  .     |/ (_/   /    
 ||  |`-'|   \ |  | |  | ||  |`-'|   \ |  | |  ||  |\    |  |  | | `-' /  |  |   .-._)   \|  .   \  ,|  |_.'|  |\    |   /   /___  
(_'  '--'\    `'  '-'  '(_'  '--'\    `'  '-'  '|  | \   | ('  '-'(_.-'   |  |   \       /|  |\   \(_|  |   |  | \   |  |        | 
   `-----'      `-----'    `-----'      `-----' `--'  `--'   `-----'      `--'    `-----' `--' '--'  `--'   `--'  `--'  `--------' 

    """)
    print ("*** Welcome to CoconutSkinz! ***")
    print ("*** My name is", name, "***")
    print ("*** I will be here to help you order the skincare you need! ***")

#menu for click and collect or delivery
def order_type ():
    print("Do you want your order delivered or would you like to do click and collect?")

    print("For click and collect enter 1")
    print("For delivery enter 2")

    while True:
        try:
            delivery = int(input("Please enter a number "))
            if delivery >= 1 and delivery <= 2:
                if delivery == 1:
                    print("Click and collect")
                    pickup_info()
                    break

                elif delivery == 2:
                    print("Delivery")
                    delivery_info()
                    break
            else: 
                print("The number must be 1 or 2")
        except ValueError:
            print("That is not a valid number")
            print("Please enter 1 or 2")

#pickup information 
def pickup_info():
    question = ("Please enter your name ")
    customer_details['name'] = not_blank(question)
    #print (customer_details['name'])

    question = ("Please enter your phone number ")
    customer_details['phone'] = not_blank(question)
    #print (customer_details['phone'])
    print(customer_details)

#delivery information - name address and phone
def delivery_info():
    question = ("Please enter your name ")
    customer_details['name'] = not_blank(question)
    print (customer_details['name'])

    question = ("Please enter your phone number ")
    customer_details['phone'] = not_blank(question)
    print (customer_details['phone'])

    question = ("Please enter your house number ")
    customer_details['house'] = not_blank(question)
    print (customer_details['house'])

    question = ("Please enter your street name ")
    customer_details['street'] = not_blank(question)
    print (customer_details['street'])

    question = ("Please enter your suburb")
    customer_details['suburb'] = not_blank(question)
    print (customer_details['suburb'])

#skincare menu 
def menu():
    number_skincare = 12

    for count in range (number_skincare):
        print("{} {} ${:.2f}".format(count+1, skincare_names[count], skincare_prices[count]))

menu()

#choose total number of skincare - max 5








#pizza order - from menu - print each skincare ordered with cost





#print order out - including if order is delivering or pickup and names and price of each pizza - total cost including any delivery charge 





#ability to cancel or proceed with order





#option for new order or to exit






#main function 
def main():
    '''
    Purpose: To run all functions
    Pairameters: None
    Returns: None
    '''
    welcome()
    order_type()
    menu()
    

main()