# crie um algoritmo que solicite 2 números ao usuário a apresente o mmc entre eles.

def mmc():
    num1 = int(input("Digite um número: "))
    num2 = int(input("Digite outro número: "))

    a = num1
    b = num2

    resto = None

    while resto is not 0:
        resto = a % b
        a = b
        b = resto
    print(f"O MMC de ({num1}, {num2}) = {(num1 * num2) / a}")


def main():
    mmc()

if __name__ == '__main__':
    main()
