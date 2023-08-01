print("Do you want your order delivered or would you like to do click and collect?")

print("For click and collect enter 1")
print("For delivery enter 2")

while True:
    try:
        delivery = int(input("Please enter a number "))
        if delivery >= 1 and delivery <= 2:
            if delivery == 1:
                print("Click and collect")
                break

            elif delivery == 2:
                print("Delivery")
                break
        else: 
            print("The number must be 1 or 2")
    except ValueError:
        print("That is not a valid number")
        print("Please enter 1 or 2")


