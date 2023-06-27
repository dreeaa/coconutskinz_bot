#list of skincare names
skincare_names = ['COCONUTSKINZ Acne Pimple Patch', 'COCONUTSKINZ Snail 96 Mucin Power essence',
                'CORSX Low pH Good Morning Gel Cleanser','AHA BHA PHA 30 Days Mircacle Toner', 'KLAIRS Freshly Juiced Vitamin Drop',
                'ROUND LAB 1025 Dokdo Toner','THE FACE SHOP Rice Water Bright Light Cleansing Oil','INNISFREE Bija Trouble Facial Foam','COCONUTSKINZ Rabbit Embo Cotton Pads', 'IM FROM Honey Mask', 
                'MIZON Good Bye Blemish Pink Spot','COCONUTSKINZ Anti-Pore Blackhead Clear Kit']

#list of skincare prices
skincare_prices = [6.00, 27.00, 16.00, 48.00, 40.00, 22.00, 20.00, 15.00, 5.00, 54.00, 
                21.00, 5.00]

def menu():
    number_skincare = 12

    for count in range (number_skincare):
        print("{} {} ${:.2f}".format(count+1, skincare_names[count], skincare_prices[count]))

menu()