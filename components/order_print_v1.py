# list to store ordered skincare
order_list = ['COCONUTSKINZ Acne Pimple Patch', 'CORSX Low pH Good Morning Gel Cleanser', 'KLAIRS Freshly Juiced Vitamin Drop', 'THE FACE SHOP Rice Water Bright Light Cleansing Oil']

# list to store skincare prices
order_cost = [6.00, 16.00, 40.00, 20.00]

cust_details = {'name': 'Andrea', 'phone': '0123456', 'house': '40', 'street': 'Rocks', 'suburb': 'Flatbush'}

print("\nCustomer Name:\n {}\nCustomer phone:\n{}\nCustomer House Number\n{}\nCustomer Street Name:\n{}\nCustomer Suburb:\n{}".format(cust_details['name'], cust_details['phone'], cust_details['house'], cust_details['street'], cust_details['suburb']))

count = 0
for item in order_list:
    print("Ordered: {} ${:.2f}".format(item, order_cost[count]))
    count = count + 1
