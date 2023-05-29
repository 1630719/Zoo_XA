# Pour le gestionnaire d'événement
from PyQt5.QtCore import pyqtSlot
# Importer la boite de dialogue
import UI_PY.DialogRecherche
from PyQt5 import QtWidgets
from PyQt5 import QtCore

######################################################
###### DÉFINITIONS DE LA CLASSE Fenetrelistview ######
######################################################

class Fenetrerecherche(QtWidgets.QDialog, UI_PY.DialogRecherche.Ui_Dialog):
    def __init__(self, parent=None):
        """
        Constructeur de la fenêtre qui affiche la liste des étudiants
        """
        super(Fenetrerecherche, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Boîte de dialogue Recherche")

    @QtCore.pyqtSlot()
    def on_pushButton_afficher_clicked(self):
        """
        Gestionnaire d'événement du bouton rechercher.
        :return: Rien.
        """



