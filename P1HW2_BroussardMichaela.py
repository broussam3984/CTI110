# Michaela Broussard
# 03/08/2026
# P1HW2
# This program calculates travel expenses and remaining budget

budget = float(input("Enter your budget: "))
destination = input("Enter your travel destination: ")

gas = float(input("Enter amount you will spend on gas: "))
accommodation = float(input("Enter amount you will spend on accommodation: "))
food = float(input("Enter amount you will spend on food: "))

expenses = gas + accommodation + food
remaining = budget - expenses

print("\n------Travel Expenses------")
print("Location:", destination)

print("\nInitial Budget:", budget)
print("Gas:", gas)
print("Accommodation:", accommodation)
print("Food:", food)

print("\nRemaining Balance:", remaining)