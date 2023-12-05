#!/usr/bin/python3
def print_list_integer(my_list=[]):
    # Check if the list is empty
    if not my_list:
        print("The list is empty.")
    else:
        # Loop through each element in the list
        for x in my_list:
            # Use str.format() to print the integer
            print("{:d}".format(x))
