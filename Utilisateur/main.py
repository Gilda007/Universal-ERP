from PySide2.QtWidgets import *
from Custom_Widgets.Widgets import *
import sys
import os

from MainFrontend import Ui_MainWindow
from Frontends.Requettes.connexion import connectToMysql


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui= Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        
        loadJsonStyle(self, self.ui, jsonFiles=['style.json'])
        self.show()
        self.connecter = connectToMysql()
        
        self.showTableDVC()
        self.ui.SettingsBtn.clicked.connect(lambda: self.ui.CenterMenuContainer.expandMenu())
        self.ui.AboutBtn.clicked.connect(lambda: self.ui.CenterMenuContainer.expandMenu())
        self.ui.pushButton.clicked.connect(lambda: self.ui.CenterMenuContainer.collapseMenu())
        self.ui.pushButton_2.clicked.connect(lambda: self.ui.rigthMenuContainer.collapseMenu())
        self.ui.EnregistrementDVC_2.clicked.connect(lambda: self.ui.rigthMenuContainer.expandMenu())
        self.ui.pushButton_7.clicked.connect(lambda: self.ui.rigthMenuContainer.expandMenu())
        self.ui.ValidateRTVSBtn_4.clicked.connect(self.validateDVCForm)
        self.ui.ValidateRTVSBtn_3.clicked.connect(self.updateValueInDVCRegister)
        self.ui.pushButton_3.clicked.connect(self.showTableDVC)
        self.ui.pushButton_17.clicked.connect(self.search)

        self.ui.label_22.setText('')
        self.ui.label_56.setText('')
        self.ui.label_24.setText('')
        self.ui.label_25.setText('')
        self.ui.label_26.setText('')
        self.ui.label_27.setText('')
        self.ui.label_29.setText('')
        self.ui.label_32.setText('')
        self.ui.label_34.setText('')
        self.ui.label_5.setText('')

