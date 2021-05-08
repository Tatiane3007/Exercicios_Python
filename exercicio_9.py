# 9 - Leia uma temperatura em graus Celsius e apresente-a convertidade em Kelvin.
# K = C + 273.15

def cel_to_kel():
    celsius = float(input("Digite a temperatura em Celsius: "))
    kelvin = celsius + 273.15
    print(f"A temperatura em Kelvin é {kelvin} K")

def main():
    cel_to_kel()

if __name__ == "__main__":
    main()
