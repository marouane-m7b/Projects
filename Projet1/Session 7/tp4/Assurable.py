from Vehicule import Vehicule

class Assurable(Vehicule):
    
    def calculer_montant_assurance(self):
        if self.prix_achat != "maintenance":
            return 0.02 * self.prix_achat
        else:
            raise Exception("Le véhicule est en maintenance, le montant de l'assurance ne peut pas être calculé.")