# Michaela Broussard
# 03/29/2026
# P3HW1_Debugging
# This program asks the user to enter 6 module grades,
# then displays the lowest grade, highest grade, sum,
# average, and the letter grade

# Enter grades for each module
grade1 = float(input("Enter grade for Module 1: "))
grade2 = float(input("Enter grade for Module 2: "))
grade3 = float(input("Enter grade for Module 3: "))
grade4 = float(input("Enter grade for Module 4: "))
grade5 = float(input("Enter grade for Module 5: "))
grade6 = float(input("Enter grade for Module 6: "))

# Store grades in a list
grade_list = [grade1, grade2, grade3, grade4, grade5, grade6]

# Calculate results
lowest = min(grade_list)
highest = max(grade_list)
total = sum(grade_list)
average = total / len(grade_list)

# Determine letter grade
if average >= 90:
    letter_grade = "A"
elif average >= 80:
    letter_grade = "B"
elif average >= 70:
    letter_grade = "C"
elif average >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"

# Display results
print("\n------------Results------------")
print(f"Lowest Grade:       {lowest}")
print(f"Highest Grade:      {highest}")
print(f"Sum of Grades:      {total}")
print(f"Average:            {average:.2f}")
print("---------------------------------------")
print(f"Your grade is: {letter_grade}")                    