def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            elem_1 = my_list_1[i] if i < len(my_list_1) else 0
            elem_2 = my_list_2[i] if i < len(my_list_2) else 0

            # Check if division by zero is going to occur
            if elem_2 == 0:
                raise ZeroDivisionError("division by 0")

            # Perform division
            division_result = elem_1 / elem_2
            result.append(division_result)

        except ZeroDivisionError:
            print("division by 0")
            result.append(0)

        except (TypeError, ValueError):
            print("wrong type")
            result.append(0)

        except IndexError:
            print("out of range")
            result.append(0)

        finally:
            # Clean up or additional logic can be added here if needed
            pass

    return result
