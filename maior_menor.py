# Crie um algoritmo que solicite 5 números. Ao término, printar o maior e o menor número.

lista = []
aux = 1

while aux <= 5:
    lista.append(int(input(f"Digite o {aux}º número: ")))
    aux += 1

print(f"Maior número: {max(lista)}")
print(f"Menor número: {min(lista)}")
