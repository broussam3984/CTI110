# Michaela Broussard
# 03/08/2026
# P2LAB1
# This program calculates the diameter, circumference, and area of a circle using the radius entered by the user.

import math

radius = float(input("Enter the radius of the circle"))

diameter = 2 * radius
circumference = 2 * math.pi * radius
area = math.pi * radius ** 2

print(f"Diameter: {diameter:.1f}")
print(f"Circumference: {circumference:.2f}")
print(f"Area: {area:.3f}")