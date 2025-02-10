#!/usr/bin/python3
"""fonction for open fil in python"""


def write_file(filename="", text=""):
    """Opens the file in write mode ('w') with UTF-8 encoding."""
    """If the file doesn't exist, it will be created. If the file already exists,
    its content will be overwritten."""
    with open(filename, mode="w", encoding="utf-8") as file:
        """Writes the text into the file and returns the number
        of characters written."""
        return file.write(text)

