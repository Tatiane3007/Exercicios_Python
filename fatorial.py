# Crie um algoritmo que solicite ao usuário um número e apresente o fatorial deste número como resultado.

num = int(input("Digite um número: "))

fatorial = num
aux = num

while aux > 1:
    fatorial *= (aux-1)
    aux -= 1

print(f"{num}! = {fatorial}")
