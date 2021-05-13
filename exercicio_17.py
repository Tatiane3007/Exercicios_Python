# 17 - Leia um valor de comprimento em centímetros e apresente-o convertido em polegadas.
# P = C / 2.54

def cen_to_pol():
    centimetros = float(input("Digite o valor em centímetros: "))
    polegadas = centimetros / 2.54
    print(f"O comprimento convertido em polegadas é {polegadas}")
    
    
def main():
    cen_to_pol()


if __name__ == '__main__':
    main()
    
