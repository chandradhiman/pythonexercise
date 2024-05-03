cars = 100
space_in_car = 10.9
drivers = 30
passengers = 90
cars_driven = 10
cars_not_driven = cars-drivers
carpool_capacity = cars_driven * space_in_car
average_passengers_per_car = passengers/cars_driven

#string

type_of_people =20
x= f"There are {type_of_people} type of people"
y = f"Chandra Dhiman is Czech language student."
z = f"Saying Hello is also a good sign of start a conversation"
binary ="binary"
do_not = "don't"

print(x)
print(y)

print(f"I said : '{x}'")
print(f"I said : '{y}' ")
print(f"I didn't say : '{z}'")



print ("We have",  cars ,  "in my house.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car,"in each car.")


