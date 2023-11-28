#!/usr/bin/python3
import random

# This line should not change
number = random.randint(-10000, 10000)

# Get the last digit of the number
lastdigit = abs(number) % 10

if number < 0:
    lastdigit = -(lastdigit)
thestring = "Last digit of {} is {}".format(number, lastdigit)
if lastdigit > 5:
    print(f"{thestring} and is greater than 5")
elif lastdigit == 0:
    print(f"{thstring} and  is 0")
elif lastdigit < 6:
    print(f"{thstring} and is less than 6 and not 0")

