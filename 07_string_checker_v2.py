# checks that users enter a valid response (e.g. yes / no
# cash / credit) based on a list of options
def string_checker(question, num_letters, valid_responses):
    error = "Please choose {} or {}".format(valid_responses[0], valid_responses[1])


    while True:
        response = input(question).lower()

        for item in valid_responses:
            if response == item[:num_letters] or response == item:
                return item

        print(error)


# main routine starts here
yes_no_list = ["yes", "no"]
payment_method = ["cash", "credit"]

for case in range(0, 1):
    pay_method = string_checker("Would you like to pay with cash or credit? ", 2, payment_method)
    print("You choose", pay_method)
