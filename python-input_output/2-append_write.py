#!/usr/bin/python3
"""use fonction who use append"""

def write_file(filename="", text=""):
 """Opens the file in write mode ('w') with UTF-8 encoding."""
 with open(filename, mode="w", encoding="utf-8") as file:
        """Writes the text into the file and returns the number
        of characters written."""

        return file.write(text)
