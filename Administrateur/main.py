from PySide2.QtWidgets import *
from PyQt5.QtWidgets import *
from Custom_Widgets.Widgets import *
import sys
import os

from MainFrontend import Ui_MainWindow
from connexion_db.connexion import connectToMysql

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        loadJsonStyle(self, self.ui)
        self.show()
        self.ui.SettingsBtn.clicked.connect(lambda: self.ui.CenterMenuContainer.expandMenu())
        self.ui.AboutBtn.clicked.connect(lambda: self.ui.CenterMenuContainer.expandMenu())
        self.ui.pushButton_9.clicked.connect(lambda: self.ui.CenterMenuContainer.expandMenu())
        self.ui.pushButton.clicked.connect(lambda: self.ui.CenterMenuContainer.collapseMenu())

        self.ui.EnregistrementDVC_2.clicked.connect(lambda: self.ui.rigthMenuContainer.expandMenu())
        self.ui.EnregistrerRTVS_2.clicked.connect(lambda: self.ui.rigthMenuContainer.expandMenu())
        self.ui.EnregistrementDVC_3.clicked.connect(lambda: self.ui.rigthMenuContainer.expandMenu())
        self.ui.EnregistrementDVC_4.clicked.connect(lambda: self.ui.rigthMenuContainer.expandMenu())
        self.ui.pushButton_2.clicked.connect(lambda: self.ui.rigthMenuContainer.collapseMenu())

        self.ui.ValidateRTVSBtn_3.clicked.connect(self.ValidateAdminForm)
        self.ui.pushButton_21.clicked.connect(self.ValidateDVCForm)
        self.ui.ValidateRTVSBtn.clicked.connect(self.ValidateRTVSForm)
        self.ui.ValidateRTVSBtn_2.clicked.connect(self.ValidateUserForm)
        self.connecter = connectToMysql()

    def ValidateRTVSForm(self):
        Numero_Sg = self.ui.lineEdit_27.text()
        Source = self.ui.lineEdit_28.text()
        Object_cour = self.ui.lineEdit_29.text()
        References_cour = self.ui.lineEdit_30.text()
        Cabinet = self.ui.lineEdit_3.text()
        Rejetter = self.ui.lineEdit_2.text()

        NumSG = "'" + Numero_Sg + "'"
        Source = "'" + Source + "'"
        Objet = str("'" + Object_cour + "'")
        ReferenceRTVS = "'" + References_cour + "'"
        Cabinet = "'" + Cabinet + "'"
        Rejeter = "'" + Rejetter + "'"

        self.valid = self.connecter.createRTVS(NumSG, Source, Objet, ReferenceRTVS, Cabinet, Rejeter)
        return self.valid
    
    def ValidateDVCForm(self):
        Numero_Sg = self.ui.lineEdit_19.text()
        Source_Objet = self.ui.lineEdit_20.text()
        ReferencesDVC = self.ui.lineEdit_21.text()
        Cotation = self.ui.lineEdit_22.text()
        Date = self.ui.dateEdit.date()
        Date.setDisplayFormat("yyyy-MM-dd")

        NumSG = "'" + Numero_Sg + "'"
        Source = "'" + Source_Objet + "'"
        referenceDVC = "'" + ReferencesDVC + "'"
        cotation = "'" + Cotation + "'"
        date_enrg = Date.toString("yyyy-MM-dd")

        valid = self.connecter.createDVC(NumSG, Source, referenceDVC, cotation, date_enrg)
        return valid
    
    def ValidateUserForm(self):
        nom = self.ui.lineEdit_34.text()
        prenom = self.ui.lineEdit_35.text()
        passWord = self.ui.lineEdit_36.text()
        telephone = self.ui.lineEdit_37.text()

        Noms = "'"+ nom +"'"
        Prenom = "'"+ prenom +"'"
        Password = "'" + passWord + "'"
        Telephone = "'" + telephone + "'"
        valid = self.connecter.createUser(Noms, Prenom, Password, Telephone)
        return valid
    
    def ValidateAdminForm(self):
        nom = self.ui.lineEdit_38.text()
        prenom = self.ui.lineEdit_39.text()
        passWord = self.ui.lineEdit_40.text()
        telephone = self.ui.lineEdit_41.text()

        Noms = "'"+ nom +"'"
        Prenom = "'"+ prenom +"'"
        Password = "'" + passWord + "'"
        Telephone = "'" + telephone + "'"
        valid = self.connecter.createAdmin(NomAdministrateur=Noms, PrenomAdministrateur=Prenom, PassWordAdministrateur=Password, TelephoneAdministrateur= Telephone)
        return valid


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())