import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Haik2004.",
    database="laplateforme"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT capacite FROM salle")

myresult = mycursor.fetchall()
area=0

for x in myresult:
    area += x[0]

print(f"La surface de la plateforme fait {area} m²")

mycursor.close()
mydb.close()