# 3 - Peça ao usuário para digitar três valores inteiros e imprima a soma deles.

def soma():
    num1 = int(input("Digite o primeiro valor: "))
    num2 = int(input("Digite o segundo valor: "))
    num3 = int(input("Digite o terceiro valor: "))

    print(f"A soma dos valores é {num1 + num2 + num3}!")

def main():
    soma()

if __name__ == "__main__":
    main()
