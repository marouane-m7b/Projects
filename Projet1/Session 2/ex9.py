num = float(input("Entrer Nombre Flottant :"))

result = None

for i in range(1, int(num)):
    if num > i ** 2 :
        result = i
    else:
        break

print(result)