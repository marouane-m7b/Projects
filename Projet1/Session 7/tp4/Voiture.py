from Vehicule import Vehicule
from Louable import Louable
from Assurable import Assurable
from Maintenable import Maintenable

class Voiture(Vehicule, Louable, Assurable, Maintenable):
    def __init__(self, numero_immatriculation, date_achat, etat, prix_achat, marque, modele, couleur):
        super().__init__(numero_immatriculation, date_achat, etat, prix_achat)
        self.marque = marque
        self.modele = modele
        self.couleur = couleur


    def __str__(self):
        return f"Numéro d'immatriculation: {self.numero_immatriculation}, Date d'achat: {self.date_achat}, État: {self.etat}, Prix d'achat: {self.prix_achat}, Marque: {self.marque}, Modèle: {self.modele}, Couleur: {self.couleur}"
