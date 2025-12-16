chaine1 = "J'aime Python"

chaine1 = chaine1.upper()

print(id(chaine1))
chaine1 = chaine1.upper()
print(id(chaine1))

print(chaine1.isupper())

print(chaine1.capitalize())

print(chaine1.replace('PYTHON','JAVA'))

print(chaine1.find('PYTHON'))

print(chaine1[::-1])

print(chaine1.split(' '))

chemin = "C/bureau/test"
list_reps = chemin.split('/')
print(list_reps)

print("   Hello     ".strip())