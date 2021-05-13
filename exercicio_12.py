# 12 - Leia uma distância em milhas e apresente-a convertida em quilômetros.
# K = 1.61 * M

def mil_to_km():
    milhas = float(input("Digite a distância em milhas: "))
    quilometros = 1.61 * milhas
    print(f"A distância convertida em quilometros é: {quilometros} km")
    

def main():
    mil_to_km()


if __name__ == '__main__':
    main()
