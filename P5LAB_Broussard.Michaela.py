# Michaela Broussard
# 05/02/2026
# P5LAB
# This program simulates a self-checkout machine and calculates change using functions and random values.

import random

def disperse_change(change):
    # Convert to cents
    cents = int(round(change * 100))

    dollars = cents // 100
    cents %= 100

    quarters = cents // 25
    cents %= 25

    dimes = cents // 10
    cents %= 10

    nickels = cents // 5
    cents %= 5

    pennies = cents

    print()  # blank line

    if dollars > 0:
        print(f"{dollars} Dollars")
    if quarters > 0:
        print(f"{quarters} Quarters")
    if dimes > 0:
        print(f"{dimes} Dimes")
    if nickels > 0:
        print(f"{nickels} Nickels")
    if pennies > 0:
        print(f"{pennies} Pennies")

def main():
    # Generate random total owed
    total_owed = round(random.uniform(0.01, 100.00), 2)
    print(f"You owe ${total_owed:.2f}")

    # Get user input
    cash = float(input("How much cash will you put in the self-checkout? "))

    # Calculate change
    if cash < total_owed:
        print("Not enough money provided.")
    else:
        change = round(cash - total_owed, 2)
        print(f"Change is: ${change:.2f}")

        # Call function
        disperse_change(change)

# Run program
main()