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
            num = int(input(question))  # Asks the user to input an integer and stores it in the variable 'num'.
            if num >= LOW and num <= HIGH:  # Checks if the input integer is within the specified range.
                return num  # If the input is valid, returns the integer 'num' to the calling code.
            else: 
                print(f"Number must be between {LOW} and {HIGH}")  # If the input is not within the specified range, prints an error message.

        except ValueError:
            print("That is not a valid number")  # If the input is not a valid integer, prints an error message.

#validates inputs to check if they are an integer with 7 to 10 digits
def check_phone(question, PH_LOW, PH_HIGH):
    while True:
        try:
            num = int(input(question))  # Asks the user to input an integer and stores it in the variable 'num'.
            test_num = num
            count = 0
            while test_num > 0:  # Counts the number of digits in the input integer.
                test_num = test_num // 10
                count = count + 1
            if count >= PH_LOW and count <= PH_HIGH:  # Checks if the count of digits is within the specified range.
                return num  # If the input has the correct number of digits, returns the integer 'num' to the calling code.
            else:
                print("NZ phone numbers have between 7 and 10 digits ")  # If the input has an invalid number of digits, prints an error message.
        except ValueError:
            print("Please enter a number ")  # If the input is not a valid integer, prints an error message.

#welcome message with random name 
def welcome():
    '''
    Purpose: To generate a random name from the list and print out
    a welcome message
    Parameters: None
    Returns: None
    '''

    num = randint(0, 9)  # Generates a random number between 0 and 9 (inclusive) and stores it in the variable 'num'.
    name = (names[num])  # Fetches a random name from the 'names' list using the random number 'num' as an index and stores it in the variable 'name'.

    #the logo for coconutskinz - Prints the logo of CoconutSkinz using a multi-line string.
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

    print ("*** Welcome to CoconutSkinz! ***")  # Prints a welcome message.
    print ("*** My name is", name, "***")  # Prints a message introducing the bot with the randomly selected name.
    print ("*** I will be here to help you order the skincare you need! ***")  # Prints a message indicating the purpose of the bot.
    print ("*** Please note that there is a $9 delivery fee when items are less than 5 ***")  # Prints a note about the delivery fee for orders with less than 5 items.


#menu for click and collect or delivery
def order_type():
    del_pick = ""  # Initialize a variable 'del_pick' to store the delivery/pickup option.

    LOW = 1  # A constant representing the lower bound for user input.
    HIGH = 2  # A constant representing the upper bound for user input.

    question = (f"Enter a number between {LOW} and {HIGH} ")  # Prompt message to instruct the user to enter a number between 'LOW' and 'HIGH'.

    print("Do you want your order delivered or would you like to do click and collect? ")  # Prints a message to ask the user about their delivery preference.
    print("  For click and collect enter 1 ")  # Prints the option for click and collect.
    print("  For delivery enter 2 ")  # Prints the option for delivery.

    delivery = valid_int(LOW, HIGH, question)  # Calls the 'valid_int' function to get a valid integer input from the user between 'LOW' and 'HIGH'.

    if delivery == 1:  # If the user chose 1 (click and collect).
        print("Click and collect")  # Prints a message indicating that click and collect option is chosen.
        del_pick = "pickup"  # Set 'del_pick' to "pickup" to represent click and collect.
        pickup_info()  # Calls the 'pickup_info' function to get additional information for click and collect.

    elif delivery == 2:  # If the user chose 2 (delivery).
        print("Delivery")  # Prints a message indicating that delivery option is chosen.
        del_pick = "delivery"  # Set 'del_pick' to "delivery" to represent delivery.
        delivery_info()  # Calls the 'delivery_info' function to get delivery information.

    return del_pick  # Returns the chosen delivery/pickup option ('del_pick') to be used in the rest of the program.


#click and collect information 
def pickup_info():
    question = ("Please enter your name ")  # Prompt message to instruct the user to enter their name.
    customer_details['name'] = check_string(question)  # Calls the 'check_string' function to get and validate the user's name. The name is stored in the 'customer_details' dictionary under the key 'name'.
    #print (customer_details['name'])  # Uncommenting this line will print the user's name, but it seems to be commented out for debugging purposes.

    question = ("Please enter your phone number ")  # Prompt message to instruct the user to enter their phone number.
    customer_details['phone'] = check_phone(question, PH_LOW, PH_HIGH)  # Calls the 'check_phone' function to get and validate the user's phone number. The phone number is stored in the 'customer_details' dictionary under the key 'phone'.
    #print (customer_details['phone'])  # Uncommenting this line will print the user's phone number, but it seems to be commented out for debugging purposes.
    print(customer_details)  # Prints the 'customer_details' dictionary containing the user's name and phone number.

