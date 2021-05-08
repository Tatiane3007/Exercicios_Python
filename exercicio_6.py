# 6 - Leia uma temperatura em graus Celsius e apresente-a convertidade em Fahrenheit.
# F = C * (9.0/5.0) + 32.0

def cel_to_fah():
    celsius = float(input("Digite a temperatura em Celsius: "))
    fahrenheit = celsius * (9 / 5) + 32
    print(f"A temperatura em Fahrenheit é {fahrenheit} F!")

def main():
    cel_to_fah()

if __name__ == "__main__":
    main()
