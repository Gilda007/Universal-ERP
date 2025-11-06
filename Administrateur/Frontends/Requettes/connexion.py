import mysql.connector

class connectToMysql():
    def __init__(self):
         self.connexion = mysql.connector.connect( host='localhost',
                                            database ='midcaf_db', 
                                            user = 'Administrateur',
                                            password ='Administrateur123!')

    def connectUser(self, NomAdmin):
        cur = self.connexion.cursor()
        sql = "SELECT * FROM administrateur WHERE NomAdmin = {}".format(NomAdmin)
        cur.execute(sql)
        usersx = cur.fetchall()
        return usersx
    
    def connectUser2(self, password):
        cur = self.connexion.cursor()
        sql = "SELECT * FROM administrateur WHERE PassWordAdmin = {}".format(password)
        cur.execute(sql)
        passwordx = cur.fetchall()
        cur.close()
        return passwordx