#delivery information - name address and phone
#customers name
def delivery_info():
    question = ("Please enter your name ")  # Prompt message to instruct the user to enter their name.
    customer_details['name'] = check_string(question)  # Calls the 'check_string' function to get and validate the user's name. The name is stored in the 'customer_details' dictionary under the key 'name'.
    print (customer_details['name'])  # Prints the user's name.

#customers phone number
    question = ("Please enter your phone number ")  # Prompt message to instruct the user to enter their phone number.
    customer_details['phone'] = check_phone(question, PH_LOW, PH_HIGH)  # Calls the 'check_phone' function to get and validate the user's phone number. The phone number is stored in the 'customer_details' dictionary under the key 'phone'.
    print (customer_details['phone'])  # Prints the user's phone number.

#customers address
    question = ("Please enter your house number ")  # Prompt message to instruct the user to enter their house number.
    customer_details['house'] = not_blank(question)  # Calls the 'not_blank' function to get and validate the user's house number. The house number is stored in the 'customer_details' dictionary under the key 'house'.
    print (customer_details['house'])  # Prints the user's house number.

#customers address
    question = ("Please enter your street name ")  # Prompt message to instruct the user to enter their street name.
    customer_details['street'] = check_string(question)  # Calls the 'check_string' function to get and validate the user's street name. The street name is stored in the 'customer_details' dictionary under the key 'street'.
    print (customer_details['street'])  # Prints the user's street name.

#customers address
    question = ("Please enter your suburb ")  # Prompt message to instruct the user to enter their suburb.
    customer_details['suburb'] = check_string(question)  # Calls the 'check_string' function to get and validate the user's suburb. The suburb is stored in the 'customer_details' dictionary under the key 'suburb'.
    print (customer_details['suburb'])  # Prints the user's suburb.


#skincare menu 
def menu():
    number_skincare = 12  # Total number of skincare products available in the menu.

    for count in range (number_skincare):  # Iterate over the range from 0 to number_skincare-1.
        # Print the name and price of each skincare product in the format "Number Name Price".
        # The format {:.2f} ensures that the price is displayed with two decimal places.
        print("{} {} ${:.2f}".format(count+1, skincare_names[count], skincare_prices[count]))

#skincare order - from menu - print each skincare ordered with cost
def order_skincare():

# ask for the total number of skincare for the order
    num_skincare = 0  # Initialize the variable to store the total number of skincare products to be ordered.
    NUM_LOW = 1  # The lowest valid number of skincare products to be ordered.
    NUM_HIGH = 12  # The highest valid number of skincare products to be ordered.
    question = (f"Enter a number between {NUM_LOW} and {NUM_HIGH} ")  # Prompt message to instruct the user to enter the number of skincare products to be ordered.
    print("How many skincare products would you like to order? ")
    num_skincare = valid_int(NUM_LOW, NUM_HIGH, question)  # Calls the 'valid_int' function to get and validate the number of skincare products to be ordered.

# choose skincare from the menu
    for item in range(num_skincare):  # Iterate over the range from 0 to num_skincare-1.
        while num_skincare > 0:  # Loop until the desired number of skincare products have been ordered.
            print("Please choose your skincare product by entering the number of the skincare from the menu: ")
            question = (f"Enter a number between {NUM_LOW} and {NUM_HIGH} ")

            skincare_ordered = valid_int(NUM_LOW, NUM_HIGH, question)  # Calls the 'valid_int' function to get and validate the chosen skincare product number.
            skincare_ordered -= 1  # Decrement by 1 to get the index in the list.
            order_list.append(skincare_names[skincare_ordered])  # Adds the chosen skincare product name to the 'order_list' list.
            order_cost.append(skincare_prices[skincare_ordered])  # Adds the chosen skincare product price to the 'order_cost' list.
            # Prints the name and price of the chosen skincare product in the format "Name Price".
            # The format {:.2f} ensures that the price is displayed with two decimal places.
            print("{} ${:.2f}".format(skincare_names[skincare_ordered], skincare_prices[skincare_ordered]))
            num_skincare -= 1  # Decrease the number of skincare products left to be ordered by 1 in each iteration.




