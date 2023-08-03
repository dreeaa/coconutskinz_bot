#skincare bot program
import sys
import random
from random import randint

#constants
LOW = 1
HIGH = 2
PH_LOW = 7
PH_HIGH = 10

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
# list to store ordered skincare
order_list = []

# list to store skincare prices
order_cost = []

#customer details dictionary
customer_details = {}

#validates inputs to check if they are blank
def not_blank(question):
    valid = False
    while not valid:
        response = input(question)
        if response !="":
            return response.title()
        else: 
            print("This cannot be blank")

#Validates to check if they are a string
def check_string(question):
    while True:
        response = input(question)
        x = response.isalpha()

        if x == False:
            print("input must only contain letters")
        else:
            return (response.title())

#validates inputs to check if they are an integer
def valid_int(LOW, HIGH, question):

    while True: 
        try:
            num = int(input(question))
            if num >= LOW and num <= HIGH:
                return num
            else: 
                print(f"Number must be between {LOW} and {HIGH}")

        except ValueError:
            print("That is not a valid number")

#validates inputs to check if they are an integer with 7 to 10 digits
def check_phone(question, PH_LOW, PH_HIGH):
    while True:
        try:
            num = int(input(question))
            test_num = num
            count = 0
            while test_num > 0:
                test_num = test_num//10
                count = count+1
            if count >= PH_LOW and count <= PH_HIGH:
                return num
            else:
                print("NZ phone numbers have between 7 and 10 digits ")
        except ValueError:
            print("Please enter a number ")



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

    #the logo for coconutskinz
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
    print ("*** Please note that there is a $9 delivery fee when items are less than 5 ***")

#menu for click and collect or delivery
def order_type():
    del_pick = ""
    LOW = 1
    HIGH = 2
    question = (f"Enter a number between {LOW} and {HIGH} ")
    print("Do you want your order delivered or would you like to do click and collect? ")
    print("  For click and collect enter 1 ")
    print("  For delivery enter 2 ")

    delivery = valid_int(LOW, HIGH, question)
    if delivery == 1:
        print("Click and collect")
        del_pick = "pickup"
        pickup_info()

    elif delivery == 2:
        print("Delivery")
        del_pick = "delivery"
        delivery_info()

    return del_pick


#click and collect information 
def pickup_info():
    question = ("Please enter your name ")
    customer_details['name'] = check_string(question)
    #print (customer_details['name'])

    question = ("Please enter your phone number ")
    customer_details['phone'] = check_phone(question, PH_LOW, PH_HIGH)
    #print (customer_details['phone'])
    print(customer_details)

#delivery information - name address and phone
def delivery_info():
    question = ("Please enter your name ")
    customer_details['name'] = check_string(question)
    print (customer_details['name'])

    question = ("Please enter your phone number ")
    customer_details['phone'] = check_phone(question, PH_LOW, PH_HIGH)
    print (customer_details['phone'])

    question = ("Please enter your house number ")
    customer_details['house'] = not_blank(question)
    print (customer_details['house'])

    question = ("Please enter your street name ")
    customer_details['street'] = check_string(question)
    print (customer_details['street'])

    question = ("Please enter your suburb ")
    customer_details['suburb'] = check_string(question)
    print (customer_details['suburb'])

#skincare menu 
def menu():
    number_skincare = 12

    for count in range (number_skincare):
        print("{} {} ${:.2f}".format(count+1, skincare_names[count], skincare_prices[count]))

#skincare order - from menu - print each skincare ordered with cost
def order_skincare():

# ask for the total number of skincare for the order
    num_skincare = 0
    NUM_LOW = 1 
    NUM_HIGH = 12
    question = (f"Enter a number between {NUM_LOW} and {NUM_HIGH} ")
    print("How many skincare products would you like to order? ")
    num_skincare = valid_int(NUM_LOW, NUM_HIGH, question)

# choose skincare from the menu
    for item in range(num_skincare):
        while num_skincare > 0:
            print("Please choose your skincare product by entering the number of the skincare from the menu: ")
            question = (f"Enter a number between {NUM_LOW} and {NUM_HIGH} ")


            skincare_ordered = valid_int(NUM_LOW, NUM_HIGH, question)
            skincare_ordered -= 1
            order_list.append(skincare_names[skincare_ordered])
            order_cost.append(skincare_prices[skincare_ordered])
            print("{} ${:.2f}".format(skincare_names[skincare_ordered], skincare_prices[skincare_ordered]))
            num_skincare -= 1



#print order out - including if order is delivering or click and collect and names and price of each skincare - total cost including any delivery charge 
def print_order(del_pick):
    print()
    total_cost = sum(order_cost)
    print("Customer Details")
    if del_pick == "pickup":
        print("Your Order is for Click and Collect")
        print(f"Customer Name: {customer_details['name']} \nCustomer Phone: {customer_details['phone']}")
    elif del_pick == "delivery":
        print("Your Order is for Delivery")
        print(f"Customer Name: {customer_details['name']} \nCustomer Phone: {customer_details['phone']} \nCustomer Address: {customer_details['house']} {customer_details['street']} {customer_details['suburb']}")
    print()
    print("Order Details")
    count = 0
    for item in order_list:
        print("Ordered: {} ${:.2f}".format(item, order_cost[count]))
        count = count + 1
    if del_pick == "delivery":
        if len(order_list) >= 5:
            print("As you have ordered 5 or more skincare products, your order will be delivered for to you free.")
        elif len(order_list) < 5:
            print("As you have ordered less than 5 skincare products, you will be charged a $9.00 delivery fee.")
            total_cost = total_cost + 9

    print()
    print("Total Order Cost")
    print(f"${total_cost:.2f}")

#ability to cancel or proceed with order
def confirm_cancel():
    LOW = 1
    HIGH = 2
    question = (f"Enter a number between {LOW} and {HIGH} ")
    
    print("Please Confirm Your Order")
    print("To confirm your order, please enter 1 ")
    print("To cancel your order, please enter 2 ")

    confirm = valid_int(LOW, HIGH, question)
    if confirm == 1:
            print("Order Confirmed")
            print("Your order has been sent to our team and will be delivered to you as soon as possible!")
            new_exit()

    elif confirm == 2:
            print("Your order has been Cancelled")
            print("You may restart your order or exit the BOT")
            new_exit()

#option for new order or to exit
def new_exit():
    LOW = 1
    HIGH = 2
    question = (f"Enter a number between {LOW} and {HIGH} ")
    
    print("Do you want to start another order or exit? ")
    print("  To start another order, please enter 1 ")
    print("  To exit the bot, please enter 2 ")

    confirm = valid_int(LOW, HIGH, question)
    if confirm == 1:
        print("New Order")
        order_list.clear()
        order_cost.clear()
        customer_details.clear()
        main()

    elif confirm == 2:
        print("Exit")
        order_list.clear()
        order_cost.clear()
        customer_details.clear()
        sys.exit()


def main():
    '''
    Purpose: To run all functions
    Parameters: None
    Returns: None
    '''
    welcome()
    del_pick = order_type()
    menu()
    order_skincare()
    print_order(del_pick)
    confirm_cancel()

main()