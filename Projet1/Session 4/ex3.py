projets = {
"Projet1": {"responsable": "Ali", "budget": 50000, "statut": "en cours"},
"Projet2": {"responsable": "Sara", "budget": 75000, "statut": "terminé"},
"Projet3": {"responsable": "Omar", "budget": 30000, "statut": "en cours"},
"Projet4": {"responsable": "Lina", "budget": 60000, "statut": "en attente"}
}

def projets_en_cours(projets:dict):
    new_projets = projets.copy()
    for i, j in projets.items():
        for k, n in j.items():
            if k == 'statut' and n != 'en cours':
                new_projets.pop(i)
                break
    return new_projets


def budget_moyen(projets:dict):
    total = 0
    count = 0
    for i, j in projets.items():
        for k, n in j.items():
            if k == 'budget':
                total += n
                count += 1
    return total / count


def projet_plus_cher(projets):
    cher = None
    cher_amount = 0
    for i, j in projets.items():
        for k, n in j.items():
            if k == 'budget' and cher_amount < n:
                cher_amount = n
                cher = i
    return cher


print(projets_en_cours(projets))

print(budget_moyen(projets))

print(projet_plus_cher(projets))