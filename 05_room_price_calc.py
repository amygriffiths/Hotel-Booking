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


# loop for testing ...
#if var =  loop for testing...
while True:


    # Get room type (assume users input a valid integer)
    room = int(input("Room number: "))

    # calculate room cost
    room_cost = calc_room_price(room)
    print("Room number: {}, Room price: ${:.2f}".format(room, room_cost))
