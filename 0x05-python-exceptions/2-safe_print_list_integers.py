#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    integers_printed = 0
    try:
        for i in range(x):
            value = my_list[i]
            if isinstance(value, int):
                print("{:d}".format(value), end=' ')
                integers_printed += 1
    except (IndexError, ValueError, TypeError):
        pass

    print()
    return integers_printed


# Example usage:
my_list = [1, "two", 3, "four", 5]

x = 3
integers_printed_count = safe_print_list_integers(my_list, x)
print(f"Number of integers printed: {integers_printed_count}")
