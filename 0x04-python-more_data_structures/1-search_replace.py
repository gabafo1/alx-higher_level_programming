#!/usr/bin/python
def search_replace(my_list, search, replace):
    # Create a new list to store the modified elements
    new_list = []

    # Iterate through the elements of the original list
    for element in my_list:
        # Check if the element is equal to the search element
        if element == search:
            # Replace the element with the new element
            new_list.append(replace)
        else:
            # Keep the original element if it doesn't match the search element
            new_list.append(element)

    return new_list
