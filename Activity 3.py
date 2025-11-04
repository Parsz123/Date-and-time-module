def hotel_cost(nights):
    return 140 * nights

def plane_ride_costs(city):
    if "Charlotte" == city:
        return 183
    elif "Tampa" == city:
        return 220
    elif "Pittsburgh" == city:
        return 222
    elif "Los Angeles" == city:
        return 475
    
def rental_car_costs(days):
    if days >= 7:
         return 40*days - 50
    elif days >= 3:
         return 40*days - 20
    else:
        return 40*days

def trip_cost(city,days,spending_money):
    return rental_car_costs(days) + hotel_cost(days) + plane_ride_costs(city) + spending_money

print("Cost of car rental:", rental_car_costs(5))
print("Cost of plane ride",plane_ride_costs("Los Angeles") )
print("Cost of hotel_room", hotel_cost(7))
print("Total cost of the trip", trip_cost("Los Angeles", 7,500))
print(trip_cost("Tampa",6,500))