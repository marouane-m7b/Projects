vehicules = ["train","bus","voiture","velo"]
couleurs = ["rouge","vert","blue","jaune"]

combinaison = []

for i in vehicules:
    for j in couleurs:
        if(not(i == "voiture" and j == "vert")):
            combinaison.append(f"{i} {j}")

# print(combinaison)

for i in combinaison:
    print(i)