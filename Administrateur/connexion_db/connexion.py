import mysql.connector

class connectToMysql():
    def __init__(self):
         self.connexion = mysql.connector.connect( host='localhost',
                                            database ='miNdcaf_db', 
                                            user = 'Administrateur',
                                            password ='Administrateur123!')
    

    def connectUser(self, NomUtilisateur):
        cur = self.connexion.cursor()
        sql = "SELECT * FROM utilisateur WHERE NomUtilisateur = {};".format(NomUtilisateur)
        cur.execute(sql)
        usersx = cur.fetchall()
        cur.close()
        return usersx
    
    def connectUser2(self, password):
        cur = self.connexion.cursor()
        sql = "SELECT * FROM utilisateur WHERE PassWordUtilisateur = {};".format(password)
        cur.execute(sql)
        passwordx = cur.fetchall()
        cur.close()
        return passwordx
    
    def createUser(self, NomUtilisateur, PrenomUtilisateur, PassWordUtilisateur, TelephoneUtilisateur):
        cur = self.connexion.cursor()
        sql = "INSERT INTO `utilisateur` (`IdUtilisateur`, `NomUtilisateur`, `PrenomUtilisateur`, `PassWordUtilisateur`, `TelephoneUtilisateur`) VALUES (NULL, "+ NomUtilisateur+", "+ PrenomUtilisateur+", "+ PassWordUtilisateur+", "+TelephoneUtilisateur+")"
        cur.execute(sql)
        self.connexion.commit()
        cur.close()

    def createAdmin(self, NomAdministrateur, PrenomAdministrateur, PassWordAdministrateur, TelephoneAdministrateur):
        cur = self.connexion.cursor()
        sql = "INSERT INTO `administrateur` (`IdAdmin`, `NomAdmin`, `PrenomAdmin`, `PassWordAdmin`, `TelephoneAdmin`) VALUES (NULL, "+ NomAdministrateur+", "+ PrenomAdministrateur+", "+ PassWordAdministrateur+", "+ TelephoneAdministrateur+");"
        cur.execute(sql)
        self.connexion.commit()
        cur.close()

    def createRTVS(self, NumSG, Source, Objet, ReferenceRTVS, Cabinet, Rejeter):
        cur = self.connexion.cursor()
        sql = "INSERT INTO `RTVS` (`IdCour`, `NumSG`, `Source`, `Objet`, `ReferenceRTVS`, `Cabinet`, `Rejeter`) VALUES (NULL, "+ NumSG +", "+ Source +", "+ Objet+ ", "+ ReferenceRTVS +", "+ Cabinet+", "+ Rejeter+");"
        cur.execute(sql)
        self.connexion.commit()
        cur.close()

    def createDVC(self, NumSG, Source, referenceDVC, cotation, date_enrg):
        cur = self.connexion.cursor()
        sql = "INSERT INTO `dvc` (`IdDVC`, `NumSGDVC`, `Obejt_Src`, `ReferencesDVC`, `CotationDVC`, `DateDVC`) VALUES (NULL, "+ NumSG +", "+ Source +", "+ referenceDVC +", "+ cotation+", "+ date_enrg+");"
        cur.execute(sql)
        self.connexion.commit()
        cur.close()

    def showUserTable(self):
        cur = self.connexion.cursor()
        sql = "SELECT NomUtilisateur, PrenomUtilisateur, PassWordUtilisateur, TelephoneUtilisateur FROM utilisateur"
        cur.execute(sql)
        cur.fetchall()
        columns = [i[0] for i in cur.description]
        cur.close()

    def showAdminTable(self):
        cur = self.connexion.cursor()
        sql = "SELECT NomAdministrateur, PrenomAdministrateur, PassWordAdministrateur, TelephoneAdministrateur FROM administrateur"
        cur.execute(sql)
        cur.fetchall()
        columns = [i[0] for i in cur.description]
        cur.close()

    def showRTVSTable(self):
        cur = self.connexion.cursor()
        sql = "SELECT NumSG, Source, Objet, ReferenceRTVS, Cabinet, Rejeter FROM rtvs"
        cur.execute(sql)
        cur.fetchall()
        columns = [i[0] for i in cur.description]
        cur.close()

    def showDVCTable(self):
        cur = self.connexion.cursor()
        sql = "SELECT NumSGDVC, Obejt_Src, ReferenceDVC, CotationDVC, DateDVC FROM dvc"
        cur.execute(sql)
        cur.fetchall()
        columns = [i[0] for i in cur.description]
        cur.close()

    def findElementInDVCRegister(self, DVCelement):
        cur = self.connexion.cursor()
        sql = "SELECT NumSGDVC, Obejt_Src, ReferenceDVC, CotationDVC, DateDVC FROM dvc WHERE Obejt_Src = "+ DVCelement+""
        cur.execute(sql)
        result = cur.fetchall()
        columns = [i[0] for i in cur.description]
        cur.close()

        if result:
            print(result)
        else:
            cur2 = self.connexion.cursor()
            sql2 = "SELECT NumSGDVC, Obejt_Src, ReferenceDVC, CotationDVC, DateDVC FROM dvc WHERE ReferenceDVC = "+DVCelement+""
            cur2.execute(sql2)
            columns = [i[0] for i in cur.description]
            cur2.close()
            result2 = cur2.fetchall()
            if result2:
                print(result2)
            else:
                cur3 = self.connexion.cursor()
                sql3 = "SELECT NumSGDVC, Obejt_Src, ReferenceDVC, CotationDVC, DateDVC FROM dvc WHERE  CotationDVC = "+DVCelement+""
                cur3.execute(sql3)
                result3 = cur3.fetchall()
                columns = [i[0] for i in cur.description]
                cur3.close()
                return result3

    def findElementInRTVSRegister(self, RTVSElement):
        cur = self.connexion.cursor()
        sql = "SELECT NumSG, Source, Objet, ReferenceRTVS, Cabinet, Rejeter FROM rtvs WHERE Source = "+RTVSElement+""
        cur.execute(sql)
        result = cur.fetchall()
        columns = [i[0] for i in cur.description]

        if result:
            print(result)
        else:
            cur2 = self.connexion.cursor()
            sql2 = "SELECT NumSG, Source, Objet, ReferenceRTVS, Cabinet, Rejeter FROM rtvs WHERE Objet = "+RTVSElement+""
            cur2.execute(sql2)
            result2 = cur2.fetchall()
            columns = [i[0] for i in cur.description]
            if result2:
                print(result2)
            else:
                cur3 = self.connexion.cursor()
                sql3 = "SELECT NumSG, Source, Objet, ReferenceRTVS, Cabinet, Rejeter FROM rtvs WHERE ReferenceRTVS = "+RTVSElement+""
                cur3.execute(sql3)
                result3 = cur3.fetchall()
                columns = [i[0] for i in cur.description]
                if result:
                    print(result3)
                else:
                    print('élément introuvable')

    def findElementInUserTable(self, UserElement):
        cur = self.connexion.cursor()
        sql = "SELECT NomUtilisateur, PrenomUtilisateur, PassWordUtilisateur, TelephoneUtilisateur FROM utilisateur WHERE NomUtilisateur = "+UserElement+""
        cur.execute(sql)
        result = cur.fetchall()
        columns = [i[0] for i in cur.description]

        if result:
            print(result)
        else:
            cur2 = self.connexion.cursor()
            sql2 = "SELECT NomUtilisateur, PrenomUtilisateur, PassWordUtilisateur, TelephoneUtilisateur FROM utilisateur WHERE PrenomUtilisateur = "+UserElement+""
            cur2.execute(sql2)
            result2 = cur2.fetchall()
            columns = [i[0] for i in cur.description]
            if result2:
                print(result2)
            else:
                cur3 = self.connexion.cursor()
                sql3 = "SELECT NomUtilisateur, PrenomUtilisateur, PassWordUtilisateur, TelephoneUtilisateur FROM utilisateur WHERE TelephoneUtilisateur = "+UserElement+""
                cur3.execute(sql3)
                result3 = cur3.fetchall()
                columns = [i[0] for i in cur.description]
                if result:
                    print(result3)
                else:
                    print('élément introuvable')


    def findElementInAdminTable(self, UserElement):
        cur = self.connexion.cursor()
        sql = "SELECT NomAdministrateur, PrenomAdministrateur, PassWordAdministrateur, TelephoneAdministrateur FROM administrateur WHERE NomAdministrateur = "+UserElement+""
        cur.execute(sql)
        result = cur.fetchall()
        columns = [i[0] for i in cur.description]

        if result:
            print(result)
        else:
            cur2 = self.connexion.cursor()
            sql2 = "SELECT NomAdministrateur, PrenomAdministrateur, PassWordAdministrateur, TelephoneAdministrateur FROM administrateur WHERE PrenomAdministrateur = "+UserElement+""
            cur2.execute(sql2)
            result2 = cur2.fetchall()
            columns = [i[0] for i in cur.description]
            if result2:
                print(result2)
            else:
                cur3 = self.connexion.cursor()
                sql3 = "SELECT NomAdministrateur, PrenomAdministrateur, PassWordAdministrateur, TelephoneAdministrateur FROM administrateur WHERE TelephoneAdministrateur = "+UserElement+""
                cur3.execute(sql3)
                result3 = cur3.fetchall()
                columns = [i[0] for i in cur.description]
                if result:
                    print(result3)
                else:
                    print('élément introuvable')