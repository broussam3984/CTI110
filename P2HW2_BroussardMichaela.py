# Michaela Broussard
# 3/14/2026
# P2HW2 - List Statistics
# This program collect module grades, stores them in a list, and calculates statistics

# Pseudocode
# 1. Ask the user to enter grades for Module 1 through Module 6
# 2. Store each grade inside a list
# 3. Find the lowest grade in the list
# 4. Find the highest grade in the list
# 5. Find the sum of all grades
# 6. Calculate the average of the grades
# 7. Display the results formatted correctly

module1 = float(input("Enter grade for Module 1: "))
module2 = float(input("Enter grade for Module 2: "))
module3 = float(input("Enter grade for Module 3: "))
module4 = float(input("Enter grade for Module 4: "))
module5 = float(input("Enter grade for Module 5: "))
module6 = float(input("Enter grade for Module 6: "))

module_grades = [module1, module2, module3, module4, module5, module6]

lowest = min(module_grades)
highest = max(module_grades)
total = sum(module_grades)
average = total / len(module_grades)

print("\n------------Results------------")

print("Lowest Grade:", lowest)
print("Highest Grade:", highest)
print("Sum of Grades:", total)
print("Average:", format(average, ".2f"))