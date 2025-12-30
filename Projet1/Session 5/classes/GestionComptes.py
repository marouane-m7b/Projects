from classes.CompteBancaire import CompteBancaire


class GestionComptes:
    def __init__(self):
        self.list_comptes = []

    def ajouterCompte(self, compte):
        if not isinstance(compte,CompteBancaire):
            raise('Compte doit etre compte bancaire')
        self.list_comptes.append(compte)

    def afficherCompte(self):
        if self.list_comptes:
            for compte in self.list_comptes:
                compte.afficher()
        else:
            print("La liste des comptes est vide")

    def nombreComptes(self):
        return len(self.list_comptes)