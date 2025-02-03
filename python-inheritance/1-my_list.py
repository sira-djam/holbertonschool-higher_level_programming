#!/usr/bin.python3
class MyList(list):
    """creation de sous classe"""
    def print_sorted(self):
        """imprimer une liste ascendante"""
        print(sorted(self))