#print order out - including if order is delivering or click and collect and names and price of each skincare - total cost including any delivery charge 
def print_order(del_pick):
    # Print a blank line for better readability.
    print()
    # Calculate the total cost of the order by summing up the prices of all the skincare products.
    total_cost = sum(order_cost)
    # Print "Customer Details" section header.
    print("Customer Details")
    # Check if the order is for click and collect.
    if del_pick == "pickup":
        print("Your Order is for Click and Collect")
        # Print customer name and phone number for click and collect.
        print(f"Customer Name: {customer_details['name']} \nCustomer Phone: {customer_details['phone']}")
    # Check if the order is for delivery.
    elif del_pick == "delivery":
        print("Your Order is for Delivery")
        # Print customer name, phone number, house number, street name, and suburb for delivery.
        print(f"Customer Name: {customer_details['name']} \nCustomer Phone: {customer_details['phone']} \nCustomer Address: {customer_details['house']} {customer_details['street']} {customer_details['suburb']}")
    # Print a blank line for better readability.
    print()
    # Print "Order Details" section header.
    print("Order Details")
    count = 0  # Initialize a counter for iterating through the ordered skincare products.
    for item in order_list:  # Iterate through each ordered skincare product.
        # Print the name and price of the ordered skincare product in the format "Ordered: Name $Price".
        print("Ordered: {} ${:.2f}".format(item, order_cost[count]))
        count = count + 1  # Increment the counter for the next iteration.
    if del_pick == "delivery":  # Check if the order is for delivery.
        # Check if the number of ordered skincare products is greater than or equal to 5.
        if len(order_list) >= 5:
            # Print a message indicating that delivery is free for orders with 5 or more products.
            print("As you have ordered 5 or more skincare products, your order will be delivered to you for free.")
        # Check if the number of ordered skincare products is less than 5.
        elif len(order_list) < 5:
            # Print a message indicating the delivery fee of $9.00 for orders with less than 5 products.
            print("As you have ordered less than 5 skincare products, you will be charged a $9.00 delivery fee.")
            # Add the delivery fee to the total cost of the order.
            total_cost = total_cost + 9

    # Print a blank line for better readability.
    print()
    # Print the "Total Order Cost" section header.
    print("Total Order Cost")
    # Print the total cost of the order in the format "$TotalCost".
    # The format {:.2f} ensures that the total cost is displayed with two decimal places.
    print(f"${total_cost:.2f}")


#ability to cancel or proceed with order
def confirm_cancel():
    # Define constants for user input validation.
    LOW = 1
    HIGH = 2
    # Create a question for user input.
    question = (f"Enter a number between {LOW} and {HIGH} ")
    
    # Print messages to ask the user to confirm or cancel the order.
    print("Please Confirm Your Order")
    print("To confirm your order, please enter 1 ")
    print("To cancel your order, please enter 2 ")

    # Get user input for confirmation or cancellation and validate it as an integer between LOW and HIGH.
    confirm = valid_int(LOW, HIGH, question)

    # Check if the user confirmed the order (chose 1).
    if confirm == 1:
        # Print a message confirming the order.
        print("Order Confirmed")
        print("Your order has been sent to our team and will be delivered to you as soon as possible!")
        # Call the new_exit function to offer the option to start a new order or exit the bot.
        new_exit()

    # Check if the user canceled the order (chose 2).
    elif confirm == 2:
        # Print a message indicating that the order has been canceled.
        print("Your order has been Cancelled")
        print("You may restart your order or exit the BOT")
        # Call the new_exit function to offer the option to start a new order or exit the bot.
        new_exit()


def new_exit():
    # Define constants for user input validation.
    LOW = 1
    HIGH = 2
    # Create a question for user input.
    question = (f"Enter a number between {LOW} and {HIGH} ")
    
    # Print messages to ask the user if they want to start another order or exit the bot.
    print("Do you want to start another order or exit? ")
    print("  To start another order, please enter 1 ")
    print("  To exit the bot, please enter 2 ")

    # Get user input for starting a new order or exiting the bot and validate it as an integer between LOW and HIGH.
    confirm = valid_int(LOW, HIGH, question)

    # Check if the user wants to start a new order (chose 1).
    if confirm == 1:
        # Print a message indicating the choice to start a new order.
        print("New Order")
        # Clear the order_list, order_cost, and customer_details lists/dictionary for a fresh order.
        order_list.clear()
        order_cost.clear()
        customer_details.clear()
        # Call the main function to start a new order process.
        main()

    # Check if the user wants to exit the bot (chose 2).
    elif confirm == 2:
        # Print a message indicating the choice to exit the bot.
        print("Exit")
        # Clear the order_list, order_cost, and customer_details lists/dictionary.
        order_list.clear()
        order_cost.clear()
        customer_details.clear()
        # Exit the bot.
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