# 18 - Leia um valor de volume em metros cúbicos e apresente-o convertido em litros.
# L = 1000 * M

def cub_to_lit():
    m_cub = float(input("Digite o volume em metros cúbicos: "))
    litros = 1000 * m_cub
    print(f"O volume convertido em litros é {litros} L")
    
    
def main():
    cub_to_lit()


if __name__ == '__main__':
    main()
    
