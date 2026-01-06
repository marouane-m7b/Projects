from Voiture import Voiture
from Camion import Camion
from datetime import date

v1 = Voiture(immatriculation="123-A-45",date_achat=date(2022, 5, 10),prix_achat=90000,marque="Toyota",modele="Corolla",couleur="Blanc")
v2 = Voiture(immatriculation="456-B-78",date_achat=date(2021, 9, 20),prix_achat=120000,marque="Dacia",modele="Duster",couleur="Gris",)
c1 = Camion(immatriculation="789-C-10",date_achat=date(2020, 3, 15),prix_achat=250000,capacite_charge=12.5)

print(v1)
print(v2)
print(c1)