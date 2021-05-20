# Crie um algoritmo que pede ao usuário para digitar 3 números, diferentes entre sí, um de cada vez. 
# A cada input do usuário insira o input dentro de um set e ao término printe na tela o output de seu set.

set3 = set()

num1 = int(input("Digite o 1 número: "))
set3.add(num1)

num2 = int(input("Digite o 2 número: "))
set3.add(num2)

num3 = int(input("Digite o 3 número: "))
set3.add(num3)

print(f"\nSet: {set3}")
print(type(set3))
