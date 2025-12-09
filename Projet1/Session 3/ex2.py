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

while nombre < 0 or nombre > 365:
    nombre = int(input("donner un nombre valide :"))

total = 0
monthIndex = 0

for i in mois:
    if(total + i[1] < nombre):
        total = total + i[1]
    else:
        month = i
        break


result = f"le jour {nombre} correspont  au {nombre - total} {month[0]}"

print(result)



