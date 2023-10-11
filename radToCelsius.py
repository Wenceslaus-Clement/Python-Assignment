#################################################
# CODE FOR CONVERTING RADIANS TO CELSIUS
#################################################

# Variables include
# radian_value and degree_value

import math

radian_value = float(input('Enter the radian value = '))

degree_value = math.degrees(radian_value)

degree_value2 = round(degree_value,0)

print(degree_value2)