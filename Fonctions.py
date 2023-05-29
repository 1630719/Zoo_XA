from Classes.Classe_Animal import *
from Classes.Classe_Enclos import *

def Existe_ou_pas_enclos(p_Numero_enclos) -> bool:
    """
    Fonction qui parcours la liste pour voir si l'étudiant existe deja ou pas.
    :param p_num_etudiant: Numéro de l'étudiant entré dans la fenêtre
    :return: Retourne un booléen vrai si présent, false si absent de la liste.
    """
    for elt in Enclos.ls_enclos:
        if elt.Numero_enclos == p_Numero_enclos:
            return True
    return False

def Existe_ou_pas_animal(p_Numero_animal) -> bool:
    """
    Fonction qui détermine si l'animal existe déjà dans la liste ou non.
    :param p_Numero_animal: Le numéro de l'animal.
    :return: Un booléen True si présent, False si absent.
    """
    for elt in Animal.ls_animaux:
        if elt.Numero_animal == p_Numero_animal:
            return True
    return False
