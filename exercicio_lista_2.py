# Crie uma lista vazia. Receba do usuário, através de inputs, 3 palavras. Apresente-as em ordem alfabética inversa(de Z à A);

lista = []

p1 = input("Digite a primeira palavra: ")
lista.append(p1)
p2 = input("Digite a segunda palavra: ")
lista.append(p2)
p3 = input("Digite a terceira palavra: ")
lista.append(p3)

lista.sort(reverse=True)
print(f"lista inversa = {lista}")
