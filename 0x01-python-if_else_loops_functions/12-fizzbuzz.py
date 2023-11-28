#!/usr/bin/python3
def fizzbuzz():
    for num in range(1, 101):
        # Check for multiples of both three and five first
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz", end=" ")
        # Check for multiples of three
        elif num % 3 == 0:
            print("Fizz", end=" ")
        # Check for multiples of five
        elif num % 5 == 0:
            print("Buzz", end=" ")
        # Print the number if it's not a multiple of three or five
        else:
            print(num, end=" ")

