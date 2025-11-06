import mysql.connector

class insertToMysql1():
    def __init__(self):
         self.connexion = mysql.connector.connect( host='localhost',
                                            database ='miNdcaf_db', 
                                            user = 'Utilisateur',
                                            password ='Utilisateur123!')

    def connectUser(self, NomUtilisateur):
        cur = self.connexion.cursor()
        sql = "SELECT * FROM utilisateur WHERE NomUtilisateur = ?".format(NomUtilisateur)
        cur.execute(sql)
        usersx = cur.fetchall()
        return usersx
    
    def connectUser2(self, password):
        cur = self.connexion.cursor()
        sql = "SELECT * FROM utilisateur WHERE PassWordUtilisateur = ?".format(password)
        cur.execute(sql)
        passwordx = cur.fetchall()
        cur.close()
        return passwordx
    
import mysql.connector

class insertToMysqldb2():
    def __init__(self):
         self.connexion = mysql.connector.connect( host='localhost',
                                            database ='miNdcaf_db', 
                                            user = 'Utilisateur',
                                            password ='Utilisateur123!')

    def connectUser(self, NomUtilisateur):
        cur = self.connexion.cursor()
        sql = "SELECT * FROM dvc WHERE NomUtilisateur".format(NomUtilisateur)
        cur.execute(sql)
        usersx = cur.fetchall()
        return usersx
    
    def findbyO(self, NomUtilisateur):
        cur = self.connexion.cursor()
        sql = "SELECT * FROM dvc WHERE NomUtilisateur".format(NomUtilisateur)
        cur.execute(sql)
        usersx = cur.fetchall()
        return usersx
    
    def connectUser2(self):
        cur = self.connexion.cursor()
        sql = "INSERT INTO `utilisateur` (`IdUtilisateur`, `NomUtilisateur`, `PrenomUtilisateur`, `PassWordUtilisateur`, `TelephoneUtilisateur`, `IdAdmin`) VALUES (NULL, ?, ?, ?, ?, NULL);"
        cur.execute(sql)
        cur.close()
    
    
