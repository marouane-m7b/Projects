List1= [3,4,5,3,4,5,1]

for i in range(0,len(List1)):
    for j in range(i,len(List1)-1):
        if i == j:
            List1.pop(i)

print(List1)