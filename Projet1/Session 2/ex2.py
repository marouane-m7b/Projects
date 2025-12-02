num1 = int(input("Nombre 1 :"))
num2 = int(input("Nombre 2 :"))
op = input("Operator :")
result = 0

if op == "+":
    result = num1 + num2
elif op == "-":
    result = num1 - num2
elif op == "x" or op == "*":
    result = num1 * num2
elif op == "/":
    result = num1 / num2


print(f"{num1} {op} {num2} = {result}")