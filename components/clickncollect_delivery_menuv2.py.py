#bugs
#will only work for valid input
#invalid input triggers else statement but program does not as for input a

#menu so that users can choose either pickup or click and collect 

print("Do you want your order delivered or would you like to do click and collect?")

print("For delivery enter d")
print("For click and collect enter c")

delivery = input()

if delivery =="d":
    print("Delivery")

elif delivery =="c":
    print("Click and collect")

else:
    print("That was not a valid input")