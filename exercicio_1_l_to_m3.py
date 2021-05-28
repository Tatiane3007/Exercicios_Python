# 19 - Leia um valor de volume em litros e apresente-o convertido em metros cúbicos.
# M = L / 1000

def lit_to_cub():
    litros = float(input("Digite o volume em litros: "))
    metros_cubicos = litros / 1000
    print(f"O volume convertido em metros cúbicos é {metros_cubicos}")
    
    
def main():
    lit_to_cub()


if __name__ == '__main__':
    main()
