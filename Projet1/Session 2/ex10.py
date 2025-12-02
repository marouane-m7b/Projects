a = 0
b = 10

print("==== a =====")

while(a < b):
    print(a)
    a += 1

print("==== b =====")

while(b > 0):
    b -= 1
    if b % 2 == 1:
        print(b)