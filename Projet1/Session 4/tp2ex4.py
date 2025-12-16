dictionnaire_pays_capitales = {
    'France': 'Paris',
    'Allemagne': 'Berlin',
    'Maroc': 'Rabat',
    'Espagne': 'Madrid',
    'Irak': 'Bagdad',
    'Italie': 'Rome'
}

dictionnaire_capitales_pays = {}

for key, value in dictionnaire_pays_capitales.items():
    dictionnaire_capitales_pays.update({value: key})

print(dictionnaire_capitales_pays)