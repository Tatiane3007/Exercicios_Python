# Crie um algoritmo que solicite ao usuário 3 números e printe na tela a média destes.

valor = 0
num = 1

while num <= 3:
    valor += float(input(f"Digite o {num}º número: "))
    num += 1

media = valor / 3
print(f"A média dos três números é: {media:.2f}")
