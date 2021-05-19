# Crie uma lista vazia. Receba de um input do usuário 3 números e os adicione em sua lista. Printe por fim sua lista;

lista = []

num1 = float(input("Digite o primeiro número: "))
lista.append(num1)
num2 = float(input("Digite o segundo número: "))
lista.append(num2)
num3 = float(input("Digite o terceiro número: "))
lista.append(num3)

print(f"\nLista = {lista}")


# Com a lista dos números, ordene-os com algum método listado em dir(list);

lista.sort()
print(f"\nLista ordenada: {lista}")
