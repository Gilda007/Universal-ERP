from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton
import mysql.connector

# Connexion à la base de données
# db_connection = mysql.connector.connect( host='localhost',
#                                             database ='miNdcaf_db', 
#                                             user = 'Administrateur',
#                                             password ='Administrateur123!')

# # Créer un objet cursor pour exécuter des requêtes
# cursor = db_connection.cursor()

# # Exécuter une requête pour récupérer tous les éléments de la table
# query = "SELECT * FROM rtvs"
# cursor.execute(query)
# rows = cursor.fetchall()

# # Créer une application PyQt5
# app = QApplication([])

# # Créer une fenêtre principale
# window = QWidget()
# layout = QVBoxLayout()
# updateButton = QPushButton("Modifier")

# # Parcourir les éléments récupérés et créer des widgets pour les afficher
# for row in rows:
#     widget_label = QLabel(f"Élément : {row[0]}, {row[1]}, {row[2]}, {row[3]}, {row[4]}, {row[5]}, {row[6]}, {row[7]}, {row[8]}, {row[9]}, {row[10]}, {row[11]}, {row[12]}")  # Exemple de création d'un widget de type QLabel
#     widget = QWidget(f"Element: {widget_label}, {updateButton}")
#     layout.addWidget(widget)

# # Appliquer la mise en page à la fenêtre
# window.setLayout(layout)
# window.show()

# # Lancer l'application
# app.exec_()

class DataWidget(QWidget):
    def __init__(self, data):
        super(DataWidget, self).__init__()
        self.data = data

        layout = QVBoxLayout()
        self.setLayout(layout)

        label = QLabel(f"Élément : {data}")
        layout.addWidget(label)

        modify_button = QPushButton("Modifier")
        modify_button.clicked.connect(self.modify_data)
        layout.addWidget(modify_button)

    def modify_data(self):
        # Implémentez la logique pour la modification des données de l'élément
        # Utilisez self.data pour accéder aux informations de cet élément
        print(f"Modification des données : {self.data}")

class App(QWidget):
    def __init__(self):
        super(App, self).__init__()

        layout = QVBoxLayout()
        self.setLayout(layout)

        # Connexion à la base de données
        
        db_connection = mysql.connector.connect( host='localhost',
                                            database ='miNdcaf_db', 
                                            user = 'Administrateur',
                                            password ='Administrateur123!')
        cursor = db_connection.cursor()

        # Exécuter une requête pour récupérer tous les éléments de la table
        query = "SELECT * FROM rtvs"
        cursor.execute(query)
        rows = cursor.fetchall()

        # Créer un widget pour chaque élément et bouton de modification associé
        for row in rows:
            data_widget = DataWidget(row)
            layout.addWidget(data_widget)

if __name__ == "__main__":
    app = QApplication([])
    window = App()
    window.show()
    app.exec_()