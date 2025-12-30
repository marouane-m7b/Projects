from classes.CompteBancaire import CompteBancaire
from classes.GestionComptes import GestionComptes

titulaire = input("Titulaire : ")
solde = input("Solde initial : ")
CompteBancaire.verifierSolde(solde)

while(not CompteBancaire.verifierSolde(solde)):
    solde = input("Solde initial : ")
    CompteBancaire.verifierSolde(solde)


compte = CompteBancaire(titulaire, float(solde)) 

while True:
    print("""
            =============================
            🏦 MENU COMPTE BANCAIRE
            =============================
            1️⃣  Afficher le compte
            2️⃣  Afficher le solde
            3️⃣  Afficher le titulaire
            4️⃣  Modifier le titulaire
            5️⃣  Déposer
            6️⃣  Retirer
            7️⃣  Afficher Nombre des comptes
            0️⃣  Quitter
            =============================
            """)

    choix = int(input("Votre choix : "))

    match choix:
        case 1:
            compte.afficher()
        case 2:
            print(f"💰 Solde : {compte.solde} DH")
        case 3:
            print(f"👤 Titulaire : {compte.titulaire}")
        case 4:
            compte.titulaire = input("Nouveau titulaire : ")
            print("✅ Titulaire modifié")
        case 5:
            montant = int(input("Montant à déposer : "))
            compte.deposer(montant)
        case 6:
            montant = int(input("Montant à retirer : "))
            compte.retirer(montant)
        case 7:
            print(CompteBancaire.nbrCompte)
        case 0:
            print("👋 Au revoir")
            break
        case _:
            print("❌ Choix invalide")
