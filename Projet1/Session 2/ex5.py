import math

poids = int(input("Entrer votre poids"))
taille = int(input("Entrer votre taille en cm"))

imc = float(poids / ((taille / 100) ** 2))

print(f"Votre poids en Kg : {poids}")
print(f"Votre taille en cm : {taille}") 
print(f"imc : {imc:.2f}")


print("Interprétation : ", end="")
if imc >= 40:
    print("Obésité morbide ou massive")
elif imc > 35:
    print("Obésité sévère")
elif imc > 30:
    print("Obésité modérée")
elif imc > 25:
    print("Surpoids")
elif imc > 18.5:
    print("Corpulence normale")
elif imc > 16.5:
    print("Maigreur")
else:
    print("Famine")