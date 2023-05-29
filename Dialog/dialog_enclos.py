# Pour le gestionnaire d'événement
from PyQt5.QtCore import pyqtSlot
# Importer la boite de dialogue
import Fonctions
import UI_PY.Dialog_enclos
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from Classes.Classe_Enclos import *


# Xavier Ayotte
# 1630719
# Groupe 1


######################################################
###### DÉFINITIONS DE LA CLASSE Fenetrelistview ######
######################################################

class Fenetreenclos(QtWidgets.QDialog, UI_PY.Dialog_enclos.Ui_Dialog):
    def __init__(self, parent=None):
        """
        Constructeur de la fenêtre qui affiche la liste des étudiants
        """
        super(Fenetreenclos, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Boîte de dialogue Enclos")

        # Bloc pour cacher les labels d'erreur
        self.label_erreur_numero_enclos_existe.setVisible(False)
        self.label_erreur_nom_enclos.setVisible(False)
        self.label_erreur_numero_enclos_existe_pas.setVisible(False)
        self.label_erreur_validation_numero_enclos.setVisible(False)

    @QtCore.pyqtSlot()  # Code qui permet d'exécuter le clic une seule fois
    def on_pushButton_Ajouter_enclos_clicked(self):
        """
        Gestionnaire d'événement pour le bouton Ajouter_enclos
        :return: Rien.
        """

        # On instancie l'enclos
        enclos1 = Enclos()

        # Enregistrement des attriuts selon texte entré
        enclos1.Numero_enclos = self.lineEdit_numero_enclos.text()
        enclos1.Nom_enclos = self.lineEdit_nom_enclos.text()
        enclos1.Taille = self.comboBox_taille_enclos.currentText()
        enclos1.Type = self.comboBox_type_enclos.currentText()
        enclos1.Localisation = self.comboBox_localisation.currentText()

        # Si le numero d'enclos est invalide
        if enclos1.Numero_enclos == "":
            self.label_erreur_validation_numero_enclos.setVisible(True)
            self.lineEdit_numero_enclos.clear()

        # Si numero d'enclos existe:
        existe = Fonctions.Existe_ou_pas(enclos1.Numero_enclos)

        if existe :
            self.lineEdit_numero_enclos.clear()
            self.label_erreur_numero_enclos_existe.setVisible(True)

        # Si le nom est invalide
        if enclos1.Nom_enclos == "":
            self.label_erreur_nom_enclos.setVisible(True)
            self.lineEdit_nom_enclos.clear()

        # Si tout est valide
        if enclos1.Numero_enclos != "" and enclos1.Numero_enclos != "":

            # On enlève les labels d'erreur
            self.label_erreur_numero_enclos_existe.setVisible(False)
            self.label_erreur_nom_enclos.setVisible(False)
            self.label_erreur_numero_enclos_existe_pas.setVisible(False)
            self.label_erreur_validation_numero_enclos.setVisible(False)

            # On ajoute l'enclos à la liste
            Enclos.ls_enclos.append(enclos1)

            # On efface les line edits
            self.lineEdit_nom_enclos.clear()
            self.lineEdit_numero_enclos.clear()

            # Confirmation de l'ajout
            print("\nL'enclos a bien été ajouté!\n")

            # Affichage de la liste d'enclos
            for elt in Enclos.ls_enclos:
                print(elt)

    @QtCore.pyqtSlot()
    def on_pushButton_supprimer_enclos_clicked(self):
        """
        Gestionnaire d'événement du bouton supprimer_enclos
        :return: Rien.
        """
        # Instanciation de l'objet
        enclos2 = Enclos()

        # Ajout de l'attribut
        enclos2.Numero_enclos = self.lineEdit_numero_enclos.text()

        for elt in Enclos.ls_enclos:  # On parcous la liste d'enclos pour voir s'il existe ou non
            if enclos2.Numero_enclos == elt.Numero_enclos:  # Si l'enclos existe
                # Vider le line edit
                self.lineEdit_numero_enclos.clear()

                # Retirer l'enclos
                Enclos.ls_enclos.remove(elt)

                # Message de confirmation
                print("\nElement supprimé\n")

                # On affiche la nouvelle liste après suppression
                for elt1 in Enclos.ls_enclos:
                    print(elt1)

            # Si le numéro n'existe pas
            else:
                self.label_erreur_numero_enclos_existe_pas.setVisible(True)
                self.lineEdit_numero_enclos.clear()
