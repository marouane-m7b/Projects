from Vehicule import Vehicule
from Assurable import Assurable
from Maintenable import Maintenable

class Camion(Vehicule, Assurable, Maintenable):
    def __init__(self, numero_immatriculation, date_achat, etat, prix_achat, capacite_charge):
        super().__init__(numero_immatriculation, date_achat, etat, prix_achat)
        self.capacite_charge = capacite_charge


    def __str__(self):
        return f"Numéro d'immatriculation: {self.numero_immatriculation}, Date d'achat: {self.date_achat}, État: {self.etat}, Prix d'achat: {self.prix_achat}, Capacité: {self.capacite_charge}"