# functions go here
def cash_credit(question):
    while True:
        response = input(question).lower()

        if response == "cash" or response == "ca":
            return "cash"
            print("You have selected cash, your final cost is ${:.2f}").format(sum(booking_price))

        elif response == "credit" or response == "cr":
            return "credit"
            print("You have selected cash, your final cost is ${:.2f}").format(sum(booking_price)) * 1.05
        else:
            print("Please choose a valid payment method")


# main routine goes here
while True:
    payment_method = cash_credit("Choose a payment method (cash"" or credit): ")

    print("You choose", payment_method)

    print("program continues...")
    print()
