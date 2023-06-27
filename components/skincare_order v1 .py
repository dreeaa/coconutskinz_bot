#list of skincare names
skincare_names = ['COCONUTSKINZ Acne Pimple Patch', 'COCONUTSKINZ Snail 96 Mucin Power essence',
                'CORSX Low pH Good Morning Gel Cleanser','AHA BHA PHA 30 Days Mircacle Toner', 'KLAIRS Freshly Juiced Vitamin Drop',
                'ROUND LAB 1025 Dokdo Toner','THE FACE SHOP Rice Water Bright Light Cleansing Oil','INNISFREE Bija Trouble Facial Foam','COCONUTSKINZ Rabbit Embo Cotton Pads', 'IM FROM Honey Mask', 
                'MIZON Good Bye Blemish Pink Spot','COCONUTSKINZ Anti-Pore Blackhead Clear Kit']

#list of skincare prices
skincare_prices = [6.00, 27.00, 16.00, 48.00, 40.00, 22.00, 20.00, 15.00, 5.00, 54.00, 
                21.00, 5.00]

#list to store ordered skincare
order_list = []

#list to store skincare prices
order_cost = []

def menu():
    number_skincare = 12

    for count in range (number_skincare):
        print("{} {} ${:.2f}".format(count+1, skincare_names[count], skincare_prices[count]))

menu()

#ask for total number of skincare for order
num_skincare = 0

num_skincare = int(input("How much skincare do you want to order? "))

print(num_skincare)

#choose skincare from menu
print("Please choose your skincare by entering the number of the skincare from the menu ")
for item in range (num_skincare):
    while num_skincare > 0:
        skincare_ordered = int(input())
        order_list.append(skincare_names[skincare_ordered])
        order_cost.append(skincare_prices[skincare_ordered])
        num_skincare = num_skincare-1

print(order_list)
print(order_cost)


#count down until all skincare are ordered



#print order