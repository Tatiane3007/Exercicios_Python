# 11 - Leia uma velocidade em m/s e apresente-a convertida em km/h.
# K = M * 3.6

def ms_to_km():
    metros_seg = float(input("Digite a velocidade em m/s: "))
    kilometros_hora = metros_seg * 3.6
    print(f"A velocidade convertida em km/h é: {kilometros_hora} km/h")
    
    
def main():
    ms_to_km()


if __name__ == '__main__':
    main()
