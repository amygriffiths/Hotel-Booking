def calculate_room_cost(price_per_night, num_nights):
    if price_per_night <= 0 or num_nights <= 0:
        return "Invalid input. Price per night and number of nights must be greater than zero."

    total_cost = price_per_night * num_nights
    return total_cost

# Input from the user
price_per_night = float(input("Enter the price per night: "))
num_nights = int(input("Enter the number of nights: "))

# Calculate and display the room cost
room_cost = calculate_room_cost(price_per_night, num_nights)
if isinstance(room_cost, str):
    print(room_cost)
else:
    print(f"The total cost for {num_nights} nights at ${price_per_night} per night is ${room_cost}.")
