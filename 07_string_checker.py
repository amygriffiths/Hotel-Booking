# checks that users enter a valid response (e.g. yes / no
# cash / credit) based on a list of options
def string_checker(question, valid_responses):
    while True:

        response = input(question).lower()

        for item in valid_responses:
            if response == item[0] or response == item:
                return item

        print("Please enter a valid response")


# main routine starts here
yes_no_list = ["yes", "no"]
payment_list = ["cash", "credit"]

for case in range(0, 5):
    want_instructions = string_checker("Do you want to read the ""instructions (y/n): ", 1)
    print("You choose", want_instructions)

for case in range(0, 5):
    pay_method = string_checker("Choose a payment method (cash"" / credit): ", 2)
    print("You choose", pay_method)
