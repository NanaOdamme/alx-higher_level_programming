#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    # Initialize a variable to count the elements printed
    elements_printed = 0

    try:
        for i in range(x):
            # Try to print the element if it exists
            print(my_list[i], end=' ')
            elements_printed += 1
    except IndexError:
        # Handle the IndexError when x is greater than the length of my_list
        pass

    # Print a new line
    print()

    return elements_printed


# Example usage:
my_list = [1, 2, 3, 4, 5]
x = 3
printed_count = safe_print_list(my_list, x)
print(f"Number of elements printed: {printed_count}")
