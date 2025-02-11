#!/usr/bin/python3
#!/usr/bin/python3
import sys
import json

# Import des fonctions de sauvegarde et de chargement de JSON
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

# Nom du fichier où on va enregistrer les données
filename = "add_item.json"

# Essayer de charger les données existantes depuis le fichier JSON
try:
    my_list = load_from_json_file(filename)
except FileNotFoundError:
    # Si le fichier n'existe pas, on crée une liste vide
    my_list = []

# Ajouter les arguments de la ligne de commande à la liste (ignorer le premier argument qui est le script lui-même)
my_list.extend(sys.argv[1:])

# Sauvegarder la liste mise à jour dans le fichier
save_to_json_file(my_list, filename)
