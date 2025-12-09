tuple1 = ("casa",33.77,22.55)
# tuple1[1]=50.60 erreur pae ce que les tuples sont immuables
for item in tuple1:
    print(item)

print(tuple1.count("casa"))

print(tuple1.index(33.77))