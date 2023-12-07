#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    # Create an empty set to store the unique elements
    unique_elements = set()

    # Add all elements from set_1 that are not in set_2
    unique_elements.update(set_1 - set_2)

    # Add all elements from set_2 that are not in set_1
    unique_elements.update(set_2 - set_1)

    return unique_elements
