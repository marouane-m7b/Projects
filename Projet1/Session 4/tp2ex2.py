Stock=["Ordinateur de bureau", "Ordinateur portable", 100, "Caméra", 310.28, "Haut-parleurs", 27.00, "Télévision", 1000, "Cartes mères", "clavier", 500, "barrettes de mémoires"]

print(Stock)

nmbrs = []
strings = []

for i in Stock:
    if isinstance(i,str):
        strings.append(i)
    elif isinstance(i,int):
        nmbrs.append(i)

print(nmbrs)
print(strings)

print(len(nmbrs))
print(len(strings))

strings.sort()
print(strings)

strings.sort(reverse=True)
print(strings)

nmbrs.sort()
print(nmbrs)

nmbrs.sort(reverse=True)
print(nmbrs)