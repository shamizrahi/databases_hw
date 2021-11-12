#Name: Sharon Mizrahi
#
# Triangle.py computes information about right triangles.

import math

a = int(input("Enter the length of the first leg of the triangle: "))

b = int(input("Enter the length of the second leg of the triangle: "))
print()


if (a <= 0 or b <= 0):
    print("The lengths must be positive.")
else:

    h = round(math.sqrt((a ** 2) + (b ** 2)), 2) # hypotenuse
    print("The hypotenuse is: ", h, "inches")

    area = round((a*b/2), 1) 
    print("The area is: ", area, "sq in")