from classes.CompteBancaire import CompteBancaire
from classes.GestionComptes import GestionComptes

gestion_comptes = GestionComptes()

while True:
    try:
        n = int(input("Entrez le nombre de comptes à créer : "))
        if n > 0:
            break
        else:
            print("Le nombre de comptes doit être un entier strictement positif.")
    except ValueError:
        print("Veuillez entrer un nombre entier valide.")

i = 0
while i < n:
    print(f"\nSaisie du compte n°{i + 1}")
    try:
        titulaire = input("Titulaire : ")
        solde_str = input("Solde : ")
        solde = float(solde_str)

        if solde < 0:
            raise ValueError("Le solde ne peut pas être négatif.")

        compte = CompteBancaire(titulaire, solde)
        gestion_comptes.ajouterCompte(compte)
        i += 1
    except ValueError as e:
        print(f"Erreur de saisie : {e}. Veuillez recommencer la saisie pour ce compte.")
    except Exception as e:
        print(f"Une erreur est survenue : {e}. Veuillez recommencer la saisie pour ce compte.")

print("\n" + "="*30)
print("Opérations terminées.")
print(f"Nombre total de comptes créés : {gestion_comptes.nombreComptes()}")
print("="*30)

print("\nAffichage de la liste des comptes :")
gestion_comptes.afficherComptes()

