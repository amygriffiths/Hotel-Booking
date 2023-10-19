import pandas


# Currency formatting function
def currency(x):
    return "${:.2f}".format(x)

# Dictionaries to hold room details
all_names = ["Single","Double", "Queen", "King", "Familys",]
all_room_costs = [30, 35, 45, 50, 65]

hotel_reservation_dict = {
    "Room": all_names,
    "Room Prices": all_room_costs
}

hotel_reservation_frame = pandas.DataFrame(hotel_reservation_dict)

# Output table with room data
print(hotel_reservation_frame)
