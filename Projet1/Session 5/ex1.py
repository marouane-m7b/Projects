from classes.CompteBancaire import CompteBancaire
from classes.GestionComptes import GestionComptes

# Create GestionComptes instance
gestion_comptes = GestionComptes()

# Initial account creation
titulaire = input("Titulaire : ")
solde = input("Solde initial : ")

while(not CompteBancaire.verifierSolde(solde)):
    solde = input("Solde non valide, Solde initial : ")

compte = CompteBancaire(titulaire, float(solde))
gestion_comptes.ajouterCompte(compte)
print("✅ Premier compte créé.")


while True:
    print("""
            =============================
            🏦 MENU BANCAIRE
            =============================
            1️⃣  Ajouter un autre compte
            2️⃣  Afficher tous les comptes
            --- Opérations sur le dernier compte ajouté ---
            3️⃣  Afficher les détails du compte
            4️⃣  Afficher le solde
            5️⃣  Afficher le titulaire
            6️⃣  Modifier le titulaire
            7️⃣  Déposer
            8️⃣  Retirer
            -------------------------------------------
            9️⃣  Afficher Nombre total des comptes
            0️⃣  Quitter
            =============================
            """)

    choix_str = input("Votre choix : ")
    if not choix_str.isdigit():
        print("❌ Choix invalide")
        continue
    
    choix = int(choix_str)

    match choix:
        case 1:
            titulaire = input("Titulaire : ")
            solde = input("Solde initial : ")
            while not CompteBancaire.verifierSolde(solde):
                solde = input("Solde non valide, Solde initial : ")
            
            compte = CompteBancaire(titulaire, float(solde)) # The 'compte' variable now refers to the new account
            gestion_comptes.ajouterCompte(compte)
            print("✅ Nouveau compte ajouté.")
        case 2:
            print("--- Affichage de tous les comptes ---")
            gestion_comptes.afficherCompte()
            print("------------------------------------")
        case 3:
            compte.afficher()
        case 4:
            print(f"💰 Solde : {compte.solde} DH")
        case 5:
            print(f"👤 Titulaire : {compte.titulaire}")
        case 6:
            compte.titulaire = input("Nouveau titulaire : ")
            print("✅ Titulaire modifié")
        case 7:
            montant = int(input("Montant à déposer : "))
            compte.deposer(montant)
        case 8:
            montant = int(input("Montant à retirer : "))
            compte.retirer(montant)
        case 9:
            print(f"Nombre total de comptes : {gestion_comptes.nombreComptes()}")
        case 0:
            print("👋 Au revoir")
            break
        case _:
            print("❌ Choix invalide")
