from datetime import datetime
from datetime import date


produits = {
    "Fromage": "2023-12-31",
    "Lait": "2022-10-15",
    "Jus Ananas": "2025-11-20",
    "Yaourt": "2026-11-22",
    "Beurre": "2024-05-18",
    "Crème Fraîche": "2023-11-02",
    "Poulet Frais": "2023-04-15",
    "Poisson Surgelé": "2026-02-10",
    "Pâtes": "2027-12-25",
    "Riz": "2028-01-01",
    "Café Moulu": "2025-03-10",
    "Thé Vert": "2026-07-18",
    "Chocolat Noir": "2025-10-11",
    "Biscuits": "2024-09-30",
    "Eau Minérale": "2030-06-01",
    "Soda": "2025-08-15",
    "Farine": "2026-01-01",
    "Sucre": "2032-12-30",
    "Huile d’Olive": "2027-03-25",
    "Confiture Fraise": "2024-01-21"
}

today = date.today()

new_produits = {}


for key, value in produits.items():
    if datetime.strptime(str(today), "%Y-%m-%d") < datetime.strptime(value, "%Y-%m-%d"):
        new_produits.update({key:value})

print(new_produits)