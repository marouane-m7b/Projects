from Vehicule import Vehicule

class Agence:
    def __init__(self, nom, adresse):
        self.nom = nom
        self.adresse = adresse
        self.vehicules = []
    
    def ajouterVehicule(self, vehicule: Vehicule):
        if vehicule.numero_immatriculation in [v.numero_immatriculation for v in self.vehicules]:
            raise Exception(f"Un véhicule avec l'immatriculation {vehicule.numero_immatriculation} existe déjà.")
        self.vehicules.append(vehicule)
    
    def rechercheVehicule(self, immatriculation):
        for vehicule in self.vehicules:
            if vehicule.numero_immatriculation == immatriculation:
                return vehicule
        raise Exception(f"Véhicule avec l'immatriculation {immatriculation} introuvable.")
    
    def supprimerVehicule(self, immatriculation):
        vehicule = self.rechercheVehicule(immatriculation)
        self.vehicules.remove(vehicule)
    
    def inventaire(self):
        if not self.vehicules:
            print("Aucun véhicule dans l'agence.")
            return
        print("Inventaire des véhicules:")
        for vehicule in self.vehicules:
            print(f"  - {vehicule}")
    
    def afficher(self):
        print(f"Agence: {self.nom}")
        print(f"Adresse: {self.adresse}")
        self.inventaire()