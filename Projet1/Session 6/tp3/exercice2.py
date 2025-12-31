# Exercice 2 – Gestion d’une bibliothèque :
# On souhaite développer une application Python pour gérer des personnes, des adhérents, des
# auteurs et des livres dans une bibliothèque.
# 1. Créer une classe Personne avec les attributs privés : nom, prenom, email, tel et age.
#    - Ajouter un constructeur avec paramètres.
#    - Définir la méthode __str__().
#
# 2. Créer une classe Adherent héritant de Personne, avec un attribut num_adherent, et
#    redéfinir la méthode __str__().
#
# 3. Créer une classe Auteur héritant de Personne, avec un attribut num_auteur, et redéfinir la
#    méthode __str__().
#
# 4. Créer une classe Livre avec les attributs : isbn, titre et auteur (objet Auteur).
#    - Définir la méthode __str__().
#
# 5. Écrire un programme principal qui :
#    - crée un adhérent,
#    - crée un auteur,
#    - crée un livre écrit par cet auteur,
#    - affiche les informations de l’adhérent et du livre.

class Personne:
    def __init__(self, nom, prenom, email, tel, age):
        self._nom = nom
        self._prenom = prenom
        self._email = email
        self._tel = tel
        self._age = age

    def __str__(self):
        return f"Nom: {self._nom}, Prénom: {self._prenom}, Email: {self._email}, Tel: {self._tel}, Age: {self._age}"


class Adherent(Personne):
    def __init__(self, nom, prenom, email, tel, age, num_adherent):
        super().__init__(nom, prenom, email, tel, age)
        self._num_adherent = num_adherent

    def __str__(self):
        return f"Adhérent N°{self._num_adherent} - {super().__str__()}"


class Auteur(Personne):
    def __init__(self, nom, prenom, email, tel, age, num_auteur):
        super().__init__(nom, prenom, email, tel, age)
        self._num_auteur = num_auteur

    def __str__(self):
        return f"Auteur N°{self._num_auteur} - {super().__str__()}"


class Livre:
    def __init__(self, isbn, titre, auteur):
        self._isbn = isbn
        self._titre = titre
        self._auteur = auteur

    def __str__(self):
        return f"Livre: {self._titre}\nISBN: {self._isbn}\n{self._auteur}"


# Programme principal
# Crée un adhérent
adherent1 = Adherent("Dupont", "Jean", "jean.dupont@email.com", "0123456789", 35, "AD001")

# Crée un auteur
auteur1 = Auteur("Hugo", "Victor", "victor.hugo@email.com", "9876543210", 83, "AU001")

# Crée un livre écrit par cet auteur
livre1 = Livre("978-2-07-041311-9", "Les Misérables", auteur1)

# Affiche les informations de l’adhérent et du livre
print("--- Informations de l'adhérent ---")
print(adherent1)
print("\n--- Informations du livre ---")
print(livre1)
