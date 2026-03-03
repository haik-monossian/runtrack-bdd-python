import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Haik2004.",
    database="laplateforme"
)

mycursor = mydb.cursor()

try:
    mycursor.execute("CREATE TABLE etage (id INT AUTO_INCREMENT PRIMARY KEY, nom VARCHAR(255), numero INT, superficie INT);")
except mysql.connector.Error as err:
    print(f"Error: {err}")

try:
    mycursor.execute("CREATE TABLE salle (id INT AUTO_INCREMENT PRIMARY KEY, nom VARCHAR(255), id_etage INT, capacite INT);")
except mysql.connector.Error as err:
    print(f"Error: {err}")

mydb.commit()

mycursor.close()
mydb.close()
