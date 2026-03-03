import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Haik2004.",
    database="laplateforme"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM etudiants")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)

mycursor.close()
mydb.close()
