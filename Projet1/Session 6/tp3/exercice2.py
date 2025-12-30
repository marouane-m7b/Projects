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
if __name__ == "__main__":
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
