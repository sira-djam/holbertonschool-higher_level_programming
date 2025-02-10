#!/usr/bin/python3
def read_file(filename=""):
    """ Open the file with the given filename using 'utf-8' encoding"""
    with open(filename, encoding="utf-8") as file:
        """ Read and print the content of the file
        without adding extra newlines"""
        print(file.read(), end="")
