num = float(input("Entrer Nombre Flottant :"))

for i in range(1, int(num)):
    if num > i ** 2 :
        print(f"{i}")
    else:
        break