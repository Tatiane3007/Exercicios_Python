# Crie um algoritmo que receba 3 números como input do usuário e a seguir adicione-o dentro de um frozenset. 
# Ao término, aplique algum atributo frozenset e printe na tela. Utilize dir(frozenset) para selecionar o atributo.

set3 = set()

num1 = int(input("Digite o 1 número: "))
set3.add(num1)

num2 = int(input("Digite o 2 número: "))
set3.add(num2)

num3 = int(input("Digite o 3 número: "))
set3.add(num3)

froz3 = frozenset(set3.copy())

print(f"\n{froz3}")
print(type(froz3))
