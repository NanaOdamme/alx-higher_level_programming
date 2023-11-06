#!/usr/bin/python3


class MyList(list):
    def print_sorted(self):
        # Sort the list in ascending order
        sorted_list = sorted(self)

        # Print the sorted list
        print(sorted_list)
