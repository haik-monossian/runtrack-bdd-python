import mysql.connector

class Employe:
    def __init__(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Haik2004.",
            database="entreprise"
        )
        self.cursor = self.db.cursor(buffered=True)
        self._setup_database()

    def _setup_database(self):
        """Initialisation des tables si elles n'existent pas."""
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS service (
            id INT AUTO_INCREMENT PRIMARY KEY, 
            nom VARCHAR(255)
        );
        """)
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS employe (
            id INT AUTO_INCREMENT PRIMARY KEY, 
            nom VARCHAR(255), 
            prenom VARCHAR(255), 
            salaire FLOAT, 
            id_service INT,
            FOREIGN KEY (id_service) REFERENCES service(id) ON DELETE SET NULL
        );
        """)
        self.db.commit()

        # Remplissage par défaut du service Informatique pour les tests si vide
        self.cursor.execute("SELECT COUNT(*) FROM service")
        if self.cursor.fetchone()[0] == 0:
            self.cursor.execute("INSERT INTO service (nom) VALUES ('Informatique')")
            self.db.commit()

    def create(self, nom, prenom, salaire, id_service):
        """CREATE : Ajouter un nouvel employé."""
        sql = "INSERT INTO employe (nom, prenom, salaire, id_service) VALUES (%s, %s, %s, %s)"
        val = (nom, prenom, salaire, id_service)
        self.cursor.execute(sql, val)
        self.db.commit()
        return self.cursor.lastrowid

    def read_all(self):
        """READ : Récupérer tous les employés avec le nom de leur service."""
        query = """
        SELECT e.id, e.prenom, e.nom, e.salaire, s.nom 
        FROM employe e
        LEFT JOIN service s ON e.id_service = s.id
        """
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def update(self, id_employe, nom=None, prenom=None, salaire=None, id_service=None):
        """UPDATE : Mettre à jour les données d'un employé."""
        updates = []
        params = []
        if nom: updates.append("nom = %s"); params.append(nom)
        if prenom: updates.append("prenom = %s"); params.append(prenom)
        if salaire: updates.append("salaire = %s"); params.append(salaire)
        if id_service: updates.append("id_service = %s"); params.append(id_service)
        
        if not updates:
            return

        sql = f"UPDATE employe SET {', '.join(updates)} WHERE id = %s"
        params.append(id_employe)
        self.cursor.execute(sql, tuple(params))
        self.db.commit()

    def delete(self, id_employe):
        """DELETE : Supprimer un employé."""
        sql = "DELETE FROM employe WHERE id = %s"
        self.cursor.execute(sql, (id_employe,))
        self.db.commit()

    def close(self):
        """Fermer la connexion."""
        self.cursor.close()
        self.db.close()

# --- TESTS (CRUD) ---

if __name__ == "__main__":
    gestion_v1 = Employe()

    print("--- TEST OPÉRATIONS CRUD ---")

    # 1. CREATE
    print("\n1. Création d'un nouvel employé...")
    new_id = gestion_v1.create("Skywalker", "Anakin", 2000.0, 1)
    print(f"Employé créé avec l'ID : {new_id}")

    # 2. READ (Initial)
    print("\n2. Liste des employés (après ajout) :")
    for emp in gestion_v1.read_all():
        print(emp)

    # 3. UPDATE
    print(f"\n3. Mise à jour du salaire de l'employé {new_id}...")
    gestion_v1.update(new_id, salaire=9999.0)
    print("Salaire mis à jour.")

    # 4. READ (Après Update)
    print("\n4. Vérification après mise à jour :")
    for emp in gestion_v1.read_all():
        if emp[0] == new_id:
            print(f"Nouveau salaire pour {emp[1]} {emp[2]} : {emp[3]}€")

    # 5. DELETE
    print(f"\n5. Suppression de l'employé {new_id}...")
    gestion_v1.delete(new_id)
    print("Employé supprimé.")

    # 6. READ (Final)
    print("\n6. Liste finale pour vérification :")
    for emp in gestion_v1.read_all():
        print(emp)

    gestion_v1.close()