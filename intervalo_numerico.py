# crie um algoritmo que solicite 2 números ao usuário a apresente o intervalo numérico entre eles.

def intervalo():
    num1 = int(input("Digite um número: "))
    num2 = int(input("Digite outro número: "))

    if num1 > num2:
        while num2 < num1 - 1:
            num2 += 1
            print(f"{num2} ")
    else:
        while num1 < num2 - 1:
            num1 += 1
            print(f"{num1} ")

  
def main():
    intervalo()


if __name__ == '__main__':
    main()
