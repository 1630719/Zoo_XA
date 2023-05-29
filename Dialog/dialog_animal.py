# Pour le gestionnaire d'événement
from PyQt5.QtCore import pyqtSlot
# Importer la boite de dialogue
from Classes.Classe_Enclos import *
import UI_PY.Dialog_animal
from PyQt5 import QtWidgets


######################################################
###### DÉFINITIONS DE LA CLASSE Fenetrelistview ######
######################################################

class Fenetreanimal(QtWidgets.QDialog, UI_PY.Dialog_animal.Ui_Dialog):
    def __init__(self, parent=None):
        """
        Constructeur de la fenêtre qui affiche la liste des étudiants
        """
        super(Fenetreanimal, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Boîte de dialogue animal")

        # On parcous la liste d'enclos pour ajouter les numéros d'enclos ajoutés au préalable dans la ComboBox
        for elt in Enclos.ls_enclos:
            self.comboBox_enclos_animal.addItem(elt.Numero_enclos)




