# Michaela Broussard   
# 03/12/2026
# P2HW1
# This program calculates and displays travel expenses with formatted output

print("This program calculates and displays travel expenses")

budget = float(input("Enter Budget: "))
destination = input("Enter your travel destination")
gas = float(input("How much do you think you will spend on gas? "))
hotel = float(input("Approximately, how much will you need for accommodation/hotel? "))
food = float(input("Last, how much do you need for food? "))

remaining = budget - gas - hotel -food

print("\n------------Travel Expenses------------")

print(f"{'Location:':<15}{destination}")
print(f"{'Initial Budget:':<15}${hotel:,.2f}")
print(f"{'Fuel:':<15}${gas:,.2f}")
print(f"{'Accommodation:':<15}${hotel:,.2f}")
print(f"{'Food:':<15}${food:,.2f}")

print("---------------------------------------")

print(f"\nRemaining Balance: ${remaining:,.2f}")