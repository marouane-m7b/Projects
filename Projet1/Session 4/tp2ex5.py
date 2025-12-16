produits = {
'produit1': {'prix': 30, 'reduction': 10},
'produit2': {'prix': 30, 'reduction': 5},
'produit3': {'prix': 40, 'reduction': 10}
}

total = 0

for i, j in produits.items():
    prix = j['prix'] - j['prix']*j['reduction']/100
    total += prix

print(total)