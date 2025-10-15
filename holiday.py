# user-defined functions

flight_costs_dict = {"cape town": 3000,                                                            # create dictionary to easily target the prices when a city is entered
                 "johannesburg": 2000,
                 "durban": 1500}

def plane_cost(city_flight):                                                                       # defining a function with a parameter (will only work if the city flight variable is given beforehand)
    if city_flight == "cape town":                                                                 # if statement for multiple returns based on city selection
        return flight_costs_dict["cape town"]
    elif city_flight == "johannesburg":
        return flight_costs_dict["johannesburg"]
    elif city_flight == "durban":
        return flight_costs_dict["durban"]
    else:
        return 0

def hotel_cost(num_nights):                                                                         # defining a function to calculate hotel cost when num nights is given
    hotel_price_per_night = 500
    return num_nights * hotel_price_per_night

def rental_car_cost(rental_car_days):                                                               # defining a function to calculate car rental cost when rental days is given
    return rental_car_days * 250

def holiday_cost(city_flight, num_nights, rental_car_days):                                                                                 # defining a function to calculate holiday cost that calls the results of other functions
    return plane_cost(city_flight) + hotel_cost(num_nights) + rental_car_cost(rental_car_days)

print("")

print("This program will calculate your total holiday cost.")
print("")

while True:                                                                                                                                     # looping until user enters an option from the dictinary
    city_flight = input("Please select your destination city from the following options (Cape Town, Johannesburg, Durban): ").lower()
    print("")
    if city_flight in flight_costs_dict:                                                                                                        # this line ensures it chooses from the dictionary
        print("Your flight will cost ", plane_cost(city_flight))
        break
    else:
        print("Invalid option")

print("")

while True:
    try:
        num_nights = int(input("How many nights at the hotel would you like to book: "))
        if num_nights > 0:
            print("")
            print("Your accomodation will cost ", hotel_cost(num_nights))
            print("")
            break
        else:
            print("invalid number, enter positive number")
    except ValueError:
        print("Invalid input, enter NUMBER")

while True:
    try:
        rental_car_days = int(input("How many days would you like to rent a car for: "))
        if rental_car_days > 0:
            print("")
            print("Your car rental will cost ", rental_car_cost(rental_car_days))
            print("")
            break
        else:
            print("invalid number, enter positive number")

    except ValueError:
        print("Invalid input, enter NUMBER")


print(f"Your holiday to {city_flight} for {num_nights} nights including car hire will be ", holiday_cost(city_flight, num_nights, rental_car_days))
print("")
