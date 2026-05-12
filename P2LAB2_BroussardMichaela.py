# Michaela Broussard
# 03/12/2026
# P2LAB2
# This program uses a dictionary to store vehicle MPG and calculate gas needed.

vehicles = {
    'Camaro': 18.21,
    'Prius': 52.36,
    'Model S': 110,
    'Silverado': 26
}

keys = vehicles.keys()
print(keys)

vehicle = input("Enter a vehicle to see it's mpg: ")

mpg = vehicles[vehicle]
print(f"\nThe {vehicle} gets {mpg} mpg.")

miles = float(input(f"\nHow many miles will you drive the {vehicle}? "))

gallons = miles / mpg

print(f"\n{gallons:.2f} gallon(s) od gas are needed to drive the {vehicle} {miles} miles.")