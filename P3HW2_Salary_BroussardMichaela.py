# Michaela Broussard
# 03/29/2026
# P3HW2 Salary
# This program calculates an employee's regular pay, overtime pay,
# and gross pay based on hours worked and pay rate.

"""
Pseudocode:
1. Ask user to enter employee name
2. Ask user to enter number of hours worked
3. Ask user to enter employee pay rate
4. If hours worked is greater than 40:
      overtime hours = hours worked - 40
      regular hours = 40
   Else:
      overtime hours = 0
      regular hours = hours worked
5. Calculate overtime pay using 1.5 times pay rate
6. Calculate regular pay
7. Calculate gross pay
8. Display employee name
9. Display hours worked, pay rate, overtime hours, overtime pay,
   regular pay, and gross pay
"""

# User input
employee_name = input("Enter employee's name: ")
hours_worked = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))

# Decision structure for overtime
if hours_worked > 40:
    overtime_hours = hours_worked - 40
    regular_hours = 40
else:
    overtime_hours = 0
    regular_hours = hours_worked

# Pay calculations
overtime_pay = overtime_hours * (pay_rate * 1.5)
regular_pay = regular_hours * pay_rate
gross_pay = regular_pay + overtime_pay

# Output
print("---------------------------------------")
print("Employee name:   ", employee_name)
print()
print("Hours Worked    Pay Rate    OverTime    OverTime Pay    RegHour Pay    Gross Pay")
print("--------------------------------------------------------------------------------")

print(f"{hours_worked:<16.1f}{pay_rate:<12.1f}{overtime_hours:<12.1f}${overtime_pay:<15.2f}${regular_pay:<14.2f}${gross_pay:<.2f}")