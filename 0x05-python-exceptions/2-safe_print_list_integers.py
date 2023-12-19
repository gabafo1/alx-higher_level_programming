#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
  count = 0
  i = 0
  while i < x:
    try:
      element = my_list[i]
      if type(element) is int:
        print("{:d}".format(element), end="")
        count += 1
    except IndexError:
      # Reached the end of the list before x elements
      break
    i += 1
  # Newline at the end
  print()
  return count
