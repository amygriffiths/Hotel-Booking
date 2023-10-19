# main routine starts here


# set maximum number of rooms below
MAX_ROOMS = 10


# loop to sell tickets
rooms_sold = 0
while rooms_sold < MAX_ROOMS:
   name = input("Please enter your name or 'xxx' to quit: ")


   if name == 'xxx':
       break


   rooms_sold += 1


# Output number of rooms sold
if rooms_sold == MAX_ROOMS:
   print("Congratulations you booked all the rooms")
else:
   print("You have sold {} room/s. There is {} room/s "
         "remaining".format(rooms_sold, MAX_ROOMS - rooms_sold))