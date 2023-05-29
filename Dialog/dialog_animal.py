# Pour le gestionnaire d'événement
from PyQt5.QtCore import pyqtSlot
# Importer la boite de dialogue
from Classes.Classe_Enclos import *
import UI_PY.Dialog_animal
from PyQt5 import QtWidgets
from PyQt5 import QtCore

# imports des classes
from Classes.Classe_Animal import *
from Classes.Classe_Mammifere import *
from Classes.Classe_Oiseau import *
from Classes.Classe_Reptile import *

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

        # Puisque Mammifères affiche par défaut, on désactive les contrôles oiseaux et reptiles
        self.lineEdit_longueur_bec.setDisabled(True)
        self.comboBox_venimeux.setDisabled(True)

        # Famille sélectionnée, exécuter méthode Controles_famille
        self.comboBox_famille_animal.currentIndexChanged.connect(self.Choisir_Famille)

    def Controles_Famille(self, p_fam):
        """
        Active et désactive les contrôles des famille d'animaux selon choix dans la combo box Famille)
        :param p_fam: La famille choisie.
        :return:
        """
        if p_fam == "Mammifères":
            self.lineEdit_longueur_bec.setDisabled(True)
            self.comboBox_venimeux.setDisabled(True)
            self.comboBox_couleur_poil.setEnabled(True)

        elif p_fam == "Oiseaux":
            self.comboBox_couleur_poil.setDisabled(True)
            self.comboBox_venimeux.setDisabled(True)
            self.lineEdit_longueur_bec.setEnabled(True)

        elif p_fam == "Reptiles":
            self.lineEdit_longueur_bec.setDisabled(True)
            self.comboBox_couleur_poil.setDisabled(True)
            self.comboBox_venimeux.setEnabled(True)


    def Choisir_Famille(self):
        """
        Méthode qui détermine quelle famille l'usager a choisi.
        :return: La famille d'animal
        """
        if self.comboBox_famille_animal.currentText() == "Mammifères":
            fam = "Mammifères"
        elif self.comboBox_famille_animal.currentText() == "Oiseaux":
            fam = "Oiseaux"
        else:
            fam = "Reptiles"
        self.Controles_Famille(fam)


        # On parcous la liste d'enclos pour ajouter les numéros d'enclos ajoutés au préalable dans la ComboBox
        for elt in Enclos.ls_enclos:
            self.comboBox_enclos_animal.addItem(elt.Numero_enclos)

    @QtCore.pyqtSlot()
    def on_pushButton_ajouter_clicked(self):
        """
        Gestionnaire d'événemnt du bouton ajouter.
        :return: Rien.
        """
        animal1 = Animal()








