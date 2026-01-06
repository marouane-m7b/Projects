from abc import ABC, abstractmethod
from datetime import date

class Vehicule(ABC):
    def __init__(self, numero_immatriculation, date_achat, etat, prix_achat):
        self.numero_immatriculation = numero_immatriculation

        if(isinstance(date_achat,date)):
            self.date_achat = date_achat
        else:
            raise TypeError("date_achat must be a datetime.date instance")
        
        if etat in ['disponible', 'loué', 'maintenance']:
            self.etat = etat
        else:
            raise ValueError("etat must be one of 'disponible', 'loué', or 'maintenance'")
        
        self.prix_achat = prix_achat


    def __str__(self):
        return f"Numéro d'immatriculation: {self.numero_immatriculation}, Date d'achat: {self.date_achat}, État: {self.etat}, Prix d'achat: {self.prix_achat}"
    
    @abstractmethod
    def type_vehicule(self):
        pass