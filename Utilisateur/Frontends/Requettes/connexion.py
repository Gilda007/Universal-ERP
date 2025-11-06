import mysql.connector
from PyQt5.QtWidgets import QMessageBox

class connectToMysql():
    def __init__(self):
        self.connexion = mysql.connector.connect(host="localhost",
                                                    database='mindcaf_db',
                                                    user='Utilisateur',
                                                    password='Utilisateur123!')
    
    def connectUser(self, NomUtilisateur):
        cur = self.connexion.cursor()
        sql = "SELECT * FROM utilisateur WHERE NomUtilisateur = {};".format(NomUtilisateur)
        cur.execute(sql)
        usersx = cur.fetchall()
        return usersx
    
    def connectUser2(self, password):
        cur = self.connexion.cursor()
        sql = "SELECT * FROM utilisateur WHERE PassWordUtilisateur = {};".format(password)
        cur.execute(sql)
        passwordx = cur.fetchall()
        cur.close()
        return passwordx


    def createDVC(self, NumSG, Num_courrier, Num_cabinet, Source, Obejt_Src, referenceDVC, 
                Date, cotation1, Date1, cotation2, Date2, cotation3, Date3, fin_traitement, date_fin, 
                transmission_cabinet, date_transmission, renvoie_correction, date_renvoie, retour_correction, date_retour):
        cur = self.connexion.cursor()
        cur.execute("INSERT INTO dvc (IdDVC, NumSGDVC, Num_courrier, Num_cabinet, Source, Objet, ReferencesDVC, Date, Cotation1, Date1, Cotation2, Date2, Cotation3, Date3, fin_traitement, date_fin_traitement, transmission_cabinet, date_transmission_cabinet, renvoie_correction, date_renvoie, retour_correction, date_retour_correction) VALUES (NULL, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", 
                    (NumSG, Num_courrier, Num_cabinet, Source, Obejt_Src, referenceDVC, Date, cotation1, Date1, 
                    cotation2, Date2, cotation3, Date3, fin_traitement, date_fin, transmission_cabinet, date_transmission, 
                    renvoie_correction, date_renvoie, retour_correction, date_retour))
        self.connexion.commit()
        cur.close()

    def showDVCTable(self):
        cursor = self.connexion.cursor()
        sql = "SELECT * FROM dvc"
        cursor.execute(sql)
        reponse = cursor.fetchall()
        cursor.close()
        return reponse

    def findElementInDVCRegister(self, DVCelement):
        cur = self.connexion.cursor()
        sql = "SELECT * FROM dvc WHERE NumSGDVC = "+ DVCelement+""
        cur.execute(sql)
        result = cur.fetchall()
        cur.close()
        return result

    def findElementInDVCRegister2(self, DCVelement):
        cur = self.connexion.cursor()
        sql = "SELECT * FROM dvc WHERE Num_courrier = "+DCVelement+""
        cur.execute(sql)
        result2 = cur.fetchall()
        cur.close()
        return result2
        
    def findElementInDVCRegister3(self, DVCelement):
        cur3 = self.connexion.cursor()
        sql3 = "SELECT * FROM dvc WHERE Num_cabinet= "+DVCelement+""
        cur3.execute(sql3)
        result3 = cur3.fetchall()
        cur3.close()
        return result3

    def updateCourrierDVC(self, NumSG, Num_courrier, Num_cabinet, Source, Obejt_Src, referenceDVC,  cotation1, cotation2, cotation3, 
                fin_traitement, date_fin, transmission_cabinet, date_transmission, renvoie_correction, date_renvoie, retour_correction, date_retour, id):
        cur = self.connexion.cursor()
        cur.execute("UPDATE dvc SET NumSGDVC= %s, Num_courrier= %s, Num_cabinet= %s, Source= %s, Objet= %s, ReferencesDVC= %s, Cotation1= %s, Cotation2= %s, Cotation3= %s, fin_traitement= %s, date_fin_traitement = %s, transmission_cabinet = %s, date_transmission_cabinet = %s, renvoie_correction = %s, date_renvoie = %s, retour_correction = %s, date_retour_correction = %s WHERE idDVC= %s", 
                    (NumSG, Num_courrier, Num_cabinet, Source, Obejt_Src, referenceDVC, 
                cotation1, cotation2, cotation3, fin_traitement, date_fin, 
                transmission_cabinet, date_transmission, renvoie_correction, date_renvoie, retour_correction, date_retour, id))
        self.connexion.commit()
        cur.close()