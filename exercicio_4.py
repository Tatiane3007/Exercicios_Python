# 4 - Leia um número real e imprima o resultado do quadrado desse número.

def real():
    num = float(input("Digite um número real: "))
    print(f"O quadrado de {num} é {num**2}!")

def main():
    real()

if __name__ == "__main__":
    main()
