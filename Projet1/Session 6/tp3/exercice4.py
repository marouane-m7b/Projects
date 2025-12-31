# Exercice 4 – Gestion des paiements (Polymorphisme)
# On souhaite développer une application permettant de gérer différents moyens de paiement.
#
# 1. Créer une classe de base Paiement avec la méthode effectuer_paiement(montant).
#
# 2. Créer les classes dérivées CarteCredit et PayPal héritant de Paiement :
#    - CarteCredit possède un attribut numero_carte
#    - PayPal possède un attribut email
#    - Chaque classe redéfinit effectuer_paiement(montant)
#
# 3. Créer une classe Commande avec :
#    - montant_commande
#    - moyen_paiement (objet de type Paiement)
#    - une méthode process_payment() utilisant le polymorphisme
#
# 4. Dans un programme principal :
#    - créer des commandes avec différents moyens de paiement
#    - appeler process_payment() et observer le comportement polymorphe.

from abc import ABC, abstractmethod

# 1. Classe de base Paiement
class Paiement(ABC):
    @abstractmethod
    def effectuer_paiement(self, montant):
        """
        Méthode abstraite pour effectuer un paiement.
        Cette méthode doit être implémentée par les classes filles.
        """
        pass

# 2. Classes dérivées
class CarteCredit(Paiement):
    def __init__(self, numero_carte, nom_titulaire):
        self.numero_carte = numero_carte
        self.nom_titulaire = nom_titulaire

    def effectuer_paiement(self, montant):
        print(f"Paiement de {montant:.2f} € effectué par carte de crédit.")
        print(f"Numéro de carte : **** **** **** {self.numero_carte[-4:]}")
        print(f"Titulaire : {self.nom_titulaire}")

class PayPal(Paiement):
    def __init__(self, email):
        self.email = email

    def effectuer_paiement(self, montant):
        print(f"Paiement de {montant:.2f} € effectué via PayPal.")
        print(f"Compte PayPal : {self.email}")

# 3. Classe Commande
class Commande:
    def __init__(self, montant_commande, moyen_paiement: Paiement):
        self.montant_commande = montant_commande
        self.moyen_paiement = moyen_paiement

    def process_payment(self):
        print(f"\nTraitement d'une commande de {self.montant_commande:.2f} €...")
        self.moyen_paiement.effectuer_paiement(self.montant_commande)

# 4. Programme principal
# Création des moyens de paiement
paiement_cc = CarteCredit(numero_carte="1234567890123456", nom_titulaire="Jean Dupont")
paiement_paypal = PayPal(email="jean.dupont@example.com")

# Création des commandes avec différents moyens de paiement
commande1 = Commande(montant_commande=150.75, moyen_paiement=paiement_cc)
commande2 = Commande(montant_commande=89.99, moyen_paiement=paiement_paypal)

# Appeler process_payment() et observer le comportement polymorphe
commande1.process_payment()
commande2.process_payment()
