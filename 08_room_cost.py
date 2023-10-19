import pandas

# dictionaries to hold room details
all_names = ["a", "b", "c", "d", "e", "f",
             "g", "h", "i", "j"]
all_ticket_costs = [120, 160, 190, 210, 240, 270, 300, 360, 420, 480]
surcharge = [0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9]

hotel_reservation_dict = {
    "Name": all_names,
    "Room Prices": all_ticket_costs,
    "Surcharge": surcharge
}

hotel_reservation_frame = pandas.DataFrame(hotel_reservation_dict)

# Calculate the total room cost (room + surcharge)
hotel_reservation_frame['Total'] = hotel_reservation_frame['Surcharge'] \
                                    + hotel_reservation_frame ['Room Prices']

# Calculate the profit for each room
hotel_reservation_frame['Profit'] = hotel_reservation_frame['Room Prices'] - 100

# Calculate room and profit totals
total = hotel_reservation_frame['Total'].sum()
profit = hotel_reservation_frame['Profit'].sum()

# output table with room data
print(hotel_reservation_frame)

# output total room sales and profit
print("Total Room Sales: ${:.2f}". format(total))
print("Total Profit : ${:.2f}".format(profit))