####################### fonction de validation des enregistrements
    
    def validateDVCForm(self):
        Numero_Sg = self.ui.lineEdit_7.text()
        Numero_courrier = self.ui.lineEdit_17.text()
        Numero_Cabinet = self.ui.lineEdit_9.text()
        Source = self.ui.lineEdit_11.text()
        objet = self.ui.lineEdit_12.text()
        ReferencesDVC = self.ui.lineEdit_14.text()
        Date = self.ui.dateEdit_6.date()
        cotation1 = self.ui.lineEdit_15.text()
        Date1 = self.ui.dateEdit_7.date()
        cotation2 = self.ui.lineEdit_19.text()
        Date2 = self.ui.dateEdit_8.date()
        cotation3 = self.ui.lineEdit_21.text()
        Date3 = self.ui.dateEdit_11.date()
        fin_traitement = self.ui.lineEdit_20.text()
        date_fin_traitement = self.ui.dateEdit_12.date()
        tranmission_courrier = self.ui.lineEdit_3.text()
        date_transmisson = self.ui.dateEdit_12.date()
        renvoie_correction = self.ui.lineEdit_3.text()
        date_renvoie = self.ui.dateEdit_13.date()
        retour_correction = self.ui.lineEdit_4.text()
        date_retour = self.ui.dateEdit_9.date()

        Num_Sg = "" + Numero_Sg + ""
        Numero_Courrier = "" + Numero_courrier +""
        Numero_cabinet = "" + Numero_Cabinet + ""
        source = "" + Source + ""
        Objet = str("" + objet + "")
        Reference = "" + ReferencesDVC + ""
        date_enrg = Date.toString("yyyy-MM-dd")
        Cotation1 = "" + cotation1 +""
        date1 = Date1.toString("yyyy-MM-dd")
        Cotation2 = "" + cotation2 +""
        date2= Date2.toString("yyyy-MM-dd")
        Cotation3 = "" + cotation3 + ""
        date3 = Date3.toString("yyyy-MM-dd")
        Fin_traitement = "" + fin_traitement +""
        date_fin = date_fin_traitement.toString("yyyy-MM-dd")
        Transmission_courrier = "" + tranmission_courrier +""
        Date_transmisson = date_transmisson.toString("yyyy-MM-dd")
        Renvoie_correction = "" + renvoie_correction +""
        Date_renvoi = date_renvoie.toString("yyyy-MM-dd")
        Retour_correction = "" + retour_correction +""
        Date_retour = date_retour.toString("yyyy-MM-dd")
        valid = self.connecter.createDVC(Num_Sg, Numero_Courrier, Numero_cabinet, source, Objet, Reference, date_enrg, 
                                         Cotation1, date1, Cotation2, date2, Cotation3, date3, Fin_traitement, date_fin, Transmission_courrier, Date_transmisson, Renvoie_correction,
                                         Date_renvoi, Retour_correction, Date_retour)
        self.showTableDVC()
        return valid

    def search(self):
        self.ui.tableWidget_2.clear()
        search_tem = self.ui.lineEdit_16.text()
        search_tem = "'" + search_tem + "'"
        valid = self.connecter.findElementInDVCRegister(search_tem)
        if valid:
            button_column = 14

            for row_index, row_data in enumerate(valid):
                for col_index, col_data in enumerate(row_data):
                    item = QTableWidgetItem(str(col_data))
                    self.ui.tableWidget_2.setItem(row_index, col_index, item)
                    # Ajouter un bouton dans la colonne spécifique pour chaque ligne
                    button = QPushButton("Information", self)
                    button.clicked.connect(lambda _, row=row_data: self.on_button_clickDVC(row))
                    self.ui.tableWidget_2.setCellWidget(row_index, button_column, button)
        else:
            valid2 = self.connecter.findElementInDVCRegister2(search_tem)
            if valid2:
                button_column = 14

                for row_index, row_data in enumerate(valid2):
                    for col_index, col_data in enumerate(row_data):
                        item = QTableWidgetItem(str(col_data))
                        self.ui.tableWidget_2.setItem(row_index, col_index, item)
                        # Ajouter un bouton dans la colonne spécifique pour chaque ligne
                        button = QPushButton("Information", self)
                        button.clicked.connect(lambda _, row=row_data: self.on_button_clickDVC(row))
                        self.ui.tableWidget_2.setCellWidget(row_index, button_column, button)
            else:
                valid3 = self.connecter.findElementInDVCRegister3(search_tem)
                button_column = 14

                for row_index, row_data in enumerate(valid3):
                    for col_index, col_data in enumerate(row_data):
                        item = QTableWidgetItem(str(col_data))
                        self.ui.tableWidget_2.setItem(row_index, col_index, item)
                        # Ajouter un bouton dans la colonne spécifique pour chaque ligne
                        button = QPushButton("Information", self)
                        button.clicked.connect(lambda _, row=row_data: self.on_button_clickDVC(row))
                        self.ui.tableWidget_2.setCellWidget(row_index, button_column, button)

    def showTableDVC(self):
        valid = self.connecter.showDVCTable()
        button_column = 22

        for row_index, row_data in enumerate(valid):
            for col_index, col_data in enumerate(row_data):
                item = QTableWidgetItem(str(col_data))
                self.ui.tableWidget_2.setItem(row_index, col_index, item)
                # Ajouter un bouton dans la colonne spécifique pour chaque ligne
                button = QPushButton("Information", self)
                button.clicked.connect(lambda _, row=row_data: self.on_button_clickDVC(row))
                self.ui.tableWidget_2.setCellWidget(row_index, button_column, button)

    def on_button_clickDVC(self, row):
        self.ui.CenterMenuContainer.expandMenu()
        # print(f"Bouton cliqué sur la ligne {row}")
        self.ui.label_4.setText(str(row[0]))
        self.ui.label_87.setText(str(row[5]))
        self.ui.label_45.setText(str(row[1]))
        self.ui.label_47.setText(str(row[2]))
        self.ui.label_49.setText(str(row[3]))
        self.ui.label_51.setText(str(row[4]))
        self.ui.label_53.setText(str(row[6]))
        self.ui.label_55.setText(str(row[7]))
        self.ui.label_58.setText(str(row[8]))
        self.ui.label_60.setText(str(row[9]))
        self.ui.label_62.setText(str(row[10]))
        self.ui.label_64.setText(str(row[11]))
        self.ui.label_66.setText(str(row[12]))
        self.ui.label_68.setText(str(row[13]))
        self.ui.label_70.setText(str(row[14]))
        self.ui.label_72.setText(str(row[15]))
        self.ui.label_74.setText(str(row[16]))
        self.ui.label_76.setText(str(row[17]))
        self.ui.label_78.setText(str(row[18]))
        self.ui.label_80.setText(str(row[19]))
        self.ui.label_82.setText(str(row[20]))
        self.ui.label_84.setText(str(row[21]))
        Numero_cabinet = self.ui.lineEdit_7.setText(str(row[1]))
        self.ui.lineEdit_17.setText(str(row[2]))
        Numero_Sg = self.ui.lineEdit_9.setText(str(row[3]))
        Source = self.ui.lineEdit_11.setText(str(row[4]))
        Object_cour = self.ui.lineEdit_12.setText(str(row[5]))
        References_cour = self.ui.lineEdit_14.setText(str(row[6]))
        # Date = self.ui.dateEdit_2.date().toString("yyyy-MM-dd")
        Cotation1 = self.ui.lineEdit_15.setText(str(row[8]))
        # Date1 = self.ui.dateEdit_3.date().toString("yyyy-MM-dd")
        Cotation2 = self.ui.lineEdit_19.setText(str(row[10]))
        # Date2 = self.ui.dateEdit_4.date().toString("yyyy-MM-dd")
        Cotation3 = self.ui.lineEdit_20.setText(str(row[12]))
        # Date3 = self.ui.dateEdit_5.date().toString("yyyy-MM-dd")
        # Ajoutez le traitement que vous souhaitez effectuer lorsque le bouton est cliqué pour une ligne spécifique

        # Ajouter le traitement que vous souhaitez effectuer lorsque le bouton est cliqué pour une ligne spécifique

    def updateValueInDVCRegister(self):
        id = self.ui.label_4.text()
        Numero_Sg = self.ui.lineEdit_7.text()
        Numero_courrier = self.ui.lineEdit_17.text()
        Numero_Cabinet = self.ui.lineEdit_9.text()
        Source = self.ui.lineEdit_11.text()
        objet = self.ui.lineEdit_12.text()
        ReferencesDVC = self.ui.lineEdit_14.text()
        # Date = self.ui.dateEdit_6.date()
        cotation1 = self.ui.lineEdit_15.text()
        # Date1 = self.ui.dateEdit_7.date()
        cotation2 = self.ui.lineEdit_19.text()
        # Date2 = self.ui.dateEdit_8.date()
        cotation3 = self.ui.lineEdit_21.text()
        # Date3 = self.ui.dateEdit_11.date()
        fin_traitement = self.ui.lineEdit_20.text()
        date_fin_traitement = self.ui.dateEdit_12.date()
        tranmission_courrier = self.ui.lineEdit_3.text()
        date_transmisson = self.ui.dateEdit_12.date()
        renvoie_correction = self.ui.lineEdit_3.text()
        date_renvoie = self.ui.dateEdit_13.date()
        retour_correction = self.ui.lineEdit_4.text()
        date_retour = self.ui.dateEdit_9.date()

        Num_Sg = "" + Numero_Sg + ""
        Numero_Courrier = "" + Numero_courrier +""
        Numero_cabinet = "" + Numero_Cabinet + ""
        source = "" + Source + ""
        Objet = str("" + objet + "")
        Reference = "" + ReferencesDVC + ""
        # date_enrg = Date.toString("yyyy-MM-dd")
        Cotation1 = "" + cotation1 +""
        # date1 = Date1.toString("yyyy-MM-dd")
        Cotation2 = "" + cotation2 +""
        # date2= Date2.toString("yyyy-MM-dd")
        Cotation3 = "" + cotation3 + ""
        # date3 = Date3.toString("yyyy-MM-dd")
        Fin_traitement = "" + fin_traitement +""
        date_fin = date_fin_traitement.toString("yyyy-MM-dd")
        Transmission_courrier = "" + tranmission_courrier +""
        Date_transmisson = date_transmisson.toString("yyyy-MM-dd")
        Renvoie_correction = "" + renvoie_correction +""
        Date_renvoi = date_renvoie.toString("yyyy-MM-dd")
        Retour_correction = "" + retour_correction +""
        Date_retour = date_retour.toString("yyyy-MM-dd")
        self.connecter.updateCourrierDVC(Num_Sg, Numero_Courrier, Numero_cabinet, source, Objet, Reference, 
                                         Cotation1, Cotation2, Cotation3, Fin_traitement, date_fin, Transmission_courrier, Date_transmisson, Renvoie_correction,
                                         Date_renvoi, Retour_correction, Date_retour, id)
        self.showTableDVC()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())