notes = {"math":15,"pyhton":13.5,"francais":16}
notes["math"] = 18

print(notes)

# modifier et ajouter
notes.update({"python":0,"java":17})
print(notes)

# retourner un element
print(notes["francais"])
print(notes.get("francais","elemet introuvable"))

print(notes.keys())

print(notes.values())

print(notes.items())
# supprimer
notes.pop("java")
print(notes)

#supprimer le dernier element
notes.popitem()

# parcourir un dictionnaire
for elmt in notes:
    print(elmt)

for elmt, item in notes.items():
    print(elmt, item)

print(notes)
print(notes.items())