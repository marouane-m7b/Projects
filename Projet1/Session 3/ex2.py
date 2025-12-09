mois = (
    ('Janvier', 31),
    ('Février', 28),
    ('Mars', 31),
    ('Avril', 30),
    ('Mai', 31),
    ('Juin', 30),
    ('Juillet', 31),
    ('Août', 31),
    ('Septembre', 30),
    ('Octobre', 31),
    ('Novembre', 30),
    ('Décembre', 31)
)

nombre = int(input("donner un nombre :"))
jour_year = nombre

while nombre < 0 or nombre > 365:
    nombre = int(input("donner un nombre valide :"))
    jour_year = nombre

total = 0
monthIndex = 0

for i in mois:
    if(total + i[1] < nombre):
        total = total + i[1]
    else:
        month = i
        break


result = f"le jour {nombre} correspont au {nombre - total} {month[0]}"

print(result)

# ================== Prof Solutiion ===================

jour_input = jour_year

i = 0

while jour_year > mois[i][1]:
    jour_year -= mois[i][1]
    i += 1


result = f"le jour {jour_input} correspont au {jour_year} {mois[i][0]}"

print(result)