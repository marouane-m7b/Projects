List1= [3,4,5,3,4,5,1]

for i in range(0,len(List1)):
    for j in range(i,len(List1)):
        if List1[i] == List1[j] and i != j:
            List1.remove(List1[j])
            break

print(List1)