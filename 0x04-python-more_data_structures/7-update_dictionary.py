#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if key in a_dictionary:  # Update existing key
        a_dictionary[key] = value
    else:  # Add new key
        a_dictionary[key] = value
