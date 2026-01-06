from Vehicule import Vehicule

class Louable(Vehicule):

    def louer(self):
        if self.etat == "disponible":
            self.etat = 'loué'
        else:
            raise Exception("Le véhicule n'est pas disponible pour la location.")

    def retourner(self):
        if self.etat == 'loué':
            self.etat = 'disponible'
        else:
            raise Exception("Le véhicule n'est pas loué, impossible de le retourner.")


    def est_disponible(self):
        return self.etat == 'disponible'