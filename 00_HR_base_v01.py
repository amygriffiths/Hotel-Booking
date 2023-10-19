import pandas


# functions go here

# Checks user has entered yes / no to a question
def yes_no(question):
    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"

        elif response == "no" or response == "n":
            return "no"

        else:
            print("Please enter yes or no")


# checks that user response is not blank
def not_blank(question):
    while True:
        response = input(question)
        if response == "":
            print("Sorry this can't be blank. Please try again")
        else:
            return response


# checks users enter an integer to given question
def num_check(question, low, high):
    while True:
        error = f"Enter a number between {low} and {high}"

        try:
            response = int(input(question))
            if low <= response <= high:
                return response
            else:
                print(error)

        except ValueError:
            print("Please enter an integer.")

# Currency formatting function
def currency(x):
    return "${:.2f}".format(x)


# main routine starts here
while True:
    print("Welcome to the Melia Hotel, thank you for choosing to stay with us.\n"
          "We have everything from an indoor pool, a 24/7 gym, and even a kids club.")


    # Calculate the room price based on room type
    def calc_room_price(var_type):
        # room is $30 for a single
        if var_type == 1:
            price = 30

        # room is $35 for two beds
        elif var_type == 2:
            price = 35

        # room is $45 for queen
        elif var_type == 3:
            price = 45

        # room is $50 for king
        elif var_type == 4:
            price = 50

        # room is $65 for family room
        elif var_type == 5:
            price = 65

        return price

    # set maximum number of rooms below
    MAX_ROOMS = 30
    rooms_sold = 0

    yes_no_list = ["yes", "no"]
    payment_list = ["cash", "credit"]


    # loop to sell rooms
    name = not_blank("Enter your name (or 'xxx' to quit) ")

    # age checker
    age = num_check("How old are you? ", 18, 120)

    # age checker
    if 18 <= age <= 120:
        pass
    elif age < 18:
        print("Sorry you are too young to book a room")
    elif age > 120:
        print("?? That looks like a typo, please try again.")

    # Dictionaries to hold room details
    all_names = ["Single","Double", "Queen", "King", "Family's",]
    all_room_costs = [30, 35, 45, 50, 65]

    hotel_reservation_dict = {
        "Room": all_names,
        "Room Prices": all_room_costs
    }

    hotel_reservation_frame = pandas.DataFrame(hotel_reservation_dict)

    # Output table with room data
    print(hotel_reservation_frame)

    room_selection = num_check("Which room do you select? ", 0, 4)
    room_stay = num_check("How long would you like to stay? ", 1, 60)

    print("You have selected option", room_selection, "for", room_stay, "days")

    room_selection = calc_room_price(room_selection)
    booking_price = room_stay*room_selection
    rooms_sold += 1

    print("")
    # calculate room cost
    print("Room price: ${:.2f}, Booked days: {}".format(room_selection, room_stay))
    print("Your total cost will be: ${:.2f}".format(booking_price))

    # Ask the user for their payment method
    payment_method = input("Would you like to pay with cash or credit? ")

    # Check the payment method and calculate the total
    if payment_method.lower() == "cash":
        total = booking_price  # Example total without surcharge for cash payment
        print("Total amount: $", total)
    elif payment_method.lower() == "credit":
        total = booking_price  # Example total without surcharge for credit payment
        surcharge = 0.90
        total_with_surcharge = total + surcharge
        print("Total amount with surcharge: $", total_with_surcharge)
    else:
        print("Invalid payment method. Please choose 'cash' or 'credit'.")

    user_choice = input("Would you like to confirm the booking?")

    if user_choice.lower() == "yes":
        print("Booking confirmed. Thank you!\n"
              "We hope you have a great stay.")
        break  # End the program if the booking is confirmed.
    elif user_choice.lower() == "no":
        restart_choice = input("Do you want to restart the program?")
        if restart_choice.lower() == "yes":
            continue  # Restart the program by going back to the beginning of the loop.
        else:
            print("Program ended.")
            break  # End the program if the user chooses not to restart.
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")

# Output number of rooms sold
if rooms_sold == MAX_ROOMS:
    print("Congratulations you booked all the rooms")
else:
    print("You have sold {} room/s. There is {} room/s "
          "remaining".format(rooms_sold, MAX_ROOMS - rooms_sold))
