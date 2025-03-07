#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    # Récupère les arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connecte-toi à la base de données MySQL
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Crée un curseur pour exécuter des requêtes SQL
    cursor = db.cursor()

    # Exécute la requête pour obtenir les états commençant par 'N'
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # Récupère tous les résultats
    states = cursor.fetchall()

    # Affiche les résultats
    for state in states:
        print(state)

    # Ferme le curseur et la connexion
    cursor.close()
    db.close()
