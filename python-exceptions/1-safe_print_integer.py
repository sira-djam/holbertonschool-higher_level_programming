#!/usr/bin/python3
def safe_print_integer(value):
    try:
        # Try to print the integer using the format method
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        # If the value cannot be formatted as an integer, return False
        return False
