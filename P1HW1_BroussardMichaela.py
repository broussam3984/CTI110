# Michaela Broussard
# 03/08/2026
# P1HW1
# This program collects numbers from the users, performs math calculations, and displays the results.

print("-----Calculating Exponents-----")
base = int(input("Enter an integer as the base value: "))
exponent = int(input("Enter an integer as the exponent"))

result = base ** exponent

print(base, "rasied to the power of", exponent, "is", result, "!!")

print("\n-----Addition and Subtraction-----")
num1 = int(input("Enter a starting integer: "))
num2 = int(input("Enter an integer to add: "))
num3 = int(input("Enter an integer to subtract: "))

sum_result = num1 + num2
final_result = sum_result -num3

print(num1, "+", num2, "-", num3, "is equal to", final_result)