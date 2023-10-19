# functions go here

# ask how long guests will be staying (add minimum stay time)
def num_check(question):

    while True:

        try:
            response = int(input(question))
            return response

        except ValueError:
            print("Please enter the amount of time you will be staying.")
# ask how long guests will be staying (add minimum stay time)
def int_check(question,low,high):
    error = f"Please enter a number between {low} and {high}"
    valid=False
    while not valid:
        try:
            response = int(input(question))
            if low <= response <= high:
                return response
            else:
                print(error)

        except ValueError:
            print(error)
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

# main routine goes here
rooms_sold = 0

room_choice = int_check("Enter the room you would like to stay in ",1,5)
time = int_check("Enter the amount of days you would like to stay",1,60)
room_cost = calc_room_price(room_choice)
booking_price = time*room_cost
rooms_sold += 1

print("")
# calculate room cost
print("Room number: {}, Room price: ${:.2f}".format(room_choice, booking_price))
