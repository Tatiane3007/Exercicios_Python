# crie um algoritmo que solicite uma palavra e verifique se é um palíndromo, printando o resultado.

def palindromo():
    palavra = input("Digite uma palavra: ")

    palavra_inversa = palavra[::-1].replace(' ', '').lower()

    if palavra.replace(' ', '').lower() == palavra_inversa:
        print(f"É um palíndromo")
    else:
        print(f"Não é palíndromo")

def main():
    palindromo()

if __name__ == '__main__':
    main()
    
