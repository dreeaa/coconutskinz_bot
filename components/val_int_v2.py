def order_type(low, high, question):


    while True: 
        try:
            num = int(input(question))
            if num >= low and num <= high:
                return num
            else: 
                print(f"Number must be between {low} and {high}")

        except ValueError:
            print("That is not a valid number")
            print(f"Enter a number between {low} and {high}")


low = 1
high = 2

question = (f"Enter a number between {low} and {high} ")

answer = order_type(low, high, question)

print(answer)