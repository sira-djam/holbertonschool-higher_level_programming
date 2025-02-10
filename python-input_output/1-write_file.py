#!/usr/bin/python3
def write_file(filename="", text=""):
    # Ouvre le fichier en mode écriture ('w') avec l'encodage UTF-8.
    """ Si le fichier n'existe pas, il sera créé. Si le fichier existe déjà,
    son contenu sera écrasé."""
    with open(filename, mode="w", encoding="utf-8") as file:
        # Écrit le texte dans le fichier et retourne le nombre de caractères écrits
        return file.write(text)
