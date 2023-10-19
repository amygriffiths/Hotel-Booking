# functions go here
def yes_no(question):

    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"

        elif response == "no" or response == "n":
            return "no"

        else:
            print("Please enter yes or no")

# main routine goes here
while True:
    want_rooms = yes_no("Do you want to see room types?")


    if want_rooms == "yes":
        print("room types go here")

    print("menu continues...")
    print()