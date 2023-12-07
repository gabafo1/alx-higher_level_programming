#!/usr/bin/python3

roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

def roman_to_int(roman_string):
  """
  Converts a Roman numeral to an integer.

  Args:
    roman_string: A string representing a Roman numeral.

  Returns:
    The integer equivalent of the Roman numeral.
  """
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    result = 0
    for i in range(len(roman_string)):
        current_value = roman_numerals[roman_string[i]]
        if i + 1 < len(roman_string) and current_value < roman_numerals[roman_string[i + 1]]:
            result -= current_value
        else:
            result += current_value
    return result
