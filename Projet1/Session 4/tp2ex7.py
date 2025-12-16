# Écrivez un programme Python pour convertir une chaîne donnée en majuscule si elle
# contient au moins 2 caractères majuscules dans les 4 premiers caractères

str1 = "Hello"
str2 = "HiIiiiii"

def str_maj(my_str):
    count = 0
    count_Maj = 0
    for i in my_str:
        if count >= 4:
            break
        if i.isupper():
            count_Maj +=1
        count+=1
    if count_Maj >= 2:
        return my_str.upper()
    else:
        return my_str

print(str_maj(str1))
print(str_maj(str2))