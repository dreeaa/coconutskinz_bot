#list to store ordered skincare
order_list = ['COCONUTSKINZ Acne Pimple Patch', 'CORSX Low pH Good Morning Gel Cleanser','KLAIRS Freshly Juiced Vitamin Drop', 'THE FACE SHOP Rice Water Bright Light Cleansing Oil']

#list to store skincare prices
order_cost =[6.00, 16.00, 40.00, 20.00,]

count = 0 
for item in order_list:
    print("Ordered: {} ${:.2f}" .format(item, order_cost[count]))
    count = count+1