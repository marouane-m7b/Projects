class Vehicule:
    def __init__(self, nom, prix):
        self._nom = nom
        self._prix = prix

    def emettre_son(self):
        print("Le véhicule émet un son générique.")

    def afficher_informations(self):
        print(f"Nom: {self._nom}")
        print(f"Prix: {self._prix:.2f} €")


class Voiture(Vehicule):
    def __init__(self, nom, prix, modele, annee):
        super().__init__(nom, prix)
        self._modele = modele
        self._annee = annee

    def emettre_son(self):
        print("Vroum vroum !")

    def afficher_informations(self):
        print("--- Informations de la Voiture ---")
        super().afficher_informations()
        print(f"Modèle: {self._modele}")
        print(f"Année: {self._annee}")


class Moto(Vehicule):
    def __init__(self, nom, prix, marque, puissance):
        super().__init__(nom, prix)
        self._marque = marque
        self._puissance = puissance

    def emettre_son(self):
        print("Brap brap !")

    def afficher_informations(self):
        print("--- Informations de la Moto ---")
        super().afficher_informations()
        print(f"Marque: {self._marque}")
        print(f"Puissance: {self._puissance} ch")


class Avion(Vehicule):
    def __init__(self, nom, prix, compagnie, vitesse_max):
        super().__init__(nom, prix)
        self._compagnie = compagnie
        self._vitesse_max = vitesse_max

    def emettre_son(self):
        print("Fshhhhhhhhhhhhh !")

    def afficher_informations(self):
        print("--- Informations de l'Avion ---")
        super().afficher_informations()
        print(f"Compagnie: {self._compagnie}")
        print(f"Vitesse maximale: {self._vitesse_max} km/h")


# Programme principal
if __name__ == "__main__":
    # Création des objets
    ma_voiture = Voiture("Voiture de sport", 50000.00, "Porsche 911", 2023)
    ma_moto = Moto("Moto de course", 15000.00, "Ducati", 200)
    mon_avion = Avion("Avion de ligne", 100000000.00, "Air France", 950)

    vehicules = [ma_voiture, ma_moto, mon_avion]

    # Appel des méthodes pour chaque véhicule
    for vehicule in vehicules:
        vehicule.afficher_informations()
        vehicule.emettre_son()
        print("-" * 30)
