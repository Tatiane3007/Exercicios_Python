# 16 - Leia um valor de comprimento em polegadas e apresente-o convertido em centímetros.
# C = P * 2.54

def pol_to_cen():
    polegadas = float(input("Digite o valor em polegadas: "))
    centimetros = polegadas * 2.54
    print(f"O comprimento convertido em centímetros é {centimetros} cm")
    
    
def main():
    pol_to_cen()
    

if __name__ == '__main__':
    main()
    
