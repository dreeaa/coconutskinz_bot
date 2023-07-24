# list to store ordered skincare
order_list = ['COCONUTSKINZ Acne Pimple Patch', 'CORSX Low pH Good Morning Gel Cleanser', 'KLAIRS Freshly Juiced Vitamin Drop', 'THE FACE SHOP Rice Water Bright Light Cleansing Oil']

# list to store skincare prices
order_cost = [6.00, 16.00, 40.00, 20.00]

cust_details = {'name': 'Andrea', 'phone': '0123456', 'house': '40', 'street': 'Rocks', 'suburb': 'Flatbush'}

def print_order():
    total_cost = sum(order_cost)
    print("Customer Details")
    print(f"Customer Name: {cust_details['name']} \nCustomer Phone: {cust_details['phone']} \nCustomer Address: {cust_details['house']} {cust_details['street']} {cust_details['suburb']}")
    print()
    print("Order Details")

    count = 0
    for item in order_list:
        print("Ordered: {} ${:.2f}".format(item, order_cost[count]))
        count = count + 1
    print()
    print("Total Order Cost")
    print(f"${total_cost:.2f}")

print_order()