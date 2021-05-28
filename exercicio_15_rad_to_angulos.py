# 15 - Leia um ângulo em radianos e apresente-o convertido em graus.
# G = R * 180 / pi

import math

def rad_to_graus():
    radianos = float(input("Digite o ângulo em radianos: "))
    graus = radianos * 180 / math.pi
    print(f"O ângulo convertido em graus é {graus}")
    
    
def main():
    rad_to_graus()


if __name__ == '__main__':
    main()
    
