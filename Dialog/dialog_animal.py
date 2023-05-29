# Pour le gestionnaire d'événement
from PyQt5.QtCore import pyqtSlot
# Importer la boite de dialogue
import Fonctions
from Classes.Classe_Enclos import *
import UI_PY.Dialog_animal
from PyQt5 import QtWidgets
from PyQt5 import QtCore

# imports des classes
from Classes.Classe_Animal import *
from Classes.Classe_Mammifere import *
from Classes.Classe_Oiseau import *
from Classes.Classe_Reptile import *

# Xavier Ayotte
# 1630719
# Groupe 1


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

        # Bloc pour cacher les labels d'erreur
        self.label_erreur_poids_animal.setVisible(False)
        self.label_erreur_longueur_bec.setVisible(False)
        self.label_erreur_numero_animal_existe.setVisible(False)
        self.label_erreur_numero_animal_existe_pas.setVisible(False)
        self.label_erreur_numero_animal_invalide.setVisible(False)

        # On parcous la liste d'enclos pour ajouter les numéros d'enclos ajoutés au préalable dans la ComboBox
        for elt in Enclos.ls_enclos:
            self.comboBox_enclos_animal.addItem(elt.Numero_enclos)

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

    @QtCore.pyqtSlot()
    def on_pushButton_ajouter_clicked(self):
        """
        Gestionnaire d'événemnt du bouton ajouter.
        :return: Rien.
        """
        # Instancier un mammifère, oiseau ou reptile selon choix de l'utilisateur
        if self.comboBox_famille_animal.currentText() == "Mammifères":
            animal1 = Mammifere()
        elif self.comboBox_famille_animal.currentText() == "Oiseaux":
            animal1 = Oiseau()
        else:
            animal1 = Reptile()

        # PARTIE COMMUNE
        # On enregistre les attributs communs selons les données entrées dans la boite de dialogue
        animal1.Enclos = self.comboBox_enclos_animal.currentText()
        animal1.Numero_animal = self.lineEdit_numero_animal.text()
        animal1.Surnom = self.lineEdit_surnom_animal.text()
        animal1.Famille = self.comboBox_famille_animal.currentText()

        # Validation pour s'assurer que le poids est bien un int valide
        try:
            animal1.Poids = int(self.lineEdit_poids_animal.text())
            if animal1.Poids == 0 or animal1.Poids < 15:
                self.label_erreur_poids_animal.setVisible(True)
                self.lineEdit_poids_animal.clear()
        except:
            self.label_erreur_poids_animal.setVisible(True)
            self.lineEdit_poids_animal.clear()

        # Si Numero_animal invalide
        if animal1.Numero_animal == "":
            self.label_erreur_numero_animal_invalide.setVisible(True)
            self.lineEdit_numero_animal.clear()

        # Si numéro d'animal existe
        existe = Fonctions.Existe_ou_pas_animal(animal1.Numero_animal)
        if existe:
            self.lineEdit_numero_animal.clear()
            self.label_erreur_numero_animal_existe.setVisible(True)

        # PARTIE MAMMIFERE
        if self.comboBox_famille_animal.currentText() == "Mammifères":
            animal1.Couleur_poil = self.comboBox_couleur_poil.currentText()

        # PARTIE OISEAU
        if self.comboBox_famille_animal.currentText() == "Oiseaux":
            try:
                animal1.Longueur_bec = float(self.lineEdit_longueur_bec.text())
                if animal1.Longueur_bec == 0.0:
                    self.label_erreur_longueur_bec.setVisible(True)
                    self.lineEdit_longueur_bec.clear()
            except:
                self.label_erreur_longueur_bec.setVisible(True)
                self.lineEdit_longueur_bec.clear()

        # PARTIE REPTILE
        if self.comboBox_famille_animal.currentText() == "Réptiles":
            animal1.Venimeux = self.comboBox_venimeux.currentText()

        # Si tout est valide dans la partie commune
        if animal1.Poids != 0 and animal1.Numero_animal != "" and animal1.Surnom != "" and not existe:
            # Ajout à la liste
            Animal.ls_animaux.append(animal1)

            # On efface les line edits
            self.lineEdit_surnom_animal.clear()
            self.lineEdit_poids_animal.clear()
            self.lineEdit_longueur_bec.clear()
            self.lineEdit_numero_animal.clear()

            # On efface les labels d'erreurs
            self.label_erreur_poids_animal.setVisible(False)
            self.label_erreur_longueur_bec.setVisible(False)
            self.label_erreur_numero_animal_existe.setVisible(False)
            self.label_erreur_numero_animal_existe_pas.setVisible(False)
            self.label_erreur_numero_animal_invalide.setVisible(False)

            # Affichage de la liste des animaux
            for elt in Animal.ls_animaux:
                print(elt)

    @QtCore.pyqtSlot()
    def on_pushButton_rechercher_clicked(self):
        """
        Gestionnaire d'événement du bouton rechercher.
        :return: Rien.
        """
        num_anim = self.lineEdit_numero_animal

        for elt in Animal.ls_animaux:
            if elt.Numero_animal == num_anim:
                self.lineEdit_poids_animal.setText(elt.Poids)
                self.lineEdit_surnom_animal.setText(elt.Surnom)
            else:
                self.label_erreur_numero_animal_existe_pas.setVisible(True)

        print("bouton fonctionnel")

