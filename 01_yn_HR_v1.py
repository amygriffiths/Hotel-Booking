# functions go here


# main routine goes here

while True:
    want_rooms = input("Do you want to see room types?").lower()

    if want_rooms == "yes" or want_rooms == "y":
        print("room types go here")
    elif want_rooms == "no" or want_rooms == "n":
        break
    else:
        print("please answer yes/no")

print("we are done")