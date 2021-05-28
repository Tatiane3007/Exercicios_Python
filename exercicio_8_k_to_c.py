# 8 - Leia uma temperatura em graus Kelvin e apresente-a convertidade em Celsius.
# C = K - 273.15

def kel_to_cel():
    kelvin = float(input("Digite a temperatura em Kelvin: "))
    celsius = kelvin - 273.15
    print(f"A temperatura em Celsius e {celsius} °C")

def main():
    kel_to_cel()

if __name__ == "__main__":
    main()
