#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result_list = []

    for i in range(list_length):
        try:
            elem_1 = my_list_1[i] if i < len(my_list_1) else 0
            elem_2 = my_list_2[i] if i < len(my_list_2) else 0

            # Check if the elements are either integers or floats
            if not isinstance(elem_1, (int, float)) or not isinstance(elem_2, (int, float)):
                raise TypeError("wrong type")

            # Check if division by zero is attempted
            if elem_2 == 0:
                raise ZeroDivisionError("division by 0")

            result = elem_1 / elem_2
            result_list.append(result)

        except TypeError as e:
            print(e)
            result_list.append(0)
        except ZeroDivisionError as e:
            print(e)
            result_list.append(0)
        except IndexError:
            print("out of range")
            result_list.append(0)
        finally:
            pass

    return result_list
