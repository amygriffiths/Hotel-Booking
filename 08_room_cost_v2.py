import pandas


# Currency formatting function
def currency(x):
    return "${:.2f}".format(x)


# Dictionaries to hold room details
all_names = [1, 2, 3, 4, 5]
all_ticket_costs = [30, 35, 40, 50, 65]
surcharge = [0.9, 0.9, 0.9, 0.9, 0.9,]

hotel_reservation_dict = {
    "Room": all_names,
    "Room Prices": all_ticket_costs,
    "Surcharge": surcharge
}

hotel_reservation_frame = pandas.DataFrame(hotel_reservation_dict)

# Calculate the total room cost (room + surcharge)
hotel_reservation_frame['Total'] = hotel_reservation_frame['Surcharge'] \
                                   + hotel_reservation_frame['Room Prices']

# Calculate the profit for each room
hotel_reservation_frame['Profit'] = hotel_reservation_frame['Room Prices'] - 20

# Calculate room and profit totals
total = hotel_reservation_frame['Total'].sum()
profit = hotel_reservation_frame['Profit'].sum()

# Currency formatting (use currency function)
add_dollars = ['Room Prices', 'Surcharge', 'Total', 'Profit']
for var_item in add_dollars:
    hotel_reservation_frame[var_item] = hotel_reservation_frame[var_item].apply(currency)

# Output table with room data
print(hotel_reservation_frame)

# Output total room sales and profit
print("Total Room Sales: ${:.2f}".format(total))
print("Total Profit : ${:.2f}".format(profit))
