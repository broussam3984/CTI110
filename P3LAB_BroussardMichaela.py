# Michaela Broussard
# 03/22/2026
# P3LAB
# This program converts a money amount into the least number of dollars and coins.

amount = float(input("Enter the amount of money: "))
cents = int(round(amount * 100))

dollars = cents // 100
cents = cents - (dollars * 100)

quarters = cents // 25
cents = cents - (quarters * 25)

dimes = cents // 10
cents = cents - (dimes * 10)

nickels = cents // 5
cents = cents - (nickels * 5)

pennies = cents

if dollars > 0:
    if dollars == 1:
        print("1 dollar")
    else:
        print(quarters, "quarters")    

if quarters > 0:
    if quarters == 1:
        print("1 quarter")
    else:
        print(quarters, "quarters")       

if dimes > 0:
    if dimes == 1:
        print("1 dime")
    else:
        print(dimes, "dimes")                 

if nickels > 0:
    if nickels == 1:
        print("1 nickel") 
    else:
        print(nickels, "nickels")

if pennies > 0:
    if pennies == 1:
        print("1 penny")
    else:
        print(pennies, "pennies")            