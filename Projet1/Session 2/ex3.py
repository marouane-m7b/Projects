num = int(input("Entrer le nombre des jours :"))

annee = int(num/365)
rest = num % 365
week = int(rest/7)
rest = rest % 7
day = rest

print(f"{num} jours = {annee} annee(s) {week} semaine(s) {day} jour(s)")