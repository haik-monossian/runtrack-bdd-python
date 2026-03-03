import mysql.connector
import subprocess
import os

# Connexion à la base de données
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Haik2004.",
    database="laplateforme"
)

mycursor = mydb.cursor()

# Données à insérer
etages_data = [
    ('RDC', 0, 500),
    ('R+1', 1, 500)
]

salles_data = [
    ('Lounge', 1, 100),
    ('Studio Son', 1, 5),
    ('Broadcasting', 2, 50),
    ('Bocal Peda', 2, 4),
    ('Coworking', 2, 80),
    ('Studio Video', 2, 5)
]

# Insertions groupées
mycursor.executemany("INSERT INTO etage (nom, numero, superficie) VALUES (%s, %s, %s)", etages_data)
mycursor.executemany("INSERT INTO salle (nom, id_etage, capacite) VALUES (%s, %s, %s)", salles_data)

mydb.commit()

mycursor.close()
mydb.close()

print("Données insérées avec succès.")

# Exportation de la base de données
output_file = "laplateforme.sql"
# Utilisation du chemin absolu pour mysqldump sur Windows
mysqldump_path = r"C:\Program Files\MySQL\MySQL Server 8.0\bin\mysqldump.exe"
dump_cmd = [mysqldump_path, "-u", "root", "-pHaik2004.", "laplateforme"]

try:
    print(f"Exportation vers '{output_file}'...")
    with open(output_file, "w") as f:
        subprocess.run(dump_cmd, stdout=f, check=True, shell=True)
    print("Exportation réussie !")
except Exception as e:
    print(f"Erreur lors de l'exportation : {e}")
    print("Note: Vérifiez que le chemin vers mysqldump.exe est correct dans le script.")