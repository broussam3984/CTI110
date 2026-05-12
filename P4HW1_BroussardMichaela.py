# Michaela Broussard
# 04/08/2026
# P4HW1
# This Program collects scores, checks for valid input,
# drops the lowest score, calculates the average,
# and displays the letter grade.

# Ask user how many scores
num_scores = int(input("How many scores do you want to enter: "))

# Create empty list
score_list = []

# Loop to collect scores
for i in range(1, num_scores + 1):
    score = float(input(f"Enter score #{i}: "))

    # Validation loop
    while score < 0 or score > 100:
        print("\nINVALID Score entered!!!!")
        print("Score should be between 0 and 100")
        score = float(input(f"Enter score #{i} again: "))

    score_list.append(score)

# Find lowest score
lowest_score = min(score_list)

# Remove lowest score
score_list.remove(lowest_score)

# Calculate average
average = sum(score_list) / len(score_list)

# Determine letter grade
if average >= 90:
    grade = 'A'
elif average >= 80:
    grade = 'B'
elif average >= 70:
    grade = 'C'
elif average >= 60:
    grade = 'D'
else:
    grade = 'F'

# Display results
print("\n------------Results------------")
print(f"Lowest Score  : {lowest_score}")
print(f"Modified List : {score_list}")
print(f"Scores Average: {average:.2f} ")
print(f"Grade         : {grade}")
print("--------------------------------")                     