# liste initiale de prénoms
list_prenom = ["ali","ahmed","samia"]
# affiche le nombre d'éléments dans la liste
print(len(list_prenom))

# remplace l'élément à l'index 1 (deuxième élément)
list_prenom[1] = "aicha"

# ajoute 'marouane' à la fin de la liste
list_prenom.append("marouane")
# insère 'rania' à l'index 1 (les éléments suivants sont décalés)
list_prenom.insert(1,"rania")
# nouvelle liste à concaténer
list_prenom1 = ["noura","salim"]
# étend la première liste avec les éléments de list_prenom1
list_prenom.extend(list_prenom1)
# supprime et retourne l'élément à l'index 3 ; on l'affiche
print(list_prenom.pop(3))
# supprime la première occurrence de la valeur "aicha"
list_prenom.remove("aicha")
# affectation : list_prenom2 référence la même liste (pas de copie)
list_prenom2 = list_prenom
# copie superficielle (shallow copy) de la liste
list_prenom2 = list_prenom.copy()
# affiche la liste finale
print(list_prenom)

for i in range(len(list_prenom)):
    print(list_prenom[i])

for x in list_prenom:
    print(x)

for x,y in enumerate(list_prenom):
    print(x, y)

liste = [12,13,14,15,10,20,30]
print(liste[1:5:1])
print(liste[:5])
print(liste[::5])
print(liste[::-1])

liste.sort()
print(liste)
liste.sort(reverse=True)
print(liste)

liste.reverse()
print(liste)