# 10 - Leia uma velocidade em km/h e apresente-a convertida em m/s.
# M = K / 3.6

def km_to_ms():
    kilometros = float(input("Digite a distância em km/h: "))
    metros_seg = kilometros / 3.6
    print(f"A distância em m/s é {metros_seg}")

def main():
    km_to_ms()

if __name__ == "__main__":
    main()
    
