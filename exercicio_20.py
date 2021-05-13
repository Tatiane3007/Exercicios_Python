# 20 - Leia um valor de massa em quilogramas e apresente-o convertido em libras.
# L = K / 0.45

def kg_to_lib():
    quilogramas = float(input("Digite a massa em quilogramas: "))
    libras = quilogramas / 0.45
    print(f"A massa convertida em libras é {libras}")


def main():
    kg_to_lib()


if __name__ == '__main__':
    main()
    
