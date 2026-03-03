import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Haik2004.",
    database="laplateforme"
)

mycursor = mydb.cursor()

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

mycursor.executemany("INSERT INTO etage (nom, numero, superficie) VALUES (%s, %s, %s)", etages_data)
mycursor.executemany("INSERT INTO salle (nom, id_etage, capacite) VALUES (%s, %s, %s)", salles_data)

mydb.commit()

mycursor.close()
mydb.close()

print("Données insérées avec succès.")