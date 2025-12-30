from classes.CompteBancaire import CompteBancaire


class GestionComptes:
    def __init__(self):
        self.comptes = []

    def ajouterCompte(self, compte):
        if not isinstance(compte, CompteBancaire):
            raise TypeError("Le paramètre doit être une instance de CompteBancaire")
        self.comptes.append(compte)

    def afficherComptes(self):
        if self.comptes:
            for compte in self.comptes:
                compte.afficher()
        else:
            print("La liste des comptes est vide")

    def nombreComptes(self):
        return len(self.comptes)

    def chercherCompteParTitulaire(self, titulaire):
        for compte in self.comptes:
            if compte.titulaire == titulaire:
                return compte
        return None