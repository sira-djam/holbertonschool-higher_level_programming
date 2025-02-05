#!/usr/bin.python3
"""creation de sous classe"""


class MyList(list):
    """imprimer une liste ascendante"""


    def print_sorted(self):
        print(sorted(self))
