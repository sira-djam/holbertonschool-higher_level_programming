#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0  # To keep track of the number of integers printed
    for i in range(x):
        try:
            # Try to print the integer using the format method
            print("{:d}".format(my_list[i]), end=" ")
            count += 1
        except (ValueError, TypeError):
            # If the value is not an integer, just skip it
            continue
    print()  # New line after printing all integers
    return count
