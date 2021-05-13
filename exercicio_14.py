# 14 - Leia um ângulo em graus e apresente-o convertido em radianos.
# R = G * pi / 180

import math

def graus_to_rad():
    graus = float(input("Digite o ângulo em graus: "))
    radianos = graus * math.pi / 180
    print(f"O ângulo convertido em radianos é: {radianos}")
    
    
def main():
    graus_to_rad()


if __name__ == '__main__':
    main()
    
