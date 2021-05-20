# Crie um código em Python que solicite do usuário o input de um número inteiro. 
# Caso haja preenchimento diferente, a máquina deve guiar o usuário até ajustar sua resposta.

while True:
    try:
        num = int(input("Digite um número inteiro: "))
        break

    except:
        print("Tente novamente. O valor digitado deve ser um número inteiro.")
        
