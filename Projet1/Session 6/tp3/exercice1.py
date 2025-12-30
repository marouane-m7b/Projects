class Produit:
    def __init__(self, nom, prix, quantite):
        self._nom = nom
        if prix > 0:
            self._prix = prix
        else:
            raise ValueError("Le prix doit être strictement positif.")
        if isinstance(quantite, int) and quantite >= 0:
            self._quantite = quantite
        else:
            raise ValueError("La quantité doit être un entier positif ou nul.")

    # Getters
    def get_nom(self):
        return self._nom

    def get_prix(self):
        return self._prix

    def get_quantite(self):
        return self._quantite

    # Setters
    def set_nom(self, nom):
        self._nom = nom

    def set_prix(self, prix):
        if prix > 0:
            self._prix = prix
        else:
            print("Erreur : Le prix doit être strictement positif.")

    def set_quantite(self, quantite):
        if isinstance(quantite, int) and quantite >= 0:
            self._quantite = quantite
        else:
            print("Erreur : La quantité doit être un entier positif ou nul.")

    def afficher_infos(self):
        print(f"Produit: {self._nom}")
        print(f"Prix: {self._prix} €")
        print(f"Quantité en stock: {self._quantite}")
        print("-" * 20)


class CatalogueProduits:
    def __init__(self):
        self.produits = []

    def ajouter_produit(self, produit):
        self.produits.append(produit)
        print(f"Produit '{produit.get_nom()}' ajouté au catalogue.")

    def afficher_produits(self):
        if not self.produits:
            print("Le catalogue est vide.")
            return
        print("--- Contenu du Catalogue ---")
        for produit in self.produits:
            produit.afficher_infos()
        print("---------------------------")

    def valeur_totale_stock(self):
        valeur_totale = sum(p.get_prix() * p.get_quantite() for p in self.produits)
        return valeur_totale


# Programme principal pour tester
if __name__ == "__main__":
    # Création de produits
    try:
        produit1 = Produit("Ordinateur Portable", 1200.50, 10)
        produit2 = Produit("Smartphone", 800.00, 25)
        produit3 = Produit("Clavier", 75.99, 50)
    except ValueError as e:
        print(f"Erreur lors de la création d'un produit : {e}")
        exit()

    # Création du catalogue
    catalogue = CatalogueProduits()

    # Ajout des produits au catalogue
    catalogue.ajouter_produit(produit1)
    catalogue.ajouter_produit(produit2)
    catalogue.ajouter_produit(produit3)
    print("\n")

    # Affichage de tous les produits du catalogue
    catalogue.afficher_produits()

    # Calcul et affichage de la valeur totale du stock
    valeur_stock = catalogue.valeur_totale_stock()
    print(f"La valeur totale du stock est de : {valeur_stock:.2f} €")

    # Test des setters avec des valeurs invalides
    print("\n--- Test des setters avec des valeurs invalides ---")
    produit1.set_prix(-50)
    produit2.set_quantite(-5)
    produit2.set_quantite(15.5)
    print("-------------------------------------------------")

    # Affichage des informations après tentative de modification
    print("\nInformations du produit 1 après tentative de modification invalide du prix:")
    produit1.afficher_infos()
