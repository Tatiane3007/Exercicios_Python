# Crie um código em Python que peça um número ímpar do usuário. Caso o número seja par, apresente mensagem guiando o usuário até o preenchimento correto.

while True:
    try:
        impar = int(input("Digite um número ímpar: "))
        if impar % 2 != 0:
            print(impar)
            break
        else:
            raise ValueError("O número digitado deve ser ímpar!")
    except ValueError as ve:
        print(ve)
