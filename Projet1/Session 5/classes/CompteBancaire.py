class CompteBancaire:
    nbrCompte = 0
    taux_interet = 0
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

    @staticmethod
    def calculerIntert(solde):
        CompteBancaire.taux_interet += solde * 0.03