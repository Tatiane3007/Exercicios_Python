'''
Crie um código em Python que solicite do usuário o input de 2 números inteiros e assim divida o primeiro número pelo segundo. 
Caso o input não seja um número inteiro, seu código deve guiar o usuário até o preenchimento correto. 
Caso o usuário preencha com 0, que apresente mensagem falando sobre a indivisibilidade por zero. 
Caso o usuário não digite um número, informar que um número deve ser digitado. 
Em outros casos de erro, apresente ao usuário uma mensagem de erro inesperado.
'''

while True:
    try:
        num1 = int(input("Digite o 1º número inteiro: "))
        num2 = int(input("Digite o 2º número inteiro: "))
        div = num1 / num2
        print(f"{num1} / {num2} = {div:.2f}")
        break
    
    except ValueError:
        print("Tente novamente. O valor digitado deve ser um número inteiro.")

    except ZeroDivisionError:
        print("Não existe divisão por 0!")

    except EOFError:
        print("Um número deve ser digitado!")

    else:
        print("Erro inesperado!")
