# 13 - Leia uma distância em quilômetros e apresente-a convertida em milhas.
# M = K / 1.61

def km_to_mil():
    km = float(input("Digite a distância em km: "))
    milhas = km / 1.61
    print(f"A distância convertida em milhas é: {milhas}")
    
    
def main():
    km_to_mil()


if __name__ == '__main__':
    main()
