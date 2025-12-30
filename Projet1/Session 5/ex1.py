from classes.CompteBancaire import CompteBancaire
from classes.GestionComptes import GestionComptes

# Create GestionComptes instance
gestion_comptes = GestionComptes()
compte_selectionne = None

# Initial account creation
titulaire = input("Titulaire du premier compte : ")
solde = input("Solde initial : ")

while not CompteBancaire.verifierSolde(solde):
    solde = input("Solde non valide, Solde initial : ")

compte = CompteBancaire(titulaire, float(solde))
gestion_comptes.ajouterCompte(compte)
compte_selectionne = compte  # Set the first account as the selected one
print("✅ Premier compte créé et sélectionné.")


while True:
    print(f"""
            =============================
            🏦 MENU BANCAIRE
            =============================
            Compte sélectionné : {compte_selectionne.titulaire if compte_selectionne else 'Aucun'}
            -----------------------------
            1️⃣  Ajouter un compte
            2️⃣  Afficher tous les comptes
            --- Opérations sur le compte sélectionné ---
            3️⃣  Afficher les détails du compte
            4️⃣  Afficher le solde
            5️⃣  Afficher le titulaire
            6️⃣  Modifier le titulaire
            7️⃣  Déposer
            8️⃣  Retirer
            -------------------------------------------
            9️⃣  Afficher Nombre total des comptes
            🔟  Sélectionner un compte
            0️⃣  Quitter
            =============================
            """)

    choix_str = input("Votre choix : ")
    if not choix_str.isdigit():
        print("❌ Choix invalide")
        continue
    
    choix = int(choix_str)

    if choix in [3, 4, 5, 6, 7, 8] and compte_selectionne is None:
        print("❌ Aucun compte n'est sélectionné. Veuillez d'abord sélectionner un compte avec l'option 10.")
        continue

    match choix:
        case 1:
            while True:
                titulaire = input("Titulaire : ")
                if gestion_comptes.chercherCompteParTitulaire(titulaire):
                    print("❌ Un compte avec ce titulaire existe déjà. Veuillez choisir un autre nom.")
                else:
                    break
            
            solde = input("Solde initial : ")
            while not CompteBancaire.verifierSolde(solde):
                solde = input("Solde non valide, Solde initial : ")
            
            compte = CompteBancaire(titulaire, float(solde))
            gestion_comptes.ajouterCompte(compte)
            print(f"✅ Nouveau compte '{titulaire}' ajouté.")
        case 2:
            print("--- Affichage de tous les comptes ---")
            gestion_comptes.afficherComptes()
            print("------------------------------------")
        case 3:
            compte_selectionne.afficher()
        case 4:
            print(f"💰 Solde : {compte_selectionne.solde} DH")
        case 5:
            print(f"👤 Titulaire : {compte_selectionne.titulaire}")
        case 6:
            compte_selectionne.titulaire = input("Nouveau titulaire : ")
            print("✅ Titulaire modifié")
        case 7:
            montant = int(input("Montant à déposer : "))
            compte_selectionne.deposer(montant)
        case 8:
            montant = int(input("Montant à retirer : "))
            compte_selectionne.retirer(montant)
        case 9:
            print(f"Nombre total de comptes : {gestion_comptes.nombreComptes()}")
        case 10:
            titulaire_recherche = input("Entrez le titulaire du compte à sélectionner : ")
            compte_trouve = gestion_comptes.chercherCompteParTitulaire(titulaire_recherche)
            if compte_trouve:
                compte_selectionne = compte_trouve
                print(f"✅ Compte '{compte_selectionne.titulaire}' sélectionné.")
            else:
                print("❌ Aucun compte trouvé avec ce titulaire.")
        case 0:
            print("👋 Au revoir")
            break
        case _:
            print("❌ Choix invalide")
