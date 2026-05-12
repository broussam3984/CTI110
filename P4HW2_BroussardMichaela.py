# Michaela Broussard
# 04/08/2026
# P4HW2
# This program calculates gross pay for multiple employees,
# including overtime pay, regular pay, and totals for all employees

# Initialize totals
total_overtime_pay = 0
total_regular_pay = 0
total_gross_pay = 0
employee_count = 0

# Ask for first employee name
employee_name = input('Enter employee\'s name or "Done" to terminate: ')

# Sentinel loop
while employee_name != "Done":

    # Get hours worked and pay rate
    hours_worked = float(input(f"How many hours did {employee_name} work? "))
    pay_rate = float(input(f"What is {employee_name}'s pay rate? "))

    # Calculate overtime and regular hours
    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        regular_hours = 40
    else:
        overtime_hours = 0
        regular_hours = hours_worked

    # Calculate pays
    overtime_pay = overtime_hours * (pay_rate * 1.5)
    regular_pay = regular_hours * pay_rate
    gross_pay = regular_pay + overtime_pay

    # Display employee results
    print()
    print(f"Employee name:   {employee_name}")
    print()
    print("Hours Worked    Pay Rate    OverTime    OverTime Pay        RegHour Pay         Gross Pay")
    print("------------------------------------------------------------------------------------------")
    print(f"{hours_worked:<15.1f}{pay_rate:<12.2f}{overtime_hours:<12.1f}{overtime_pay:<20.2f}${regular_pay:<19.2f}${gross_pay:.2f}")
    print()

    # Update totals
    total_overtime_pay += overtime_pay
    total_regular_pay += regular_pay
    total_gross_pay += gross_pay
    employee_count += 1

    # Ask for next employee name
    employee_name = input('Enter employee\'s name or "Done" to terminate: ')

# Display totals
print()
print(f"Total number of employees entered: {employee_count}")
print(f"Total amount paid for overtime: ${total_overtime_pay:.2f}")
print(f"Total amount paid for regular hours: ${total_regular_pay:.2f}")
print(f"Total amount paid in gross: ${total_gross_pay:.2f}")    

