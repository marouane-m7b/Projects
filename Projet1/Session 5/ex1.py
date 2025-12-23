class CompteBancaire:
    nbrCompte = 0
    def __init__(self, titulaire, solde):
        self.titulaire = titulaire
        self.solde = solde
        CompteBancaire.nbrCompte += 1

    @property
    def titulaire(self):
        return self.__titulaire

    @titulaire.setter
    def titulaire(self, titulaire):
        self.__titulaire = titulaire

    @property
    def solde(self):
        return self.__solde

    @solde.setter
    def solde(self, solde):
        if solde >= 0:
            self.__solde = solde
        else:
            print("❌ Solde positif requis")

    def __str__(self):
        return f"👤 Titulaire : {self.__titulaire}\n💰 Solde : {self.__solde} DH"

    def afficher(self):
        print("\n" + "-" * 30)
        print(self)
        print("-" * 30)

    def deposer(self, montant):
        if montant > 0:
            self.__solde += montant
            print(f"✅ {montant} DH ajoutés")
        else:
            print("❌ Montant invalide")

    def retirer(self, montant):
        if montant > 0 and self.__solde - montant >= 0:
            self.__solde -= montant
            print(f"✅ {montant} DH retirés")
        else:
            print("❌ Solde insuffisant")

    @staticmethod
    def verifierSolde(solde):
        try:
            solde = float(solde)
        except (ValueError, TypeError):
            return False

        if solde >= 0:
            return True
        else:
            return False



# ===== PROGRAMME PRINCIPAL =====

titulaire = input("Titulaire : ")
solde = input("Solde initial : ")
CompteBancaire.verifierSolde(solde)

while(not CompteBancaire.verifierSolde(solde)):
    solde = input("Solde initial : ")
    CompteBancaire.verifierSolde(solde)



cmp1 = CompteBancaire(titulaire, float(solde))  # ✅ CREATED ONCE

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
            cmp1.afficher()
        case 2:
            print(f"💰 Solde : {cmp1.solde} DH")
        case 3:
            print(f"👤 Titulaire : {cmp1.titulaire}")
        case 4:
            cmp1.titulaire = input("Nouveau titulaire : ")
            print("✅ Titulaire modifié")
        case 5:
            montant = int(input("Montant à déposer : "))
            cmp1.deposer(montant)
        case 6:
            montant = int(input("Montant à retirer : "))
            cmp1.retirer(montant)
        case 7:
            print(CompteBancaire.nbrCompte)
        case 0:
            print("👋 Au revoir")
            break
        case _:
            print("❌ Choix invalide")
