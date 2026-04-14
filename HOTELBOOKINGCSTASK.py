

#validation of the booking reference number
def validate_booking_ref(reference):
    if len(reference) != 7 :
        return False

    letters = reference[0:3]
    digits = reference[3:6]

    if letters.isalpha() and digits.isdigit():
        return True
    else:
        return False

#calculating the room cost
def calculate_room_cost(room_type, nights):

    if room_type == "single":
        return 50*nights

    elif room_type == "double":
        return 80*nights

    elif room_type == "suite":
        return 150*nights

    return 0



#adding the discounts
def apply_discounts(cost, nights, season, returning):
    if nights >= 7:
        cost = (cost*(1-(10/100)))

    if season == "winter":
        cost = (cost * (1 - (15 / 100)))

    if returning == "yes":
        cost = (cost * (1 - (5 / 100)))

    return cost


#add breakfast
def add_extras(cost, guests, breakfast, nights):
    if breakfast == "yes":
        cost += guests * 15 * nights

    return cost


reference = input("Enter the reference number: ")
if validate_booking_ref(reference):
    nights = int(input("Enter the number of nights: "))
    room_type = input("Enter the room type: ")
    guests = int(input("Enter the number of guests: "))
    returning = input("Have you visited us before? (yes/no): ")
    season = input("Enter the season of visit: ")
    breakfast = input("Will you be having breakfast? (yes/no): ")
    basecost = calculate_room_cost(room_type, nights)
    discounts = apply_discounts(basecost, nights, season, returning)
    totalcost = add_extras(basecost, guests, breakfast, nights)
    print("The total cost is ", totalcost)

else:
    print("This room isnt available")














