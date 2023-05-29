from Classes.Classe_Enclos import *

def Existe_ou_pas(p_Numero_enclos) -> bool:
    """
    Fonction qui parcours la liste pour voir si l'étudiant existe deja ou pas.
    :param p_num_etudiant: Numéro de l'étudiant entré dans la fenêtre
    :return: Retourne un booléen vrai si présent, false si absent de la liste.
    """
    for elt in Enclos.ls_enclos:
        if elt.Numero_enclos == p_Numero_enclos:
            return True
    return False
