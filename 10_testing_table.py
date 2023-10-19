def calculate_hotel_room_cost(nights, room_rate):
    total_cost = nights * room_type
    return total_cost

# Input from the user
try:
    nights = int(input("Enter the number of nights: "))
    room_type = float(input("Enter the nightly room type: "))
except ValueError:
    print("Invalid input. Please enter a valid number.")
else:
    if nights < 1 or room_type <= 0:
        print("Invalid input. Number of nights should be at least 1, and room rate should be positive.")
    else:
        total_cost = calculate_hotel_room_cost(nights, room_type)
        print(f"Total cost for {nights} nights at a fixed rate of ${room_type} per night is ${total_cost:.2f}")
